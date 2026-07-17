from services.task_service import TaskService
class Menu:
    def __init__(self):
        self.task_service = TaskService()

    def main_menu(self):
            salir = False
            print('*** Gestor de Tareas ***')
            self.menu()
            while not salir:
                try:
                    opcion = self.menu()
                    salir = self.ejecutar_opcion(opcion)
                except Exception as e:
                    print(f'Ocurrio un error: {e}')
    def menu():
        print("¿Qué deseas hacer?\n")
        print(f'''Seleccione una opción:\n
                1. Crear una nueva tarea\n
                2. Listar todas las tareas\n
                3. Buscar una tarea por ID\n
                4. Actualizar una tarea\n
                5. Marcar una tarea como terminada\n
                6.Borrar una tarea\n
                7. Salir\n
        ''')
        return int(input('Elige una opción: '))

    def ejecutar_opcion(self, opcion):
            if opcion == 1:
                self.crear_tarea()
            elif opcion == 2:
                self.listar_tareas()
            elif opcion == 3:
                self.buscar_tarea_id()
            elif opcion == 4:
                self.actualizar_tarea()
            elif opcion == 5:
                self.marcar_tarea_terminada()
            elif opcion == 6:
                self.borrar_tarea()
            elif opcion == 7:
                print('Regresa pronto!')
                return True
            else:
                print(f'Opción inválida: {opcion}')
            return False