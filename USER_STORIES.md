---

## 4. Historias de Usuario por Módulo

---

### 4.1 Gestión Académica (Materias y Carreras)

#### **HU1. Creación de Facultad**
**Como** administrativo  
**Quiero** registrar la estructura de la Facultad de Ingeniería  
**Para** gestionar sus carreras, materias y aulas asociadas.  

**Criterios de aceptación:**
- Se deben definir nombre, dirección y código institucional.  
- Se deben poder asociar múltiples carreras.  
- Cada carrera debe tener al menos una materia.  

---

#### **HU2. Registro de Carreras**
**Como** administrativo  
**Quiero** registrar carreras universitarias dentro de la facultad  
**Para** estructurar las materias, correlativas y plan de estudios.  

**Criterios de aceptación:**
- Cada carrera tiene código, nombre y duración en años.  
- Puede registrar correlatividades entre materias.  
- Se valida que no haya duplicados de código.  

---

#### **HU3. Alta de Materias**
**Como** docente o administrativo  
**Quiero** crear materias nuevas dentro de una carrera  
**Para** asignar docentes, horarios y alumnos.  

**Criterios de aceptación:**
- Se definen nombre, código, carga horaria y tipo (teórica, práctica, laboratorio).  
- Se permite asignar un aula y un docente responsable.  
- Las materias deben estar vinculadas a una carrera existente.  

---

#### **HU4. Validación de Correlativas**
**Como** sistema  
**Quiero** validar automáticamente las correlativas de materias  
**Para** impedir inscripciones inválidas.  

**Criterios de aceptación:**
- Antes de la inscripción, el sistema verifica correlativas aprobadas.  
- En caso de incumplimiento, muestra mensaje detallado con materias pendientes.  

---

### 4.2 Gestión Docente

#### **HU5. Alta de Docentes**
**Como** administrativo  
**Quiero** registrar docentes con sus datos personales y académicos  
**Para** asignarlos a materias y mantener sus antecedentes.  

**Criterios de aceptación:**
- Debe incluir DNI, nombre, título profesional y fecha de alta.  
- Se valida que el docente tenga título habilitante.  
- Se almacena el historial de materias dictadas.  

---

#### **HU6. Asignación de Materias**
**Como** administrativo  
**Quiero** asignar docentes a materias y cursos  
**Para** asegurar la cobertura académica.  

**Criterios de aceptación:**
- Solo docentes con disponibilidad pueden ser asignados.  
- Se valida que un docente no tenga superposición de horarios.  

---

#### **HU7. Registro de Evaluaciones**
**Como** docente  
**Quiero** registrar notas y evaluaciones de los alumnos  
**Para** mantener actualizado su rendimiento académico.  

**Criterios de aceptación:**
- Permite registrar parciales, finales y recuperatorios.  
- Los datos se asocian automáticamente al legajo del alumno.  

---

### 4.3 Gestión Estudiantil

#### **HU8. Alta de Estudiantes**
**Como** administrativo  
**Quiero** registrar alumnos con sus datos personales  
**Para** permitir su inscripción en carreras y materias.  

**Criterios de aceptación:**
- Requiere DNI, nombre, fecha de nacimiento y correo institucional.  
- Se genera automáticamente un legajo único por estudiante.  

---

#### **HU9. Inscripción a Materias**
**Como** estudiante  
**Quiero** inscribirme a materias disponibles según mi carrera  
**Para** cursarlas durante el cuatrimestre actual.  

**Criterios de aceptación:**
- El sistema verifica correlativas y cupos antes de confirmar.  
- El estudiante recibe comprobante de inscripción.  

---

#### **HU10. Consulta de Calificaciones**
**Como** estudiante  
**Quiero** consultar mis notas y asistencias por materia  
**Para** hacer seguimiento de mi progreso.  

**Criterios de aceptación:**
- Se muestran todas las evaluaciones y promedios.  
- Se puede exportar en formato PDF o CSV.  

---

### 4.4 Sistema de Notificaciones Automatizadas

