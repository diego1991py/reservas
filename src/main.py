import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Añade la raíz al path
from models.huesped import Huesped
from utils.manager_huesped import ManagerHuesped
from logs.registro_logs import RegistroLogs

manager_huesped = ManagerHuesped()
registro_logs = RegistroLogs()



while True:
    print("\n1. Registrar Huesped")
    print("2. Mostrar Huespedes")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id_huesped = int(input("Ingrese el ID del huesped: "))
        nombre = input("Ingrese el nombre del huesped: ")
        correo = input("Ingrese el correo del huesped: ")
        telefono = input("Ingrese el teléfono del huesped: ")

        nuevo_huesped = Huesped(id_huesped, nombre, correo, telefono)
        manager_huesped.nuevo_registro(nuevo_huesped.__to_dict__())
        registro_logs.registrar(f"Se ha registrado el huesped: {nuevo_huesped}")
        manager_huesped.guardar_huespedes()
        print(f"Huesped registrado: {nuevo_huesped}")

    elif opcion == "2":
            manager_huesped.__str__()

    elif opcion == "3":
        break

    else:
        print("Opción no válida. Intente nuevamente.")
# from logs.registro_logs import RegistroLogs
