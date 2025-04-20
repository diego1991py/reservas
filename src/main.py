from datetime import datetime
import sys 
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Añade la raíz al path
from models.huesped import Huesped
from utils.manager_huesped import ManagerHuesped
from logs.registro_logs import RegistroLogs
from models.reservas import Reservas
from utils.manager_reservas import ManagerReservas
from validaciones.validar import Validar as val

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
        id_huesped = manager_huesped.agregar_id() # Se genera un nuevo ID para el huesped
        nombre = input("Ingrese el nombre del huesped: ")
        correo = input("Ingrese el correo del huesped: ")
        telefono = input("Ingrese el teléfono del huesped: ")

        nuevo_huesped = Huesped(id_huesped, nombre, correo, telefono) # Se crea un nuevo objeto Huesped
        manager_huesped.nuevo_registro(nuevo_huesped.__to_dict__())
        registro_logs.registrar(f"Se ha registrado el huesped: {nuevo_huesped}") # Se registra la acción en el log
        manager_huesped.guardar_huespedes() # Se guardan los cambios en el archivo JSON
        print(f"Huesped registrado: {nuevo_huesped}") # Se imprime el nuevo huesped registrado  

    elif opcion == "2":
            manager_huesped.__str__() # Se imprime la lista de huespedes registrados

    elif opcion == "3":
        id_reserva = manager_reservas.agregar_id() # Se genera un nuevo ID para la reserva
        id_cliente = int(input("Ingrese el ID del cliente: ")) 
        manager_huesped.confirmar_id(id_cliente) # Se verifica si el ID del cliente existe
        
        if not manager_huesped.confirmar_id(id_cliente): # Si el ID no existe, se muestra un mensaje y se vuelve a solicitar el ID
            print("El ID del cliente no existe.")
            continue
        try:
            id_habitacion = int(input("Ingrese el ID de la habitación: "))
            y_inicio = input("Ingrese la año de reserva (YYYY): ").strip()
            m_inicio = input("Ingrese la año de reserva (mm): ").strip()
            d_inicio = input("Ingrese la año de reserva (dd): ").strip()

            fecha_inicio = datetime(int(y_inicio), int(m_inicio), int(d_inicio))
            dias_reserva = int(input("Ingrese la cantidad de días de reserva: "))

            val.validar_enteros_positivos(id_habitacion, dias_reserva)

        
            nueva_reserva = Reservas(id_reserva, id_cliente, id_habitacion, fecha_inicio, dias_reserva) # Se crea un nuevo objeto Reserva
            manager_reservas.nuevo_registro(nueva_reserva.__to_dict__()) # Se agrega la nueva reserva a la lista de reservas
            registro_logs.registrar(f"Se ha registrado la reserva: {nueva_reserva}") # Se registra la acción en el log

            manager_reservas.guardar_reservas() # Se guardan los cambios en el archivo JSON
            print(f"Reserva registrada: {nueva_reserva}") # Se imprime la nueva reserva registrada

        except ValueError:
            print("La cantidad de días de reserva debe ser un número entero.")
        
        except val as e:
            print(f"Error: {e}")

    elif opcion == "4":
        manager_reservas.__str__() # Se imprime la lista de reservas registradas

    elif opcion == "5":
        print("Saliendo del programa...")
        registro_logs.registrar("El programa ha sido cerrado.") # Se registra la acción en el log
        break

    else:
        print("Opción no válida. Intente nuevamente.")
