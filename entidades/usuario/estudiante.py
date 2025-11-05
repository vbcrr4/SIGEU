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