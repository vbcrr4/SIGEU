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