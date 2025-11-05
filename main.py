# main.py
import os
from datetime import date
from servicios.registro_servicios import RegistroServicios
from entidades.academico.facultad import Facultad
from entidades.academico.carrera import Carrera
from entidades.usuario.estudiante import Estudiante
from entidades.usuario.docente import Docente
from patrones.factory.materia_factory import MateriaFactory
from patrones.strategy.impl.promedio_simple import PromedioSimpleStrategy
from patrones.strategy.impl.promedio_ponderado import PromedioPonderadoStrategy
from servicios.academico.inscripcion_service import InscripcionService
from servicios.academico.evaluacion_service import EvaluacionService
from servicios.persistencia_service import PersistenciaService
from servicios.notificacion.sistema_alertas import SistemaAlertas, EventoAlerta
from patrones.observer.observer import Observer

# --- Observadores Concretos ---
class NotificadorEstudiante(Observer[EventoAlerta]):
    def actualizar(self, evento: EventoAlerta) -> None:
        print(f"|--> [Notif.Estudiante] Correo a {evento.destinatario}: {evento.mensaje[:50]}...")

class AuditoriaLog(Observer[EventoAlerta]):
    def actualizar(self, evento: EventoAlerta) -> None:
        print(f"|--> [AuditoriaLog] REGISTRO {evento.tipo}: {evento.remitente} -> {evento.destinatario}")


# ======================================================================
#                       INICIO DEL SISTEMA SIGEU
# ======================================================================

