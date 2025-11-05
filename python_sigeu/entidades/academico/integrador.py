"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/entidades/academico
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/7: carrera.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/carrera.py
# ================================================================================

# entidades/academico/carrera.py
from typing import List

class Carrera:
    """Entidad Carrera (Cumple HU2)."""
    
    def __init__(self, nombre: str, codigo: str, duracion_anios: int):
        self.nombre = nombre
        self.codigo = codigo
        self.duracion_anios = duracion_anios
        self.materias_codigos: List[str] = []
        # Correlativas: {codigo_materia: [materias_precedentes]}
        self.correlativas: Dict[str, List[str]] = {} 

    def agregar_materia(self, codigo_materia: str) -> None:
        if codigo_materia not in self.materias_codigos:
            self.materias_codigos.append(codigo_materia)

    def establecer_correlativa(self, materia_actual: str, materia_precedente: str) -> None:
        if materia_actual not in self.correlativas:
            self.correlativas[materia_actual] = []
        if materia_precedente not in self.correlativas[materia_actual]:
            self.correlativas[materia_actual].append(materia_precedente)

    def get_correlativas(self, materia_codigo: str) -> List[str]:
        return self.correlativas.get(materia_codigo, [])

    def __str__(self):
        return f"Carrera: {self.nombre} ({self.codigo})"

# ================================================================================
# ARCHIVO 3/7: curso.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/curso.py
# ================================================================================

from abc import ABC, abstractmethod

class Curso(ABC):
    """Clase base (Interfaz) para todos los tipos de cursos (Presencial, Virtual, Híbrido)."""
    
    def __init__(self, nombre: str, capacidad: int, codigo: str):
        self._nombre = nombre
        self._capacidad = capacidad
        self._codigo = codigo
        self._estudiantes_inscritos = []

    def get_codigo(self) -> str:
        return self._codigo

    def get_nombre(self) -> str:
        return self._nombre
    
    @abstractmethod
    def get_modalidad(self) -> str:
        """Define la modalidad (requerido por Factory)."""
        pass

# ================================================================================
# ARCHIVO 4/7: facultad.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/facultad.py
# ================================================================================

# entidades/academico/facultad.py
from typing import List

class Facultad:
    """Entidad principal para la estructura universitaria (Cumple HU1)."""
    
    def __init__(self, nombre: str, codigo: str, direccion: str):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.carreras_codigos: List[str] = [] # Se almacena el código de carrera

    def asociar_carrera(self, codigo_carrera: str) -> None:
        if codigo_carrera not in self.carreras_codigos:
            self.carreras_codigos.append(codigo_carrera)
            print(f"Carrera {codigo_carrera} asociada a {self.nombre}.")

    def __str__(self):
        return f"Facultad: {self.nombre} ({self.codigo})"

# ================================================================================
# ARCHIVO 5/7: materia.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia.py
# ================================================================================

# entidades/academico/materia.py (Clase Base)
from abc import ABC, abstractmethod
from typing import Optional

class Materia(ABC):
    """Clase base (interfaz) para Materia universitaria (parte del Factory)."""
    def __init__(self, nombre: str, codigo: str, carga_horaria: int, carrera_codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.carrera_codigo = carrera_codigo
        self.docente_dni: Optional[int] = None

    @abstractmethod
    def get_tipo(self) -> str:
        pass
    
    def asignar_docente(self, docente_dni: int) -> None:
        self.docente_dni = docente_dni
        
    def __str__(self):
        return f"Materia: {self.nombre} ({self.codigo}) - Tipo: {self.get_tipo()}"


# ================================================================================
# ARCHIVO 6/7: materia_practica.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia_practica.py
# ================================================================================

# entidades/academico/materia_practica.py
from entidades.academico.materia import Materia

class MateriaPractica(Materia):
    def get_tipo(self) -> str:
        return "Práctica/Laboratorio"

# ================================================================================
# ARCHIVO 7/7: materia_teorica.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia_teorica.py
# ================================================================================

# entidades/academico/materia_teorica.py
from entidades.academico.materia import Materia

class MateriaTeorica(Materia):
    def get_tipo(self) -> str:
        return "Teórica"

