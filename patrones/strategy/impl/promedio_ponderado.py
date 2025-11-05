# patrones/strategy/impl/promedio_ponderado.py
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import List, Dict, Any

class PromedioPonderadoStrategy(PromedioStrategy):
    """Implementa el cálculo del promedio ponderado por peso de evaluación."""

    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        if not evaluaciones:
            return 0.0
        
        total_puntos = sum(e['nota'] * e['peso'] for e in evaluaciones)
        total_pesos = sum(e['peso'] for e in evaluaciones)
        
        if total_pesos == 0:
            return self.calcular_promedio_simple(evaluaciones) # Failsafe
            
        return total_puntos / total_pesos

    def get_nombre(self) -> str:
        return "Promedio Ponderado"
    
    def calcular_promedio_simple(self, evaluaciones: List[Dict[str, Any]]) -> float:
        """Función auxiliar en caso de pesos nulos."""
        return sum(e['nota'] for e in evaluaciones) / len(evaluaciones)