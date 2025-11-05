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