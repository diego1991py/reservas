from datetime import datetime, timedelta


class Reservas:
    def __init__(self, id_reserva = int, id_cliente = int, id_habitacion = int, fecha_inicio = datetime, dias_reserva = int):
        self.id_reserva = id_reserva
        self.id_cliente = id_cliente
        self.id_habitacion = id_habitacion
        self.fecha_inicio = fecha_inicio
        self.dias_reserva = dias_reserva
        self.fecha_fin = self.fecha_inicio + timedelta(days=self.dias_reserva)

    def __str__(self):
        return f"Reserva {self.id_reserva}: Cliente {self.id_cliente}, Habitación {self.id_habitacion}, Fecha de inicio {self.fecha_inicio.strftime('%Y-%m-%d')}, Días de reserva {self.dias_reserva}, Fecha de fin {self.fecha_fin.strftime('%Y-%m-%d')}"
    
    def __to_dict__(self):
        return {
            'id_reserva': self.id_reserva,
            'id_cliente': self.id_cliente,
            'id_habitacion': self.id_habitacion,
            'fecha_inicio': self.fecha_inicio.strftime('%Y-%m-%d'),
            'dias_reserva': self.dias_reserva,
            'fecha_fin': self.fecha_fin.strftime('%Y-%m-%d'),
        }