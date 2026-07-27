from dao.cliente_dao import ClienteDAO
from models.cliente import Cliente

class Menu:


    @staticmethod
    def main_menu():
        salir = False
        print('*** Gestor de Clientes ***')
        
        while not salir:
            try:
                opcion = Menu.menu()
                salir = Menu.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}')
    @staticmethod
    def menu():
        print('¿Qué deseas hacer?')
        print(f'''Seleccione una opción:\n
            1. Crea un nuevo cliente\n
            2. Actualiza a un cliente\n
            3. Elimina un cliente\n
            4. Lista todos los clientes\n
            5. Salir\n
    ''')
        try:
            return int(input('Elige una opción: '))
        except ValueError:
            return 0 # Retorna opción inválida si no es un número

    @staticmethod
    def ejecutar_opcion(opcion):
            
        if opcion == 1:
            print('\n--- Crear Nuevo Cliente ---')
            nombre = input('Nombre: ')
            apellido = input('Apellido: ')
            membresia = int(input('Membresía (Número): '))
            
            valores = Cliente(nombre=nombre, apellido=apellido, membresia=membresia)
            registros = ClienteDAO.insertar(valores)
            print(f'Clientes insertados: {registros}\n')

        elif opcion == 2:
            print('\n--- Actualizar Cliente ---')
            id_cliente = int(input('ID del cliente a actualizar: '))
            nombre = input('Nuevo Nombre: ')
            apellido = input('Nuevo Apellido: ')
            membresia = int(input('Nueva Membresía (Número): '))
            
            
            cliente_actualizar = Cliente(id_cliente, nombre, apellido, membresia)
            registros = ClienteDAO.actualizar(cliente_actualizar)
            print(f'Clientes actualizados: {registros}\n')

        elif opcion == 3:
            print('\n--- Eliminar Cliente ---')
            id = int(input('ID del cliente a eliminar: '))
            id=Cliente(id=id)
            registros = ClienteDAO.eliminar(id)
            print(f'Clientes eliminados: {registros}\n')
            


        elif opcion == 4:
            print('\n--- Listado de Clientes ---')
            clientes = ClienteDAO.seleccionar()
            for cliente in clientes:
                print(cliente)

        elif opcion == 5:
            print("Regresa pronto!")
            return True

        else:
            print("Opción inválida.")

        return False