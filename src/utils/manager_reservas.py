import os
import json

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, '..\\data\\reserva.json')


class ManagerReservas:
    def __init__(self):
        self.reservas = []
        self.cargar_reservas()

    def cargar_reservas(self):
        try:                
            with open(ruta_archivo, 'r') as file:
                datos = json.load(file)
                self.reservas = datos
            return self.reservas
        except (FileNotFoundError, json.JSONDecodeError):
            print("El archivo no existe o está vacío. Se creará uno nuevo.")
            self.reservas = []

    def nuevo_registro(self, diccionario_reserva):
        self.reservas.append(diccionario_reserva)

    def guardar_reservas(self):
        with open(ruta_archivo, 'w', encoding="utf-8") as file:
            json.dump(self.reservas, file, indent=4)

    def __str__(self):
        for reserva in self.reservas:
            print(f"{"id_reserva"}: {reserva["id_reserva"]}, {"id_cliente"}: {reserva["id_cliente"]}, {"id_habitacion"}: {reserva["id_habitacion"]}, {"fecha_inicio"}: {reserva["fecha_inicio"]}, {"dias_reserva"}: {reserva["dias_reserva"]}, {"fecha_fin"}: {reserva["fecha_fin"]}")

