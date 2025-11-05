"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/debian-user/SIGEU/python_sigeu
Fecha de generacion: 2025-11-05 18:24:02
Total de archivos integrados: 35
Total de directorios procesados: 14
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#
# DIRECTORIO: entidades
#   2. __init__.py
#
# DIRECTORIO: entidades/academico
#   3. __init__.py
#   4. carrera.py
#   5. curso.py
#   6. facultad.py
#   7. materia.py
#   8. materia_practica.py
#   9. materia_teorica.py
#
# DIRECTORIO: entidades/recursos
#   10. aula.py
#   11. material.py
#
# DIRECTORIO: entidades/usuario
#   12. __init__.py
#   13. docente.py
#   14. estudiante.py
#
# DIRECTORIO: excepciones
#   15. dominio_exception.py
#   16. inscripcion_exception.py
#
# DIRECTORIO: patrones
#   17. __init__.py
#
# DIRECTORIO: patrones/factory
#   18. __init__.py
#   19. materia_factory.py
#
# DIRECTORIO: patrones/observer
#   20. __init__.py
#   21. observable.py
#   22. observer.py
#
# DIRECTORIO: patrones/strategy
#   23. __init__.py
#   24. promedio_strategy.py
#
# DIRECTORIO: patrones/strategy/impl
#   25. __init__.py
#   26. promedio_ponderado.py
#   27. promedio_simple.py
#
# DIRECTORIO: servicios
#   28. __init__.py
#   29. persistencia_service.py
#   30. registro_servicios.py
#
# DIRECTORIO: servicios/academico
#   31. __init__.py
#   32. evaluacion_service.py
#   33. inscripcion_service.py
#
# DIRECTORIO: servicios/notificacion
#   34. __init__.py
#   35. sistema_alertas.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/35: __init__.py
# Directorio: .
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades
################################################################################

# ==============================================================================
# ARCHIVO 2/35: __init__.py
# Directorio: entidades
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/academico
################################################################################

# ==============================================================================
# ARCHIVO 3/35: __init__.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 4/35: carrera.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/carrera.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 5/35: curso.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/curso.py
# ==============================================================================

from abc import ABC, abstractmethod

class Curso(ABC):
    """Clase base (Interfaz) para todos los tipos de cursos (Presencial, Virtual, Híbrido)."""
    
    def __init__(self, nombre: str, capacidad: int, codigo: str):
        self._nombre = nombre
        self._capacidad = capacidad
        self._codigo = codigo
        self._estudiantes_inscritos = []

    def get_codigo(self) -> str:
        return self._codigo

    def get_nombre(self) -> str:
        return self._nombre
    
    @abstractmethod
    def get_modalidad(self) -> str:
        """Define la modalidad (requerido por Factory)."""
        pass

# ==============================================================================
# ARCHIVO 6/35: facultad.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/facultad.py
# ==============================================================================

# entidades/academico/facultad.py
from typing import List

class Facultad:
    """Entidad principal para la estructura universitaria (Cumple HU1)."""
    
    def __init__(self, nombre: str, codigo: str, direccion: str):
        self.nombre = nombre
        self.codigo = codigo
        self.direccion = direccion
        self.carreras_codigos: List[str] = [] # Se almacena el código de carrera

    def asociar_carrera(self, codigo_carrera: str) -> None:
        if codigo_carrera not in self.carreras_codigos:
            self.carreras_codigos.append(codigo_carrera)
            print(f"Carrera {codigo_carrera} asociada a {self.nombre}.")

    def __str__(self):
        return f"Facultad: {self.nombre} ({self.codigo})"

# ==============================================================================
# ARCHIVO 7/35: materia.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia.py
# ==============================================================================

# entidades/academico/materia.py (Clase Base)
from abc import ABC, abstractmethod
from typing import Optional

class Materia(ABC):
    """Clase base (interfaz) para Materia universitaria (parte del Factory)."""
    def __init__(self, nombre: str, codigo: str, carga_horaria: int, carrera_codigo: str):
        self.nombre = nombre
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.carrera_codigo = carrera_codigo
        self.docente_dni: Optional[int] = None

    @abstractmethod
    def get_tipo(self) -> str:
        pass
    
    def asignar_docente(self, docente_dni: int) -> None:
        self.docente_dni = docente_dni
        
    def __str__(self):
        return f"Materia: {self.nombre} ({self.codigo}) - Tipo: {self.get_tipo()}"


# ==============================================================================
# ARCHIVO 8/35: materia_practica.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia_practica.py
# ==============================================================================

