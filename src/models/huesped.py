from persona import Persona

class Huesped(Persona):
    def __init__(self, name, correo, telefono, id_huesped):
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