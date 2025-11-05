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