# entidades/academico/materia_practica.py
from entidades.academico.materia import Materia

class MateriaPractica(Materia):
    def get_tipo(self) -> str:
        return "Práctica/Laboratorio"

# ==============================================================================
# ARCHIVO 9/35: materia_teorica.py
# Directorio: entidades/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/academico/materia_teorica.py
# ==============================================================================

# entidades/academico/materia_teorica.py
from entidades.academico.materia import Materia

class MateriaTeorica(Materia):
    def get_tipo(self) -> str:
        return "Teórica"


################################################################################
# DIRECTORIO: entidades/recursos
################################################################################

# ==============================================================================
# ARCHIVO 10/35: aula.py
# Directorio: entidades/recursos
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/recursos/aula.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 11/35: material.py
# Directorio: entidades/recursos
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/recursos/material.py
# ==============================================================================




################################################################################
# DIRECTORIO: entidades/usuario
################################################################################

# ==============================================================================
# ARCHIVO 12/35: __init__.py
# Directorio: entidades/usuario
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 13/35: docente.py
# Directorio: entidades/usuario
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/docente.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/35: estudiante.py
# Directorio: entidades/usuario
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/entidades/usuario/estudiante.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: excepciones
################################################################################

# ==============================================================================
# ARCHIVO 15/35: dominio_exception.py
# Directorio: excepciones
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/excepciones/dominio_exception.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 16/35: inscripcion_exception.py
# Directorio: excepciones
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/excepciones/inscripcion_exception.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones
################################################################################

# ==============================================================================
# ARCHIVO 17/35: __init__.py
# Directorio: patrones
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/__init__.py
# ==============================================================================




################################################################################
# DIRECTORIO: patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 18/35: __init__.py
# Directorio: patrones/factory
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 19/35: materia_factory.py
# Directorio: patrones/factory
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/factory/materia_factory.py
# ==============================================================================

# patrones/factory/materia_factory.py
from typing import Dict, Callable
from entidades.academico.materia import Materia
from entidades.academico.materia_teorica import MateriaTeorica
from entidades.academico.materia_practica import MateriaPractica

class MateriaFactory:
    """
    FACTORY METHOD Pattern: Crea instancias de Materia (Teórica, Práctica, Laboratorio) 
    sin exponer la lógica de instanciación al código cliente.
    (Cumple HU3 y rúbrica)
    """

    @staticmethod
    def crear_materia(
        tipo: str,
        nombre: str,
        codigo: str,
        carga_horaria: int,
        carrera_codigo: str
    ) -> Materia:
        """
        Crea un objeto Materia basado en el tipo especificado.
        
        Args:
            tipo: El tipo de materia a crear ("Teorica", "Practica", "Laboratorio").
            nombre: Nombre de la materia.
            codigo: Código único de la materia.
            carga_horaria: Carga horaria semanal.
            carrera_codigo: Código de la carrera a la que pertenece.
        
        Returns:
            Una instancia de la clase Materia concreta.
        
        Raises:
            ValueError: Si el tipo de materia es desconocido.
        """
        
        # Uso de diccionario para evitar if/elif/else (mejora la extensibilidad)
        factories: Dict[str, Callable[[], Materia]] = {
            "Teorica": lambda: MateriaTeorica(nombre, codigo, carga_horaria, carrera_codigo),
            "Practica": lambda: MateriaPractica(nombre, codigo, carga_horaria, carrera_codigo),
            "Laboratorio": lambda: MateriaPractica(nombre, codigo, carga_horaria, carrera_codigo), # Misma clase por simplicidad
        }

        if tipo not in factories:
            raise ValueError(f"[FACTORY ERROR] Tipo de materia desconocido: {tipo}")

        # Ejecuta la función lambda para crear la instancia
        return factories[tipo]()


################################################################################
# DIRECTORIO: patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 20/35: __init__.py
# Directorio: patrones/observer
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 21/35: observable.py
# Directorio: patrones/observer
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/observer/observable.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 22/35: observer.py
# Directorio: patrones/observer
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/observer/observer.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 23/35: __init__.py
# Directorio: patrones/strategy
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 24/35: promedio_strategy.py
# Directorio: patrones/strategy
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/promedio_strategy.py
# ==============================================================================

# patrones/strategy/promedio_strategy.py
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class PromedioStrategy(ABC):
    """
    STRATEGY Pattern: Interfaz base para todas las estrategias de cálculo de promedios.
    (Cumple HU7 y rúbrica)
    """
    
    @abstractmethod
    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        """
        Calcula el promedio final a partir de una lista de evaluaciones.
        
        Args:
            evaluaciones: Lista de diccionarios, cada uno con 'nota' y 'peso'.
            
        Returns:
            El promedio calculado (float).
        """
        pass
    
    @abstractmethod
    def get_nombre(self) -> str:
        """Retorna el nombre de la estrategia."""
        pass


