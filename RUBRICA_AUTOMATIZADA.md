# Rubrica de Evaluacion Automatizada - Sistema Integral de Gestión Educativa Universitaria

**Proyecto**: SIGEU - Gestión Educativa Universitaria
**Version**: 1.0.0
**Fecha**: Noviembre 2025
**Proposito**: Automatizacion de correccion de proyectos en n8n

---

## Seccion 1: Verificaciones Estaticas (Analisis de Codigo)

### 1.1 Patron SINGLETON

#### SING-001: Atributo de Instancia Unica
```json
{
  "id": "SING-001",
  "categoria": "Singleton",
  "descripcion": "Verificar atributo _instance en clase RegistroServicios",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn '_instance = None' --include='registro_servicios.py' .",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
#### SING-003: Thread-Safety con Lock
{
  "id": "SING-003",
  "categoria": "Singleton",
  "descripcion": "Verificar uso de threading.Lock en Singleton",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'threading.Lock\\|with self._lock' --include='registro_servicios.py' .",
  "puntaje": 3,
  "threshold": 2,
  "peso": "alto"
}
### 1.2 Patron FACTORY METHOD
#### FACT-002: Clase Factory Existe
{
  "id": "FACT-002",
  "categoria": "Factory",
  "descripcion": "Verificar existencia de MateriaFactory",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -name 'materia_factory.py' -type f",
  "puntaje": 2,
  "threshold": 1,
  "peso": "critico"
}
#### FACT-003: Metodo crear_materia Implementado
{
  "id": "FACT-003",
  "categoria": "Factory",
  "descripcion": "Verificar metodos de creacion de Materia",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def crear_materia' --include='materia_factory.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
### 1.3 Patron OBSERVER
#### OBSR-004: Metodo notificar_observadores
{
  "id": "OBSR-004",
  "categoria": "Observer",
  "descripcion": "Verificar metodo de notificacion en SistemaAlertas",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'def notificar_observadores' --include='*sistema_alertas.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
### 1.4 Patron STRATEGY
#### STRT-001: Interfaz PromedioStrategy Abstracta
{
  "id": "STRT-001",
  "categoria": "Strategy",
  "descripcion": "Verificar interfaz PromedioStrategy abstracta",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'class.*PromedioStrategy.*ABC' --include='*.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "critico"
}
#### STRT-003: Inyeccion de Estrategia
{
  "id": "STRT-003",
  "categoria": "Strategy",
  "descripcion": "Verificar inyeccion de Strategy en EvaluacionService",
  "tipo": "estatica",
  "metodo": "grep",
  "comando": "grep -rn 'self._estrategia' --include='evaluacion_service.py' .",
  "puntaje": 3,
  "threshold": 1,
  "peso": "alto"
}
### 1.6 Estructura del Proyecto
#### STRC-001: Paquete entidades/academico
{
  "id": "STRC-001",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete entidades/academico existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'academico'",
  "puntaje": 2,
  "threshold": 1,
  "peso": "alto"
}
#### STRC-002: Paquete servicios/academico
{
  "id": "STRC-002",
  "categoria": "Estructura",
  "descripcion": "Verificar paquete servicios/academico existe",
  "tipo": "estatica",
  "metodo": "glob",
  "comando": "find . -type d -name 'academico'",
  "puntaje": 2,
  "threshold": 2,
  "peso": "alto"
}
## Seccion 2: Verificaciones Dinamicas (Ejecucion)
### 2.2 Patrones en Accion
#### EXEC-007: Patron Strategy Demostrado
{
  "id": "EXEC-007",
  "categoria": "Ejecucion",
  "descripcion": "Verificar uso y nombre de Strategy en output",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i '\\[STRATEGY\\] Promedio'",
  "puntaje": 3,
  "threshold": 1,
  "peso": "medio"
}
### 2.3 Funcionalidad
#### EXEC-008: Inscripción con Correlativas Funcional (HU4, HU9)
{
  "id": "EXEC-008",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar mensaje de inscripcion exitosa",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'inscrito(a)'",
  "puntaje": 4,
  "threshold": 1,
  "peso": "alto"
}
#### EXEC-009: Evaluación y Promedio Funcional (HU7)
{
  "id": "EXEC-009",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar cálculo y mensaje de promedio final",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'Promedio final'",
  "puntaje": 4,
  "threshold": 2,
  "peso": "alto"
}
#### EXEC-010: Persistencia de Legajo Funcional (HU13, HU14)
{
  "id": "EXEC-010",
  "categoria": "Funcionalidad",
  "descripcion": "Verificar recuperación de datos de legajo",
  "tipo": "dinamica",
  "metodo": "python_output",
  "comando": "timeout 30 python main.py 2>&1 | grep -i 'Legajo.*recuperado'",
  "puntaje": 4,
  "threshold": 1,
  "peso": "alto"
}

