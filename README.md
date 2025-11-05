# Sistema Integral de Gestión Educativa Universitaria (SIGEU)

[![Python Version](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
[![Patrones de Diseño](https://img.shields.io/badge/Patrones-4%20Implementados-brightgreen.svg)](USER_STORIES.md)

Sistema integral de gestión para instituciones de educación superior, enfocado en la administración de facultades, carreras, planes de estudio, inscripciones y evaluaciones académicas. Este proyecto está diseñado con un fuerte énfasis en la **Arquitectura por Capas** y la aplicación de **Patrones de Diseño** para garantizar su mantenibilidad, extensibilidad y cumplimiento de los principios SOLID.

---

## Tabla de Contenidos

- [Contexto del Dominio](#contexto-del-dominio)
- [Características Principales](#características-principales)
- [Arquitectura del Sistema](#arquitectura-del-sistema)
- [Patrones de Diseño Implementados](#patrones-de-diseño-implementados)
- [Requisitos del Sistema](#requisitos-del-sistema)
- [Instalación y Uso](#instalación-y-uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Documentación Técnica](#documentación-técnica)
- [Licencia](#licencia)

---

## Contexto del Dominio

### Problema que Resuelve

El **SIGEU** aborda los desafíos de la administración académica en universidades. Se centra en proveer una solución robusta y modular para manejar procesos críticos como la validación de **correlativas** (HU4), el registro detallado de **evaluaciones** (HU7) y la gestión de la **estructura académica** completa (Facultades, Carreras, Materias). El uso de patrones garantiza que el sistema pueda evolucionar fácilmente a medida que cambian los reglamentos universitarios.

## Características Principales

1.  **Estructura Académica:** Registro de Facultades (HU1), Carreras (HU2) y Materias por tipo (Teórica, Práctica/Laboratorio) (HU3).
2.  **Validación de Inscripción:** Control estricto de **correlatividades** antes de permitir la inscripción de un estudiante (HU4, HU9).
3.  **Evaluación Flexible:** Soporte para múltiples métodos de cálculo de promedio (Simple vs. Ponderado) gracias al patrón **Strategy** (HU7).
4.  **Notificaciones Automatizadas:** Sistema de alertas para notificar vencimientos y eventos clave (HU11), implementado con el patrón **Observer**.
5.  **Persistencia Segura:** Capacidad de guardar y recuperar el **Legajo Académico** completo de un estudiante en formato binario (`.dat`) para auditoría y consulta (HU13, HU14).

---

## Arquitectura del Sistema

El SIGEU está diseñado siguiendo un modelo de **Arquitectura por Capas**, lo que promueve la separación de responsabilidades:

| Capa | Paquetes Principales | Responsabilidad |
| :--- | :--- | :--- |
| **Dominio (Modelo)** | `entidades/` | Contiene los modelos de datos (`Estudiante`, `Carrera`, `Materia`) y reglas de negocio puras. |
| **Servicios (Negocio)** | `servicios/` | Aloja la lógica de negocio (`InscripcionService`, `EvaluacionService`). Orquesta las entidades y patrones. |
| **Patrones** | `patrones/` | Implementación desacoplada de los patrones de diseño (*Strategy*, *Factory*, *Observer*). |
| **Registro** | `registro_servicios.py` | Implementa el patrón **Singleton** como fuente de verdad y registro de servicios. |

---

## Patrones de Diseño Implementados

Este proyecto implementa cuatro patrones de diseño fundamentales, cumpliendo con los requerimientos técnicos del proyecto:

| Patrón | Archivo Clave | Propósito en SIGEU |
| :--- | :--- | :--- |
| **Singleton** | `servicios/registro_servicios.py` | Fuente única y centralizada para acceder a todas las entidades y servicios del sistema (Service Registry). |
| **Factory Method** | `patrones/factory/materia_factory.py` | Creación polimórfica de diferentes tipos de materias (`Teórica`, `Práctica`), ocultando la lógica de instanciación. |
| **Strategy** | `patrones/strategy/promedio_strategy.py` | Intercambia el algoritmo de cálculo de promedio (Simple o Ponderado) en tiempo de ejecución para diferentes planes de estudio. |
| **Observer** | `servicios/notificacion/sistema_alertas.py` | Permite que el sistema de alertas notifique a múltiples componentes (`AuditoriaLog`, `NotificadorEstudiante`) sin conocer sus detalles internos (HU11). |

---

## Requisitos del Sistema

* **Python**: Versión 3.10 o superior.
* **Librerías**: No se requieren librerías externas complejas. Solo módulos estándar de Python (`os`, `pickle`, `threading`, `abc`).

---

## Instalación y Uso

### Instalación

Clonar el repositorio y navegar al directorio principal:

```bash
git clone [URL_DEL_REPOSITORIO]
cd SIGEU