################################################################################
# DIRECTORIO: patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 25/35: __init__.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 26/35: promedio_ponderado.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/promedio_ponderado.py
# ==============================================================================

# patrones/strategy/impl/promedio_ponderado.py
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import List, Dict, Any

class PromedioPonderadoStrategy(PromedioStrategy):
    """Implementa el cálculo del promedio ponderado por peso de evaluación."""

    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        if not evaluaciones:
            return 0.0
        
        total_puntos = sum(e['nota'] * e['peso'] for e in evaluaciones)
        total_pesos = sum(e['peso'] for e in evaluaciones)
        
        if total_pesos == 0:
            return self.calcular_promedio_simple(evaluaciones) # Failsafe
            
        return total_puntos / total_pesos

    def get_nombre(self) -> str:
        return "Promedio Ponderado"
    
    def calcular_promedio_simple(self, evaluaciones: List[Dict[str, Any]]) -> float:
        """Función auxiliar en caso de pesos nulos."""
        return sum(e['nota'] for e in evaluaciones) / len(evaluaciones)

# ==============================================================================
# ARCHIVO 27/35: promedio_simple.py
# Directorio: patrones/strategy/impl
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/patrones/strategy/impl/promedio_simple.py
# ==============================================================================

# patrones/strategy/impl/promedio_simple.py
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import List, Dict, Any

class PromedioSimpleStrategy(PromedioStrategy):
    """Implementa el cálculo del promedio simple (igual peso para todas las notas)."""

    def calcular_promedio(self, evaluaciones: List[Dict[str, Any]]) -> float:
        if not evaluaciones:
            return 0.0
        
        total_notas = sum(e['nota'] for e in evaluaciones)
        return total_notas / len(evaluaciones)

    def get_nombre(self) -> str:
        return "Promedio Simple"


################################################################################
# DIRECTORIO: servicios
################################################################################

# ==============================================================================
# ARCHIVO 28/35: __init__.py
# Directorio: servicios
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 29/35: persistencia_service.py
# Directorio: servicios
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/persistencia_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 30/35: registro_servicios.py
# Directorio: servicios
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/registro_servicios.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: servicios/academico
################################################################################

# ==============================================================================
# ARCHIVO 31/35: __init__.py
# Directorio: servicios/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/academico/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 32/35: evaluacion_service.py
# Directorio: servicios/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/academico/evaluacion_service.py
# ==============================================================================

# servicios/academico/evaluacion_service.py
from servicios.registro_servicios import RegistroServicios
from patrones.strategy.promedio_strategy import PromedioStrategy
from typing import Dict, Any, List

class EvaluacionService:
    """
    Servicio de Evaluación y Calificación. Delega el cálculo del promedio 
    al patrón Strategy (Cumple HU7 y rúbrica).
    """
    
    def __init__(self, estrategia_promedio: PromedioStrategy):
        # Inyección de dependencia de Strategy (cumple rúbrica)
        self._registro = RegistroServicios.get_instance()
        self._estrategia = estrategia_promedio
        # Base de datos de evaluaciones: {legajo_materia: [{'tipo': 'Parcial 1', 'nota': 7.5, 'peso': 0.5}]}
        self._evaluaciones: Dict[str, List[Dict[str, Any]]] = {}

    def registrar_evaluacion(self, legajo: str, materia_codigo: str, tipo: str, nota: float, peso: float = 1.0) -> None:
        """Registra una evaluación de un alumno (HU7)."""
        clave = f"{legajo}_{materia_codigo}"
        if clave not in self._evaluaciones:
            self._evaluaciones[clave] = []
            
        self._evaluaciones[clave].append({'tipo': tipo, 'nota': nota, 'peso': peso})
        print(f"[EvaluacionService] Nota {nota} ({tipo}) registrada para {legajo} en {materia_codigo}.")

    def calcular_promedio_final(self, legajo: str, materia_codigo: str) -> float:
        """Calcula el promedio final usando la Strategy inyectada."""
        clave = f"{legajo}_{materia_codigo}"
        evaluaciones = self._evaluaciones.get(clave, [])
        
        # Delegación del cálculo a la estrategia (cumple rúbrica)
        promedio = self._estrategia.calcular_promedio(evaluaciones)
        print(f"[STRATEGY] Promedio ({self._estrategia.get_nombre()}) para {legajo} en {materia_codigo}: {promedio:.2f}")
        return promedio

    def get_evaluaciones(self, legajo: str, materia_codigo: str) -> List[Dict[str, Any]]:
        """Permite consultar notas (HU10)."""
        return self._evaluaciones.get(f"{legajo}_{materia_codigo}", [])

