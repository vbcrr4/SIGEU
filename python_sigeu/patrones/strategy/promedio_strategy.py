# patrones/strategy/promedio_strategy.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PromedioStrategy(ABC):
    """
    STRATEGY Pattern: Interfaz base para todas las estrategias de cálculo de promedios.
    (Cumple HU7 y rúbrica)
    """
    
    @abstractmethod
    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        """
        Calcula el promedio final a partir de una lista de evaluaciones.
        
        Args:
            evaluaciones: Lista de diccionarios, cada uno con 'nota' y 'peso'.
            
        Returns:
            El promedio calculado (float).
        """
        pass
    
    @abstractmethod
    def get_nombre(self) -> str:
        """Retorna el nombre de la estrategia."""
        pass