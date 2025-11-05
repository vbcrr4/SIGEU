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
