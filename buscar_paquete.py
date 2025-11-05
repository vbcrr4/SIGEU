"""
Script para verificar la estructura del proyecto SIGEU (Sistema Integral de Gestión Educativa Universitaria).
Busca directorios clave (entidades, servicios, patrones) y valida que sean paquetes Python (contienen __init__.py).
"""
import os
import sys
from datetime import datetime

# --- CONFIGURACIÓN ESPECÍFICA DEL PROYECTO SIGEU ---
# Se define una lista de directorios/paquetes clave a verificar en la raíz del proyecto.
PAQUETES_CLAVE_SIGEU = ['entidades', 'servicios', 'patrones']
# El nombre del directorio raíz del proyecto para la búsqueda de paquetes principales.
NOMBRE_PROYECTO_RAIZ = os.path.basename(os.getcwd()) # Asume el directorio actual es la raíz SIGEU
# ----------------------------------------------------

def buscar_paquete_clave(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python (directorio con __init__.py) en un directorio específico.

    Args:
        directorio_raiz: Directorio donde iniciar la búsqueda.
        nombre_paquete: Nombre del paquete a buscar.

    Returns:
        Lista de rutas donde se encontró el paquete.
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Solo buscamos paquetes clave en el primer nivel de subdirectorios
        if raiz == directorio_raiz:
            for nombre_dir in directorios:
                if nombre_dir == nombre_paquete:
                    ruta_paquete = os.path.join(raiz, nombre_dir)
                    # Verificar que sea un paquete Python (contiene __init__.py)
                    if '__init__.py' in os.listdir(ruta_paquete):
                        paquetes_encontrados.append(ruta_paquete)
                        print(f"[+] Paquete encontrado: {ruta_paquete}")
                    else:
                        print(f"[!] Directorio encontrado pero NO es un paquete Python (falta __init__.py): {ruta_paquete}")
            # Detener el walk después del primer nivel (el raíz)
            break
            
    return paquetes_encontrados

def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            if item.endswith('.py') and os.path.isfile(os.path.join(directorio, item)):
                archivos_python.append(os.path.join(directorio, item))
    except PermissionError:
        print(f"      [!] Sin permisos para leer el directorio {directorio}")
    return archivos_python


def mostrar_estructura_paquete(ruta_paquete: str):
    """Muestra el contenido básico de un paquete y subpaquetes."""
    print(f"    Contenido de {os.path.basename(ruta_paquete)}:")
    try:
        # Explorar el contenido para mostrar una vista jerárquica
        for item in sorted(os.listdir(ruta_paquete)):
            ruta_item = os.path.join(ruta_paquete, item)
            
            # Excluir directorios privados y de caché
            if item in ['__pycache__', '.git', '.vscode']:
                continue
                
            if os.path.isdir(ruta_item):
                if '__init__.py' in os.listdir(ruta_item):
                    print(f"      [DIR-PKG] {item}/")
                else:
                    print(f"      [DIR]   {item}/")
            elif os.path.isfile(ruta_item):
                if item.endswith('.py'):
                    print(f"      [FILE-PY] {item}")
                else:
                    print(f"      [FILE]    {item}")
    except PermissionError:
        print(f"      [!] Sin permisos para leer el directorio")


def main():
    directorio_raiz = os.getcwd()
    
    print("=" * 60)
    print(f"  VERIFICADOR DE ESTRUCTURA DEL PROYECTO {NOMBRE_PROYECTO_RAIZ} (SIGEU)")
    print("=" * 60)
    print(f"[INFO] Buscando desde la raíz del proyecto: {directorio_raiz}")
    print(f"[INFO] Verificando paquetes clave: {', '.join(PAQUETES_CLAVE_SIGEU)}")
    print("\n" + "-" * 60)

    paquetes_totales = []
    paquetes_faltantes = []
    
    for paquete_nombre in PAQUETES_CLAVE_SIGEU:
        encontrados = buscar_paquete_clave(directorio_raiz, paquete_nombre)
        if encontrados:
            paquetes_totales.extend(encontrados)
        else:
            paquetes_faltantes.append(paquete_nombre)

    print("\n" + "=" * 60)
    if paquetes_faltantes:
        print(f"[FAIL] Faltan paquetes clave ({len(paquetes_faltantes)}): {', '.join(paquetes_faltantes)}")
        print("[FAIL] La estructura no cumple con la Arquitectura por Capas.")
        return 1
    else:
        print(f"[OK] Se encontraron {len(paquetes_totales)} paquetes clave y subpaquetes.")
        for ruta in paquetes_totales:
             mostrar_estructura_paquete(ruta)

    print("\n" + "-" * 60)
    print("[INFO] Buscando archivos Python sueltos en la raíz...")
    archivos_raiz = [f for f in os.listdir(directorio_raiz) if f.endswith('.py') and os.path.isfile(f)]
    for archivo in archivos_raiz:
        print(f"  [FILE-PY] {archivo}")
    
    print("\n[OK] Verificación de estructura finalizada.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'help':
        print("\nUso: python buscar_paquete.py")
        print("Verifica si los directorios 'entidades', 'servicios' y 'patrones' existen y son paquetes Python válidos.")
        sys.exit(0)
        
    sys.exit(main())