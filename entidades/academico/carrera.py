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