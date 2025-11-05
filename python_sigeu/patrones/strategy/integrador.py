"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/patrones/strategy
Fecha: 2025-11-05 18:47:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: promedio_strategy.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/promedio_strategy.py
# ================================================================================

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