def inicializar_y_ejecutar():
    print("=====================================================================")
    print("      SISTEMA INTEGRAL DE GESTIÓN EDUCATIVA UNIVERSITARIA (SIGEU)    ")
    print("=====================================================================")

    # 1. SETUP DEL SINGLETON (Service Registry)
    registro = RegistroServicios.get_instance()
    print(f"\n--- 1. SINGLETON (RegistroServicios) --- ID: {id(registro)}")

    # 2. GESTIÓN ACADÉMICA (HU1, HU2)
    print("\n--- 2. GESTIÓN ACADÉMICA (Facultad, Carrera) ---")
    
    # HU1: Crear Facultad
    facultad = Facultad("Facultad de Ingeniería", "FI", "Av. San Martín 123")
    registro.registrar_entidad(facultad, 'Facultad', facultad.codigo)
    
    # HU2: Crear Carrera
    carrera = Carrera("Ingeniería de Software", "IS", 5)
    registro.registrar_entidad(carrera, 'Carrera', carrera.codigo)
    facultad.asociar_carrera(carrera.codigo)
    
    # HU5: Alta de Docente
    docente1 = Docente(dni=30123456, nombre="Dr. Alan Turing", titulo="PhD en CS", fecha_alta="2020-01-01")
    registro.registrar_entidad(docente1, 'Docente', docente1.dni)

    # 3. FACTORY METHOD (HU3: Alta de Materias)
    print("\n--- 3. FACTORY METHOD (MateriaFactory) ---")
    
    # Materia Teórica (creada por Factory)
    materia_teo = MateriaFactory.crear_materia("Teorica", "Estructuras de Datos", "ED-301", 6, carrera.codigo)
    registro.registrar_entidad(materia_teo, 'Materia', materia_teo.codigo)
    carrera.agregar_materia(materia_teo.codigo)
    materia_teo.asignar_docente(docente1.dni)
    
    # Materia Práctica (creada por Factory)
    materia_lab = MateriaFactory.crear_materia("Laboratorio", "Programación Avanzada", "PA-302", 4, carrera.codigo)
    registro.registrar_entidad(materia_lab, 'Materia', materia_lab.codigo)
    carrera.agregar_materia(materia_lab.codigo)

    # Establecer Correlativas (HU2, HU4 - simulación)
    carrera.establecer_correlativa("ED-301", "INTRO-101") # Supongamos que INTRO-101 es la correlativa
    print(f"Materias creadas: {materia_teo.nombre}, {materia_lab.nombre}")
    
    # 4. GESTIÓN ESTUDIANTIL (HU8)
    estudiante1 = Estudiante(
        dni=40555666, 
        nombre="Lucia Garcés", 
        legajo="L40555", 
        email_institucional="lucia.g@fi.edu.ar", 
        carrera_codigo=carrera.codigo
    )
    registro.registrar_entidad(estudiante1, 'Estudiante', estudiante1.legajo)
    # Simular materia aprobada para pasar correlativa de PA-302
    estudiante1.historial_academico["INTRO-101"] = 'APROBADA' 

    # 5. INSCRIPCIÓN (HU9, HU4)
    inscripcion_service = InscripcionService()
    print("\n--- 5. INSCRIPCIÓN Y CORRELATIVAS ---")
    
    # Intento de inscripción fallida (ejemplo con una materia inventada sin aprobar)
    try:
        inscripcion_service.inscribir_estudiante_a_materia(estudiante1.legajo, "ED-301") 
    except PermissionError as e:
        print(f"[ERROR HU4] Correlativa fallida: {e}")
        # Hacemos que pase la correlativa para el ejemplo
        estudiante1.historial_academico["INTRO-101"] = 'APROBADA' 
        inscripcion_service.inscribir_estudiante_a_materia(estudiante1.legajo, "ED-301") # Ahora sí se inscribe

    # Inscripción exitosa
    inscripcion_service.inscribir_estudiante_a_materia(estudiante1.legajo, "PA-302")

    # 6. STRATEGY METHOD (HU7, HU10)
    print("\n--- 6. STRATEGY METHOD (Evaluación y Promedio) ---")
    
    # Estrategia 1: Promedio Simple
    evaluacion_simple = EvaluacionService(PromedioSimpleStrategy())
    evaluacion_simple.registrar_evaluacion(estudiante1.legajo, "ED-301", "Parcial 1", 7.0)
    evaluacion_simple.registrar_evaluacion(estudiante1.legajo, "ED-301", "Parcial 2", 9.0)
    promedio_simple = evaluacion_simple.calcular_promedio_final(estudiante1.legajo, "ED-301")
    print(f"Promedio final simple: {promedio_simple:.2f}")

    # Estrategia 2: Promedio Ponderado
    evaluacion_ponderada = EvaluacionService(PromedioPonderadoStrategy())
    evaluacion_ponderada.registrar_evaluacion(estudiante1.legajo, "PA-302", "Parcial 1", 7.0, peso=0.4)
    evaluacion_ponderada.registrar_evaluacion(estudiante1.legajo, "PA-302", "Trabajo Final", 9.0, peso=0.6)
    promedio_ponderado = evaluacion_ponderada.calcular_promedio_final(estudiante1.legajo, "PA-302")
    print(f"Promedio final ponderado: {promedio_ponderado:.2f}")

    # 7. OBSERVER PATTERN (HU11)
    print("\n--- 7. OBSERVER PATTERN (Sistema de Alertas) ---")
    alertas = SistemaAlertas()
    
    # Suscribir observadores
    notificador_estudiante = NotificadorEstudiante()
    auditor_log = AuditoriaLog()
    
    alertas.agregar_observador(notificador_estudiante)
    alertas.agregar_observador(auditor_log)
    
    # Evento 1: Alerta de vencimiento (HU11)
    alertas.emitir_alerta(
        tipo="VENCIMIENTO", 
        remitente="Sistema", 
        destinatario=estudiante1.email_institucional, 
        mensaje="La fecha límite para el Parcial 2 de PA-302 es mañana."
    )
    
    # 8. PERSISTENCIA (HU13, HU14)
    persistencia_service = PersistenciaService()
    print("\n--- 8. PERSISTENCIA (.dat Legajo) ---")
    
    # Guardar legajo (HU13)
    persistencia_service.guardar_legajo_estudiante(estudiante1.legajo)
    
    # Recuperar legajo (HU14)
    legajo_recuperado = persistencia_service.recuperar_legajo_estudiante(estudiante1.legajo)
    print(f"Datos recuperados (Legajo {legajo_recuperado['legajo']}): Historial -> {legajo_recuperado['historial_academico']}")

    print("\n=====================================================================")
    print("           EJEMPLO SIGEU COMPLETADO EXITOSAMENTE                      ")
    print("=====================================================================")

if __name__ == "__main__":
    # Limpiar directorio de datos para un demo limpio
    if os.path.exists("data"):
        for file in os.listdir("data"):
            os.remove(os.path.join("data", file))
        os.rmdir("data")
    
    inicializar_y_ejecutar()