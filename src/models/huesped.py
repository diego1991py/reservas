from persona import Persona
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Añade la raíz al path
from utils.manager_huesped import ManagerHuesped


class Huesped(Persona):
    def __init__(self, id_huesped, name, correo, telefono, ):
        super().__init__(name, correo, telefono)
        self.id_huesped = id_huesped

    def __str__(self):
        return f'Huesped: ID Huesped: {self.id_huesped}, {self.name}, Correo: {self.correo}, Telefono: {self.telefono}'
    
    def __to_dict__(self):
        return {
            'id_huesped': self.id_huesped,
            'name': self.name,
            'correo': self.correo,
            'telefono': self.telefono
        }