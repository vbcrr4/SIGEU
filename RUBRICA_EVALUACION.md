# Rubrica de Evaluacion Tecnica - Sistema Integral de Gestión Educativa Universitaria

**Proyecto**: SIGEU - Gestión Educativa Universitaria
**Version**: 1.0.0
**Fecha**: Noviembre 2025
**Tipo de Evaluacion**: Tecnica Academica / Profesional

---

## Instrucciones de Uso

[... Escala de Puntuacion y Puntaje Total se mantienen sin cambios ...]

---

## Seccion 1: Patrones de Diseno (80 puntos)

### 1.1 Patron SINGLETON (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Clase implementa Singleton con instancia unica | `__new__` con control de instancia unica |
| **Thread-safety** | 5 | Implementacion thread-safe con Lock | Uso de `threading.Lock` en `RegistroServicios` |
| **Acceso consistente** | 3 | Metodo `get_instance()` disponible | Metodo de clase que retorna instancia |
| **Inicializacion perezosa** | 3 | Lazy initialization correcta | Instancia se crea solo cuando se solicita |
| **Uso apropiado en el sistema** | 4 | Singleton usado donde corresponde (Registry) | **RegistroServicios** es Singleton |

**Puntaje Seccion 1.1**: _____ / 20

---

### 1.2 Patron FACTORY METHOD (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Factory encapsula creacion de objetos | Metodo estatico `crear_materia(...)` |
| **Desacoplamiento** | 5 | Cliente no conoce clases concretas | Retorna tipo base `Materia`, no tipos concretos |
| **Extensibilidad** | 4 | Facil agregar nuevos tipos | Diccionario de factories (NO if/elif cascades) |
| **Validacion de entrada** | 3 | Valida parametros y lanza excepciones | Lanza `ValueError` si tipo de materia desconocido |
| **Uso apropiado en el sistema** | 3 | Factory usado en la creacion de Materias | **MateriaFactory** crea `MateriaTeorica`/`MateriaPractica` |

**Puntaje Seccion 1.2**: _____ / 20

---

### 1.3 Patron OBSERVER (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Observable y Observer implementados | Clases `Observable[T]` y `Observer[T]` |
| **Generics para tipo-seguridad** | 5 | Uso de TypeVar y Generic[T] | `Observable[EventoAlerta]` |
| **Notificaciones automaticas** | 4 | Observadores notificados al cambiar estado | `notificar_observadores()` llamado al emitir una alerta |
| **Desacoplamiento** | 3 | Observable no conoce detalles de Observer | Lista generica de observadores |
| **Uso apropiado en el sistema** | 3 | Observable usado para Alertas | **SistemaAlertas** como Observable para eventos. (HU11) |

**Puntaje Seccion 1.3**: _____ / 20

---

### 1.4 Patron STRATEGY (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Implementacion correcta del patron** | 5 | Interfaz Strategy con implementaciones | **PromedioStrategy** (abstracta) |
| **Algoritmos intercambiables** | 5 | Multiples estrategias implementadas | `PromedioSimpleStrategy`, `PromedioPonderadoStrategy` |
| **Inyeccion de dependencias** | 4 | Estrategia inyectada via constructor | **EvaluacionService** recibe strategy en `__init__` |
| **Delegacion correcta** | 3 | Servicios delegan calculo a estrategia | `calcular_promedio_final()` llama al metodo de Strategy |
| **Uso apropiado en el sistema** | 3 | Estrategias usadas segun tipo de promedio | Usado en el módulo de **Evaluaciones/Calificaciones**. (HU7) |

**Puntaje Seccion 1.4**: _____ / 20

---

**PUNTAJE TOTAL SECCION 1**: _____ / 80

---

## Seccion 2: Arquitectura y Diseno (60 puntos)

### 2.1 Separacion de Responsabilidades (20 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Entidades vs Servicios** | 5 | Entidades solo datos, servicios solo logica | Clases en `entidades/` vs `servicios/` |
| **Service Layer Pattern** | 5 | Capa de servicios bien definida | Servicios (`InscripcionService`, `EvaluacionService`) contienen toda la logica de negocio. |
| **Principio SRP** | 4 | Cada clase una unica responsabilidad | Una clase = un concepto de dominio (e.g., `Estudiante`, `Carrera`). |
| **Cohesion alta** | 3 | Elementos relacionados agrupados | Modulos tematicos (`academico/`, `usuario/`, `patrones/`) |
| **Acoplamiento bajo** | 3 | Dependencias minimizadas | Uso de interfaces, inyeccion de Strategy. |

