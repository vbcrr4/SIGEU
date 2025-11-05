# entidades/academico/materia_teorica.py
from entidades.academico.materia import Materia

class MateriaTeorica(Materia):
    def get_tipo(self) -> str:
        return "Teórica"