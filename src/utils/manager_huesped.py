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
    
    def agregar_id(self): # Asigna un nuevo ID al huésped
        if self.huespedes:
            max_id = max(huesped["id_huesped"] for huesped in self.huespedes)
            return max_id + 1
        else:
            return 1
        
    def confirmar_id(self, id_huesped): # Verifica si el ID del huésped ya existe
        for huesped in self.huespedes:
            if huesped["id_huesped"] == id_huesped:
                return True
        return False

    def nuevo_registro(self, diccionario_huesped):
        self.huespedes.append(diccionario_huesped)



    def guardar_huespedes(self):
        with open(ruta_archivo, 'w', encoding="utf-8") as file:
            json.dump(self.huespedes, file, indent=4)

    def __str__(self):
        for huesped in self.huespedes:
            print(f"{"id"}: {huesped["id_huesped"]}, {"nombre"}: {huesped["nombre"]}, {"correo"}: {huesped["correo"]}, {"telefono"}: {huesped["telefono"]}")
                
        