**Puntaje Seccion 2.1**: _____ / 20

---

### 2.4 Organizacion del Codigo (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Estructura de paquetes** | 3 | Organizacion logica de modulos | Paquetes: **entidades**, **servicios**, **patrones**. |
| **Modulos tematicos** | 3 | Agrupacion por dominio | `entidades/academico`, `entidades/usuario`, `servicios/academico` |
| **Archivos `__init__.py`** | 2 | Inicializacion de paquetes | Todos los paquetes con `__init__.py` |
| **Importaciones limpias** | 2 | Sin imports circulares | Uso de TYPE_CHECKING para forward references |

**Puntaje Seccion 2.4**: _____ / 10

---

## Seccion 4: Funcionalidad del Sistema (40 puntos)

### 4.1 Gestión de la Estructura Académica (10 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Creación de Facultad** | 3 | Se registra la Facultad principal | `Facultad` creada y registrada. (HU1) |
| **Registro de Carrera** | 3 | Se registra la Carrera con sus atributos | `Carrera` creada y vinculada a `Facultad`. (HU2) |
| **Alta de Materias** | 4 | Factory crea y registra al menos 2 tipos de Materia | `MateriaFactory` crea tipos distintos (`Teórica`, `Práctica`). (HU3) |

**Puntaje Seccion 4.1**: _____ / 10

---

### 4.2 Gestión de Inscripciones y Correlativas (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Validacion de Correlativas** | 4 | El sistema valida la aprobación de correlativas | `InscripcionService` verifica historial académico antes de inscribir. (HU4) |
| **Inscripción funcional** | 4 | El estudiante se inscribe a la materia | `inscribir_estudiante_a_materia()` actualiza `Estudiante.inscripciones_actuales`. (HU9) |
| **Alta de Estudiante** | 4 | Se registra al estudiante con su legajo | `Estudiante` creado y registrado. (HU8) |

**Puntaje Seccion 4.2**: _____ / 12

---

### 4.3 Gestión de Evaluaciones y Promedios (12 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Registro de Calificaciones** | 4 | El sistema registra notas por tipo/peso | `EvaluacionService.registrar_evaluacion()` guarda notas. (HU7) |
| **Cálculo de Promedio** | 4 | El servicio calcula el promedio usando la Strategy | `calcular_promedio_final()` usa `PromedioSimple` o `PromedioPonderado`. (HU7) |
| **Consulta de Notas** | 4 | El estudiante puede consultar su historial de notas | `get_evaluaciones()` expone las notas registradas. (HU10) |

**Puntaje Seccion 4.3**: _____ / 12

---

### 4.4 Persistencia de Legajo y Notificaciones (6 puntos)

| Criterio | Puntos | Descripcion | Evidencia Requerida |
|----------|--------|-------------|---------------------|
| **Guardado de Legajo** | 3 | El sistema persiste el legajo académico completo | `PersistenciaService.guardar_legajo_estudiante()` crea archivo **`.dat`**. (HU13) |
| **Recuperación de Legajo** | 3 | El sistema lee y deserializa el archivo `DAT` | `PersistenciaService.recuperar_legajo_estudiante()` funciona. (HU14) |

**Puntaje Seccion 4.4**: _____ / 6

---

**PUNTAJE TOTAL SECCION 4**: _____ / 40

---
[... Las Secciones 3 y 5 (Calidad, Buenas Prácticas) se mantienen genéricas ...]

---

## Anexo: Mapeo de Historias de Usuario a Criterios (SIGEU)

| Epic | Historias de Usuario | Seccion de Rubrica |
|------|----------------------|--------------------|
| **Académico** | HU1, HU2, HU3, HU5 | 4.1, 4.2 |
| **Inscripción** | HU4, HU9 | 4.2 |
| **Evaluación** | HU7, HU10 | 4.3 |
| **Usuarios** | HU8 | 4.2 |
| **Notificación** | HU11 | 1.3 (Observer) |
| **Persistencia** | HU13, HU14 | 4.4 |
| **Patrones** | US-TECH-001 al 004 | 1.1 al 1.4 |