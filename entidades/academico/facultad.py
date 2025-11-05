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