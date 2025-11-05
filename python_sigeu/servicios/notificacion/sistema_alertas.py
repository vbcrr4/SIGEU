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