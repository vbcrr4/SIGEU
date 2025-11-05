"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/servicios
Fecha: 2025-11-05 18:24:02
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/3: persistencia_service.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/persistencia_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: registro_servicios.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/registro_servicios.py
# ================================================================================

# servicios/registro_servicios.py
import threading
from typing import Dict, Any, List
# Importar entidades necesarias para el registro

class RegistroServicios:
    """
    SINGLETON Pattern: Registro de servicios y fuente de verdad global (Service Registry).
    Asegura una única instancia thread-safe, central para la gestión universitaria.
    """
    _instance: 'RegistroServicios' = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> 'RegistroServicios':
        """Implementación thread-safe del Singleton."""
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    # Inicialización interna: Contenedores para entidades de dominio (PLURALES CORRECTOS)
                    cls._instance._facultades: Dict[str, Any] = {}
                    cls._instance._carreras: Dict[str, Any] = {}
                    cls._instance._materias: Dict[str, Any] = {}
                    cls._instance._estudiantes: Dict[int, Any] = {}
                    cls._instance._docentes: Dict[int, Any] = {}
                    
                    # MAPEO DE CLAVE SINGULAR A ATRIBUTO PLURAL
                    cls._instance._mapeo_registro = {
                        'facultad': cls._instance._facultades,
                        'carrera': cls._instance._carreras,
                        'materia': cls._instance._materias,
                        'estudiante': cls._instance._estudiantes,
                        'docente': cls._instance._docentes,
                    }
        return cls._instance

    @staticmethod
    def get_instance() -> 'RegistroServicios':
        """Método estático para acceder a la única instancia."""
        return RegistroServicios()

    # --- Métodos de Gestión Básica (Solo ejemplo) ---

    def registrar_entidad(self, entidad: Any, tipo: str, clave: Any) -> None:
        """Método genérico para registrar cualquier entidad usando mapeo explícito."""
        
        tipo_lower = tipo.lower()
        
        if tipo_lower not in self._mapeo_registro:
             raise ValueError(f"Tipo de entidad desconocido: {tipo}")
             
        # Usamos el mapeo para obtener el registro correcto
        registro = self._mapeo_registro[tipo_lower] 
        
        if clave in registro:
            raise ValueError(f"El {tipo} con clave {clave} ya existe.")
            
        registro[clave] = entidad
        print(f"[SINGLETON] {tipo} con clave {clave} registrado exitosamente.")

    def obtener_entidad(self, tipo: str, clave: Any) -> Any:
        """Método genérico para obtener cualquier entidad."""
        return getattr(self, f"_{tipo.lower()}s").get(clave)

    def obtener_todo(self, tipo: str) -> List[Any]:
        """Retorna todas las entidades de un tipo dado."""
        return list(getattr(self, f"_{tipo.lower()}s").values())

# Nota: Este Singleton se inyecta en los Servicios de Negocio.