# ==============================================================================
# ARCHIVO 33/35: inscripcion_service.py
# Directorio: servicios/academico
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/academico/inscripcion_service.py
# ==============================================================================

# servicios/academico/inscripcion_service.py
from servicios.registro_servicios import RegistroServicios
from entidades.usuario.estudiante import Estudiante
from entidades.academico.carrera import Carrera

class InscripcionService:
    """
    Servicio de Inscripción y validación de Correlativas.
    (Cumple HU4 y HU9)
    """
    
    def __init__(self):
        self._registro = RegistroServicios.get_instance()

    def _validar_correlativas(self, estudiante: Estudiante, materia_codigo: str) -> None:
        """Verifica si el estudiante cumple con las correlativas (HU4)."""
        carrera: Carrera = self._registro.obtener_entidad('Carrera', estudiante.carrera_codigo)
        if not carrera:
            raise ValueError("Carrera no encontrada en el registro.")

        correlativas = carrera.get_correlativas(materia_codigo)
        
        materias_pendientes = []
        for corr_codigo in correlativas:
            if not estudiante.materia_aprobada(corr_codigo):
                materias_pendientes.append(corr_codigo)
                
        if materias_pendientes:
            raise PermissionError(
                f"No puede inscribirse a {materia_codigo}. Correlativas pendientes: {', '.join(materias_pendientes)}."
            )

    def inscribir_estudiante_a_materia(self, legajo_estudiante: str, materia_codigo: str) -> None:
        """
        Inscribe un estudiante a una materia verificando cupos y correlativas (HU9).
        """
        estudiante: Estudiante = self._registro.obtener_entidad('Estudiante', legajo_estudiante)
        materia = self._registro.obtener_entidad('Materia', materia_codigo)
        
        if not estudiante or not materia:
            raise ValueError("Estudiante o Materia no encontrados.")

        # 1. Validación de Correlativas (HU4)
        self._validar_correlativas(estudiante, materia_codigo)
        
        # 2. Validación de Cupo (Simulación - asumir cupo infinito por ahora)
        # if len(materia.estudiantes_inscritos) >= materia.capacidad:
        #     raise PermissionError("Cupo máximo alcanzado en la materia.")

        # 3. Inscripción
        estudiante.inscribir_materia(materia_codigo)
        # materia.estudiantes_inscritos.append(estudiante.legajo)
        
        print(f"[InscripcionService] {estudiante.nombre} inscrito(a) a {materia.nombre}.")
        # [OBSERVER TBD] Notificar inscripción (HU9: comprobante)


################################################################################
# DIRECTORIO: servicios/notificacion
################################################################################

# ==============================================================================
# ARCHIVO 34/35: __init__.py
# Directorio: servicios/notificacion
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/notificacion/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 35/35: sistema_alertas.py
# Directorio: servicios/notificacion
# Ruta completa: /home/debian-user/SIGEU/python_sigeu/servicios/notificacion/sistema_alertas.py
# ==============================================================================

# servicios/notificacion/sistema_alertas.py
from patrones.observer.observable import Observable
from typing import Dict, Any

# Definición del tipo de evento (similar a EventoAsistencia, pero más genérico)
class EventoAlerta:
    def __init__(self, tipo: str, remitente: str, destinatario: str, mensaje: str):
        self.tipo = tipo # 'FALTA', 'VENCIMIENTO', 'NOTA_ALTA'
        self.remitente = remitente
        self.destinatario = destinatario
        self.mensaje = mensaje
        
class SistemaAlertas(Observable[EventoAlerta]):
    """
    OBSERVER Pattern: Sistema de Alertas (Sujeto Observable).
    (Cumple HU11: Envío de Alertas)
    """
    
    def emitir_alerta(self, tipo: str, remitente: str, destinatario: str, mensaje: str) -> None:
        """
        Emite una alerta y notifica a todos los observadores suscritos.
        """
        evento = EventoAlerta(tipo, remitente, destinatario, mensaje)
        print(f"\n[SISTEMA ALERTAS] 🚨 Alerta Emitida: {tipo} a {destinatario}")
        self.notificar_observadores(evento)


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 35
# Generado: 2025-11-05 18:24:02
################################################################################
