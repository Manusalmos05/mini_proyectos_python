from datetime import datetime


class Task:
    """Clase que representa una tarea en el sistema de gestión de tareas."""

    def __init__(
        self,
        nombre: str,
        descripcion: str,
        fecha_limite: date,
        prioridad: str,
        terminada: bool = False,
        fecha_creacion: datetime | None = None,
        task_id: int | None = None
    ):
        self.id = task_id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion or datetime.now()
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.terminada = terminada

    def mark_completed(self):
        """Marca la tarea como completada."""
        self.terminada = True

    def __str__(self):
        status = "✔" if self.terminada else "✘"

        """Devuelve una representación en cadena de la tarea."""

        return (
            f"{status} "
            f"{self.nombre} "
            f"({self.prioridad})"
        )
