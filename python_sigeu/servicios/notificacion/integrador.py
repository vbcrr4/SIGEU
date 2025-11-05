"""
Archivo integrador generado automaticamente
Directorio: /home/debian-user/SIGEU/python_sigeu/servicios/notificacion
Fecha: 2025-11-05 18:47:21
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/notificacion/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: sistema_alertas.py
# Ruta: /home/debian-user/SIGEU/python_sigeu/servicios/notificacion/sistema_alertas.py
# ================================================================================

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

