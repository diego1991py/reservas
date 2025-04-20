from datetime import datetime
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Añade la raíz al path
from models.huesped import Huesped
from utils.manager_huesped import ManagerHuesped
from logs.registro_logs import RegistroLogs
from models.reservas import Reservas
from utils.manager_reservas import ManagerReservas

manager_huesped = ManagerHuesped()
manager_reservas = ManagerReservas()
registro_logs = RegistroLogs()



while True:
    print("\n1. Registrar Huesped")
    print("2. Mostrar Huespedes")
    print("3. Registrar Reserva")
    print("4. Mostrar Reservas")
    print("5. Salir")
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
        id_reserva = int(input("Ingrese el ID de la reserva: "))
        id_cliente = int(input("Ingrese el ID del cliente: "))
        id_habitacion = int(input("Ingrese el ID de la habitación: "))
        y_inicio = input("Ingrese la año de reserva (YYYY): ").strip()
        m_inicio = input("Ingrese la año de reserva (mm): ").strip()
        d_inicio = input("Ingrese la año de reserva (dd): ").strip()

        fecha_inicio = datetime(int(y_inicio), int(m_inicio), int(d_inicio))

        dias_reserva = int(input("Ingrese la cantidad de días de reserva: "))

        nueva_reserva = Reservas(id_reserva, id_cliente, id_habitacion, fecha_inicio, dias_reserva)
        manager_reservas.nuevo_registro(nueva_reserva.__to_dict__())
        registro_logs.registrar(f"Se ha registrado la reserva: {nueva_reserva}")

        manager_reservas.guardar_reservas()
        print(f"Reserva registrada: {nueva_reserva}")        

    elif opcion == "4":
        manager_reservas.__str__()
        #print(manager_reservas.reservas)

    elif opcion == "5":
        print("Saliendo del programa...")
        registro_logs.registrar("El programa ha sido cerrado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
# from logs.registro_logs import RegistroLogs
