class Validar(Exception):
    pass

    def validar_enteros_positivos(habitacion, dias):
        if habitacion <= 0 or dias <= 0:
            raise Validar("El valor debe ser un número entero positivo.")
        return True