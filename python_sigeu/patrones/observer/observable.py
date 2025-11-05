# patrones/observer/observable.py
from typing import List, Generic, TypeVar
from patrones.observer.observer import Observer

T = TypeVar('T') # Tipo genérico para el evento

class Observable(Generic[T]):
    """
    OBSERVER Pattern: Clase base para los componentes que generan eventos.
    (Sujeto en el patrón Observer).
    """

    def __init__(self):
        # La lista de observadores debe ser genérica para manejar cualquier tipo de evento (T)
        self._observadores: List[Observer[T]] = []

    def agregar_observador(self, observador: Observer[T]) -> None:
        """Suscribe un observador a los eventos."""
        if observador not in self._observadores:
            self._observadores.append(observador)
            print(f"[OBSERVER] Nuevo observador suscrito: {type(observador).__name__}")

    def eliminar_observador(self, observador: Observer[T]) -> None:
        """Desuscribe un observador."""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores con el evento."""
        print(f"[OBSERVER] Notificando evento: {type(evento).__name__}")
        for observador in self._observadores:
            observador.actualizar(evento)