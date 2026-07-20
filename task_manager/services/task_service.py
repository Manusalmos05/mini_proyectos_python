from models.task import Task
from repository.task_repository import TaskRepository
from datetime import datetime

class TaskService:
    """
    Capa de servicios.

    Se encarga de aplicar la lógica de negocio y de
    comunicarse con el repositorio.
    """
    #opciones permitidas para la prioridad de la tarea
    PRIORIDADES_VALIDAS = ("Alta", "Media", "Baja")

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def crear_tarea(self, task: Task) -> int:
        """
        Crea una nueva tarea.
        Valida las opciones de la tarea antes de enviarla al repositorio.
        """
        #normalizaciones de texto en nombre y descripcion de la tarea
        task.nombre = task.nombre.strip()
        task.descripcion = task.descripcion.strip()
        
        task.prioridad = task.prioridad.strip().capitalize()

        #logica de validacion de la tarea
        if not task.nombre:
            raise ValueError("El nombre de la tarea es obligatorio.")
        if task.fecha_limite is None:
            raise ValueError("Debe indicar una fecha límite.")
        if task.prioridad not in self.PRIORIDADES_VALIDAS:
            raise ValueError("La prioridad debe ser Alta, Media o Baja.")
        if task.fecha_limite < datetime.today():
            raise ValueError("La fecha límite no puede ser anterior a hoy.")
        if task.fecha_limite < task.fecha_creacion:
            raise ValueError("La fecha límite no puede ser anterior a la fecha de creación.")
        
        
        return self.repository.crear_tarea(task)

    def listar_tareas(self) -> list[Task]:
        """
        Devuelve todas las tareas.
        """

        return self.repository.listar_tareas()

    def buscar_tarea_id(self, task_id: int) -> Task | None:
        """
        Busca una tarea por su ID.
        """
        #validacion de la entrada del ID
        if not isinstance(task_id, int):
            
            raise ValueError("El ID debe ser un número entero.")
        #se realiza la busqueda de la tarea en el repositorio
        tarea = self.repository.buscar_tarea_id(task_id)
        #si la tarea no existe, se lanza una excepcion
        if tarea is None:
            raise ValueError("La tarea no existe.")
        #si la tarea existe, se devuelve

        return tarea


    def borrar_tarea(self, task_id: int) -> bool:
        """
        Elimina una tarea.
        """
        self.buscar_tarea_id(task_id)

        return self.repository.borrar_tarea(task_id)

    def marcar_tarea_terminada(self, task_id: int) -> bool:
        """
        Marca una tarea como terminada.
        """
        tarea=self.buscar_tarea_id(task_id)
        if tarea.terminada:
            raise ValueError("La tarea ya está marcada como terminada.")
        return self.repository.marcar_tarea_terminada(task_id)