"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/entidades/usuario
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: docente.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/docente.py
# ================================================================================

# entidades/usuario/docente.py
from typing import List

class Docente:
    """Entidad Docente (Cumple HU5)."""
    
    def __init__(self, dni: int, nombre: str, titulo: str, fecha_alta: str):
        self.dni = dni
        self.nombre = nombre
        self.titulo = titulo # Título profesional habilitante (HU5)
        self.fecha_alta = fecha_alta
        self.materias_dictadas: List[str] = []
        self.disponibilidad_horaria: List[str] = ["Lunes 10-12", "Martes 14-16"] # Ejemplo

    def get_id(self) -> int:
        return self.dni
        
    def agregar_materia_dictada(self, codigo_materia: str) -> None:
        if codigo_materia not in self.materias_dictadas:
            self.materias_dictadas.append(codigo_materia)
            
    def tiene_titulo_habilitante(self) -> bool:
        # Lógica de validación de título simple
        return len(self.titulo) > 5

    def __str__(self):
        return f"Docente: {self.nombre} ({self.titulo})"

# ================================================================================
# ARCHIVO 3/3: estudiante.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/estudiante.py
# ================================================================================

# entidades/usuario/estudiante.py
from typing import List, Dict, Any

class Estudiante:
    """Entidad Estudiante (Cumple HU8)."""
    
    def __init__(self, dni: int, nombre: str, legajo: str, email_institucional: str, carrera_codigo: str):
        self.dni = dni
        self.nombre = nombre
        self.legajo = legajo # Código único generado automáticamente (HU8)
        self.email_institucional = email_institucional
        self.carrera_codigo = carrera_codigo
        # {codigo_materia: 'APROBADA'/'CURSANDO'/'DESAPROBADA'}
        self.historial_academico: Dict[str, str] = {} 
        self.inscripciones_actuales: List[str] = [] # Códigos de materia
        
    def get_id(self) -> int:
        return self.dni
    
    def inscribir_materia(self, codigo_materia: str) -> None:
        if codigo_materia not in self.inscripciones_actuales:
            self.inscripciones_actuales.append(codigo_materia)
            self.historial_academico[codigo_materia] = 'CURSANDO'

    def materia_aprobada(self, codigo_materia: str) -> bool:
        return self.historial_academico.get(codigo_materia) == 'APROBADA'

    # Contiene toda la información requerida por HU13 (Legajo)
    def to_legajo_data(self) -> Dict[str, Any]:
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'legajo': self.legajo,
            'carrera_codigo': self.carrera_codigo,
            'historial_academico': self.historial_academico,
        }

    def __str__(self):
        return f"Estudiante: {self.nombre} (Legajo: {self.legajo})"

