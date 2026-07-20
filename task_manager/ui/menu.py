from datetime import datetime


from models.task import Task

class Menu:
    def __init__(self, task_service):
        self.task_service = task_service

    def main_menu(self):
            salir = False
            print('*** Gestor de Tareas ***')
            
            while not salir:
                try:
                    opcion = self.menu()
                    salir = self.ejecutar_opcion(opcion)
                except Exception as e:
                    print(f'Ocurrio un error: {e}')
    def menu(self):
        print("¿Qué deseas hacer?\n")
        print(f'''Seleccione una opción:\n
                1. Crear una nueva tarea\n
                2. Listar todas las tareas\n
                3. Buscar una tarea por ID\n
                4. Marcar una tarea como terminada\n
                5.Borrar una tarea\n
                6. Salir\n
        ''')
        return int(input('Elige una opción: '))
    
    def pedir_task_id(self):
        """
        Solicita al usuario el ID de una tarea.
        """

        while True:

            try:
                task_id = int(input("Introduce el ID de la tarea: "))

                if task_id <= 0:
                    print("El ID debe ser mayor que cero.")
                    continue

                return task_id

            except ValueError:
                print("Debes introducir un número entero.")
        

    def ejecutar_opcion(self, opcion):
        

        if opcion == 1:
            self.crear_tarea()

        elif opcion == 2:
            tareas=self.task_service.listar_tareas()
            if not tareas:
                print("\nNo hay tareas registradas.\n")
            else:
                for tarea in tareas:
                    print(tarea)

        elif opcion == 3:
            task_id = self.pedir_task_id()
            tarea=self.task_service.buscar_tarea_id(task_id)
            print(tarea)

        elif opcion == 4:
            task_id = self.pedir_task_id()
            self.task_service.marcar_tarea_terminada(task_id)
            print("\n✅ La tarea ha sido marcada como terminada.\n")

        elif opcion == 5:
            task_id = self.pedir_task_id()
            self.task_service.borrar_tarea(task_id)
            print("\n🗑️ Tarea eliminada correctamente.\n")

        elif opcion == 6:
            print("Regresa pronto!")
            return True

        else:
            print("Opción inválida.")

        return False
    
    def crear_tarea(self):
         
        print("\n---------Nueva Tarea-------------")
        nombre=input("Nombre: ").strip()
        descripcion = input("Descripción: ").strip()
        fecha_creacion_texto = input("Fecha inicio (AAAA-MM-DD): ")
        fecha_creacion=datetime.strptime(fecha_creacion_texto, "%Y-%m-%d")
        fecha_limite_texto = input("Fecha fin (AAAA-MM-DD): ")
        fecha_limite=datetime.strptime(fecha_limite_texto, "%Y-%m-%d")
        prioridad = input("Prioridad (Alta, Media, Baja): ")
        
        tarea=Task(
            nombre=nombre,
            descripcion=descripcion,
            fecha_creacion=fecha_creacion,
            fecha_limite=fecha_limite,
            prioridad=prioridad)

        self.task_service.crear_tarea(tarea)
        print("\n✅ Tarea creada correctamente.\n")