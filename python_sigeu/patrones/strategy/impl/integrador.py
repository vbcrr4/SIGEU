"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: promedio_ponderado.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/promedio_ponderado.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: promedio_simple.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/promedio_simple.py
# ================================================================================

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

