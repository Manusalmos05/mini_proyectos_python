from datetime import date
from models.task import Task
from database.connection import DatabaseConnection
from repository.task_repository import TaskRepository
from ui.menu import menu, ejecutar_opcion


def main():
    database = DatabaseConnection()
    repository = TaskRepository(database.get_connection())
    
    

    tarea = Task(

    nombre="mejorar mi repositorio de tareas",
    descripcion="Guardar una tarea en MySQL",
    fecha_creacion=date.today(),
    fecha_limite=date(2026, 7, 30),
    prioridad="Alta",
    terminada=False
    )

    id_generado = repository.crear_tarea(tarea)

    print(f"Tarea creada con ID: {id_generado}")

#listar las tareas
    tareas = repository.listar_tareas()

    print(f"Se encontraron {len(tareas)} tareas.\n")

    for tarea in tareas:
        print("-----------------------------")
        print(f"ID: {tarea.id}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Descripción: {tarea.descripcion}")
        print(f"Fecha creación: {tarea.fecha_creacion}")
        print(f"Fecha límite: {tarea.fecha_limite}")
        print(f"Prioridad: {tarea.prioridad}")
        print(f"Terminada: {tarea.terminada}")
        print("-----------------------------")





if __name__ == "__main__":
    main()