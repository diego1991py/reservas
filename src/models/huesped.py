import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from models.persona import Persona


class Huesped(Persona):
    def __init__(self, id_huesped, nombre, correo, telefono, ):
        super().__init__(nombre, correo, telefono)
        self.id_huesped = id_huesped

    def __str__(self):
        return f'Huesped: ID Huesped: {self.id_huesped}, {self.nombre}, Correo: {self.correo}, Telefono: {self.telefono}'
    
    def __to_dict__(self):
        return {
            'id_huesped': self.id_huesped,
            'nombre': self.nombre,
            'correo': self.correo,
            'telefono': self.telefono
        }