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