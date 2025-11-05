# patrones/strategy/impl/promedio_simple.py
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import List, Dict, Any

class PromedioSimpleStrategy(PromedioStrategy):
    """Implementa el cálculo del promedio simple (igual peso para todas las notas)."""

    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        if not evaluaciones:
            return 0.0
        
        total_notas = sum(e['nota'] for e in evaluaciones)
        return total_notas / len(evaluaciones)

    def get_nombre(self) -> str:
        return "Promedio Simple"