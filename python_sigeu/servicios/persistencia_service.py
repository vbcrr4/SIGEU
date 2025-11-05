# servicios/persistencia_service.py
import pickle
import os
from typing import Dict, Any
from servicios.registro_servicios import RegistroServicios
from entidades.usuario.estudiante import Estudiante

class PersistenciaService:
    """
    Servicio para el guardado y recuperación de legajos (Cumple HU13 y HU14).
    """
    
    DATA_DIR = "data"
    
    def __init__(self):
        self._registro = RegistroServicios.get_instance()
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
        
    def guardar_legajo_estudiante(self, legajo: str) -> None:
        """Guarda el legajo completo de un estudiante en un archivo .dat (HU13)."""
        estudiante: Estudiante = self._registro.obtener_entidad('Estudiante', legajo)
        if not estudiante:
            raise ValueError(f"Estudiante con legajo {legajo} no encontrado.")
            
        filename = os.path.join(self.DATA_DIR, f"legajo_{legajo}.dat")
        legajo_data = estudiante.to_legajo_data()
        
        try:
            with open(filename, 'wb') as f:
                pickle.dump(legajo_data, f)
            print(f"[PERSISTENCIA] Legajo {legajo} guardado correctamente en {filename}.")
        except Exception as e:
            print(f"[ERROR PERSISTENCIA] No se pudo guardar el legajo: {e}")

    def recuperar_legajo_estudiante(self, legajo: str) -> Dict[str, Any]:
        """Recupera la información de un legajo guardado (HU14)."""
        filename = os.path.join(self.DATA_DIR, f"legajo_{legajo}.dat")
        
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Archivo de legajo {legajo} no encontrado.")
            
        try:
            with open(filename, 'rb') as f:
                data = pickle.load(f)
            print(f"[PERSISTENCIA] Legajo {legajo} recuperado.")
            return data
        except Exception as e:
            raise IOError(f"Error al leer el archivo de legajo: {e}")