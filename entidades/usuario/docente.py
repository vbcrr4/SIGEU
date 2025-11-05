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