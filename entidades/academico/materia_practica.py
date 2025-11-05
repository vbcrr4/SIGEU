# entidades/academico/materia_practica.py
from entidades.academico.materia import Materia

class MateriaPractica(Materia):
    def get_tipo(self) -> str:
        return "Práctica/Laboratorio"