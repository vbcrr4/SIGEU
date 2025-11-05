"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/patrones/observer
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/observer/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/patrones/observer/observer.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T') # Tipo genérico para el evento

class Observer(Generic[T], ABC):
    """
    OBSERVER Pattern: Interfaz para los componentes que desean recibir notificaciones.
    """

    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """Método llamado por el Observable para notificar un cambio."""
        pass

