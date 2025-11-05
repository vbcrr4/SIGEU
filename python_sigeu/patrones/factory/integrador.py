"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/patrones/factory
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: materia_factory.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/factory/materia_factory.py
# ================================================================================

# patrones/factory/materia_factory.py
from typing import Dict, Callable
from entidades.academico.materia import Materia
from entidades.academico.materia_teorica import MateriaTeorica
from entidades.academico.materia_practica import MateriaPractica

class MateriaFactory:
    """
    FACTORY METHOD Pattern: Crea instancias de Materia (Teórica, Práctica, Laboratorio) 
    sin exponer la lógica de instanciación al código cliente.
    (Cumple HU3 y rúbrica)
    """

    @staticmethod
    def crear_materia(
        tipo: str,
        nombre: str,
        codigo: str,
        carga_horaria: int,
        carrera_codigo: str
    ) -> Materia:
        """
        Crea un objeto Materia basado en el tipo especificado.
        
        Args:
            tipo: El tipo de materia a crear ("Teorica", "Practica", "Laboratorio").
            nombre: Nombre de la materia.
            codigo: Código único de la materia.
            carga_horaria: Carga horaria semanal.
            carrera_codigo: Código de la carrera a la que pertenece.
        
        Returns:
            Una instancia de la clase Materia concreta.
        
        Raises:
            ValueError: Si el tipo de materia es desconocido.
        """
        
        # Uso de diccionario para evitar if/elif/else (mejora la extensibilidad)
        factories: Dict[str, Callable[[], Materia]] = {
            "Teorica": lambda: MateriaTeorica(nombre, codigo, carga_horaria, carrera_codigo),
            "Practica": lambda: MateriaPractica(nombre, codigo, carga_horaria, carrera_codigo),
            "Laboratorio": lambda: MateriaPractica(nombre, codigo, carga_horaria, carrera_codigo), # Misma clase por simplicidad
        }

        if tipo not in factories:
            raise ValueError(f"[FACTORY ERROR] Tipo de materia desconocido: {tipo}")

        # Ejecuta la función lambda para crear la instancia
        return factories[tipo]()

