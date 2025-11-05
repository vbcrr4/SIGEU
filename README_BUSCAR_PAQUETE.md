# buscar_paquete.py - Documentación de Validación de Arquitectura (SIGEU)

## 1. Descripción General

**buscar_paquete.py** es un script de utilidad diseñado específicamente para **validar la estructura de la Arquitectura por Capas** del proyecto **SIGEU (Sistema Integral de Gestión Educativa Universitaria)**.

Su propósito principal es automatizar la verificación de que los directorios principales del proyecto (`entidades`, `servicios`, `patrones`) son **Paquetes de Python válidos** (es decir, contienen un archivo `__init__.py`), lo cual es un requisito crucial para el cumplimiento de la rúbrica de evaluación técnica.

---

## 2. Requisitos del Sistema

* **Python**: Versión 3.x.
* **Estructura del Proyecto**: Debe ejecutarse desde el directorio raíz del proyecto **SIGEU** (donde se encuentran las carpetas `entidades`, `servicios`, etc.).

---

## 3. Modo de Operación

El script opera en un único modo de **Búsqueda y Validación de Paquetes Clave**.

### Flujo de Verificación:

1.  Identifica el directorio de ejecución como la raíz del proyecto.
2.  Busca los directorios definidos como las capas principales: **`entidades`**, **`servicios`**, y **`patrones`**.
3.  Verifica la existencia del archivo **`__init__.py`** dentro de cada uno de ellos.
4.  Si el archivo existe, lo marca como `[+] Paquete encontrado`.
5.  Si el archivo falta, genera una alerta `[!] Directorio encontrado pero NO es un paquete Python (falta __init__.py)`.
6.  Al finalizar, lista el contenido de cada paquete para una revisión visual de la estructura.

---

## 4. Sintaxis y Comandos

Para ejecutar la validación, simplemente navegue a la raíz del proyecto y ejecute:

```bash
python3 buscar_paquete.py