#### **HU11. Envío de Alertas Automáticas**
**Como** sistema  
**Quiero** enviar notificaciones automáticas sobre faltas y vencimientos  
**Para** mantener informados a alumnos y docentes.  

**Criterios de aceptación:**
- Se envían alertas por inasistencias mayores al 30%.  
- Se notifican vencimientos de exámenes y fechas de inscripción.  
- Notificaciones mediante correo institucional o CLI.  

---

#### **HU12. Seguimiento de Desempeño**
**Como** docente  
**Quiero** recibir informes automáticos de desempeño estudiantil  
**Para** identificar alumnos en riesgo académico.  

**Criterios de aceptación:**
- Se generan reportes semanales de promedios y asistencia.  
- Se permite configurar umbrales personalizados.  

---

### 4.5 Persistencia y Legajos Académicos

#### **HU13. Guardado de Legajos**
**Como** sistema  
**Quiero** guardar los legajos completos de alumnos y docentes  
**Para** asegurar la trazabilidad académica.  

**Criterios de aceptación:**
- Se guarda en formato binario (.dat) en la carpeta `data/`.  
- Se incluye información personal, materias cursadas y calificaciones.  

---

#### **HU14. Recuperación de Legajos**
**Como** auditor académico  
**Quiero** recuperar legajos almacenados  
**Para** verificar la integridad de la información.  

**Criterios de aceptación:**
- Permite búsqueda por DNI o nombre.  
- Valida que el archivo no esté dañado.  

---

### 4.6 Reportes y Certificados

#### **HU15. Generación de Reportes Académicos**
**Como** administrativo  
**Quiero** generar reportes de notas y asistencia por materia o carrera  
**Para** presentarlos ante el consejo académico.  

**Criterios de aceptación:**
- Exporta reportes en formato PDF.  
- Se incluyen estadísticas de aprobación y rendimiento.  

---

#### **HU16. Emisión de Certificados**
**Como** administrativo  
**Quiero** emitir certificados de cursado y regularidad  
**Para** proveer documentación oficial a los estudiantes.  

**Criterios de aceptación:**
- Se genera documento firmado digitalmente.  
- Incluye código de verificación único.  

---

## 5. Criterios de Aceptación Generales

- Todas las operaciones deben registrar fecha, hora y usuario.  
- Los datos se validan antes de persistir.  
- Cada módulo debe ser testeado de forma independiente.  
- Debe existir control de excepciones y logs centralizados.  
- El sistema debe cumplir con los principios SOLID y patrones de diseño definidos.  

---

## 6. Notas Técnicas y Patrones de Diseño Aplicados

| Patrón | Aplicación en SIGEU | Descripción |
|--------|----------------------|--------------|
| **Singleton** | `ServiceRegistry` | Garantiza una única instancia global de registro de servicios académicos. |
| **Factory Method** | `MateriaFactory` | Crea materias (teóricas, prácticas, laboratorio) sin conocer clases concretas. |
| **Observer** | `SistemaDeAlertas` | Notifica automáticamente a docentes y alumnos ante eventos. |
| **Strategy** | `CálculoDePromedioStrategy` | Diferentes estrategias de evaluación (ponderado, simple, por créditos). |
| **Registry Pattern** | `CarreraServiceRegistry` | Registro central de servicios por tipo de entidad (Alumno, Docente, Materia). |

---

## ✅ Resultado Esperado

El **SIGEU** debe permitir ejecutar un flujo completo de gestión universitaria, donde:
- Se creen carreras y materias.
- Se registren docentes y alumnos.
- Se gestionen inscripciones y evaluaciones.
- Se envíen notificaciones automáticas.
- Se persistan y consulten legajos académicos.
- Se generen reportes y certificados.

---

**Facultad de Ingeniería – Universidad de Mendoza**  
**Sistema Integral de Gestión Educativa Universitaria (SIGEU)**  
**Versión:** 1.0.0  
**Fecha:** Noviembre 2025  