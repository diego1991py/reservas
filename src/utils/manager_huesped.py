import os
import json

ruta_script = os.path.dirname(__file__)
ruta_archivo = os.path.join(ruta_script, '..\\data\\huesped.json')


class ManagerHuesped:
    def __init__(self):
        self.huespedes = []
        self.cargar_huespedes()

    def cargar_huespedes(self):
            try:                
                with open(ruta_archivo, 'r') as file:
                    datos = json.load(file)
                    self.huespedes = datos
                return self.huespedes
            except (FileNotFoundError, json.JSONDecodeError):
                print("El archivo no existe o está vacío. Se creará uno nuevo.")
                self.huespedes = []
    

    def nuevo_registro(self, diccionario_huesped):
        self.huespedes.append(diccionario_huesped)
        #print(f"Se ha registrado el huesped: {diccionario_huesped}")
       # print(self.huespedes)


    def guardar_huespedes(self):
        with open(ruta_archivo, 'w', encoding="utf-8") as file:
            json.dump(self.huespedes, file, indent=4)