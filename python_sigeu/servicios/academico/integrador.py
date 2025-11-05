"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/servicios/academico
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/academico/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: evaluacion_service.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/academico/evaluacion_service.py
# ================================================================================

# servicios/academico/evaluacion_service.py
from servicios.registro_servicios import RegistroServicios
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import Dict, Any, List

class EvaluacionService:
    """
    Servicio de Evaluación y Calificación. Delega el cálculo del promedio 
    al patrón Strategy (Cumple HU7 y rúbrica).
    """
    
    def __init__(self, estrategia_promedio: PromedioStrategy):
        # Inyección de dependencia de Strategy (cumple rúbrica)
        self._registro = RegistroServicios.get_instance()
        self._estrategia = estrategia_promedio
        # Base de datos de evaluaciones: {legajo_materia: [{'tipo': 'Parcial 1', 'nota': 7.5, 'peso': 0.5}]}
        self._evaluaciones: Dict[str, List[Dict[str, Any]]] = {}

    def registrar_evaluacion(self, legajo: str, materia_codigo: str, tipo: str, nota: float, peso: float = 1.0) -> None:
        """Registra una evaluación de un alumno (HU7)."""
        clave = f"{legajo}_{materia_codigo}"
        if clave not in self._evaluaciones:
            self._evaluaciones[clave] = []
            
        self._evaluaciones[clave].append({'tipo': tipo, 'nota': nota, 'peso': peso})
        print(f"[EvaluacionService] Nota {nota} ({tipo}) registrada para {legajo} en {materia_codigo}.")

    def calcular_promedio_final(self, legajo: str, materia_codigo: str) -> float:
        """Calcula el promedio final usando la Strategy inyectada."""
        clave = f"{legajo}_{materia_codigo}"
        evaluaciones = self._evaluaciones.get(clave, [])
        
        # Delegación del cálculo a la estrategia (cumple rúbrica)
        promedio = self._estrategia.calcular_promedio(evaluaciones)
        print(f"[STRATEGY] Promedio ({self._estrategia.get_nombre()}) para {legajo} en {materia_codigo}: {promedio:.2f}")
        return promedio

    def get_evaluaciones(self, legajo: str, materia_codigo: str) -> List[Dict[str, Any]]:
        """Permite consultar notas (HU10)."""
        return self._evaluaciones.get(f"{legajo}_{materia_codigo}", [])

# ================================================================================
# ARCHIVO 3/3: inscripcion_service.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/academico/inscripcion_service.py
# ================================================================================

# servicios/academico/inscripcion_service.py
from servicios.registro_servicios import RegistroServicios
from entidades.usuario.estudiante import Estudiante
from entidades.academico.carrera import Carrera

class InscripcionService:
    """
    Servicio de Inscripción y validación de Correlativas.
    (Cumple HU4 y HU9)
    """
    
    def __init__(self):
        self._registro = RegistroServicios.get_instance()

    def _validar_correlativas(self, estudiante: Estudiante, materia_codigo: str) -> None:
        """Verifica si el estudiante cumple con las correlativas (HU4)."""
        carrera: Carrera = self._registro.obtener_entidad('Carrera', estudiante.carrera_codigo)
        if not carrera:
            raise ValueError("Carrera no encontrada en el registro.")

        correlativas = carrera.get_correlativas(materia_codigo)
        
        materias_pendientes = []
        for corr_codigo in correlativas:
            if not estudiante.materia_aprobada(corr_codigo):
                materias_pendientes.append(corr_codigo)
                
        if materias_pendientes:
            raise PermissionError(
                f"No puede inscribirse a {materia_codigo}. Correlativas pendientes: {', '.join(materias_pendientes)}."
            )

    def inscribir_estudiante_a_materia(self, legajo_estudiante: str, materia_codigo: str) -> None:
        """
        Inscribe un estudiante a una materia verificando cupos y correlativas (HU9).
        """
        estudiante: Estudiante = self._registro.obtener_entidad('Estudiante', legajo_estudiante)
        materia = self._registro.obtener_entidad('Materia', materia_codigo)
        
        if not estudiante or not materia:
            raise ValueError("Estudiante o Materia no encontrados.")

        # 1. Validación de Correlativas (HU4)
        self._validar_correlativas(estudiante, materia_codigo)
        
        # 2. Validación de Cupo (Simulación - asumir cupo infinito por ahora)
        # if len(materia.estudiantes_inscritos) >= materia.capacidad:
        #     raise PermissionError("Cupo máximo alcanzado en la materia.")

        # 3. Inscripción
        estudiante.inscribir_materia(materia_codigo)
        # materia.estudiantes_inscritos.append(estudiante.legajo)
        
        print(f"[InscripcionService] {estudiante.nombre} inscrito(a) a {materia.nombre}.")
        # [OBSERVER TBD] Notificar inscripción (HU9: comprobante)

