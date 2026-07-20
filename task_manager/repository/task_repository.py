from models.task import Task

class TaskRepository:
    """
    Repositorio encargado de realizar todas las operaciones
    CRUD sobre la tabla tasks.
    """

    def __init__(self, connection):
        self.connection = connection

    def crear_tarea(self, task: Task) -> int:
        """
        Guarda una nueva tarea en la base de datos.

        Args:
            task (Task): Objeto Task.

        Returns:
            int: ID generado por MySQL.
        """

        query = """
            INSERT INTO task
            (
                nombre,
                descripcion,
                fecha_creacion,
                fecha_limite,
                prioridad,
                terminada
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        valores = (
            task.nombre,
            task.descripcion,
            task.fecha_creacion,
            task.fecha_limite,
            task.prioridad,
            task.terminada
        )

        cursor = self.connection.cursor()

        cursor.execute(query, valores)

        self.connection.commit()

        task.id = cursor.lastrowid

        cursor.close()

        return task.id

    def listar_tareas(self) -> list[Task]:
        """
        Devuelve todas las tareas almacenadas.
        """

        query = """
            SELECT
                id,
                nombre,
                descripcion,
                fecha_creacion,
                fecha_limite,
                prioridad,
                terminada
            FROM task
            ORDER BY fecha_limite ASC
        """

        cursor = self.connection.cursor(dictionary=True)

        cursor.execute(query)

        resultados = cursor.fetchall()

        tareas = []

        for fila in resultados:

            tarea = Task(
                task_id=fila["id"],
                nombre=fila["nombre"],
                descripcion=fila["descripcion"],
                fecha_creacion=fila["fecha_creacion"],
                fecha_limite=fila["fecha_limite"],
                prioridad=fila["prioridad"],
                terminada=bool(fila["terminada"])
            )

            tareas.append(tarea)

        cursor.close()

        return tareas

    def buscar_tarea_id(self, task_id: int) -> Task | None:
        """
        Busca una tarea por su ID.
        """

        query = """
            SELECT *
            FROM task
            WHERE id= %s
        """

        cursor = self.connection.cursor(dictionary=True)

        cursor.execute(query, (task_id,))

        fila = cursor.fetchone()

        cursor.close()

        if fila is None:
            return None

        return Task(
            task_id=fila["id"],
            nombre=fila["nombre"],
            descripcion=fila["descripcion"],
            fecha_creacion=fila["fecha_creacion"],
            fecha_limite=fila["fecha_limite"],
            prioridad=fila["prioridad"],
            terminada=bool(fila["terminada"])
        )


    def borrar_tarea(self, task_id: int) -> bool:
        """
        Elimina una tarea.
        """

        query = """
            DELETE FROM task
            WHERE id = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (task_id,))

        self.connection.commit()

        eliminado = cursor.rowcount > 0

        cursor.close()

        return eliminado

    def marcar_tarea_terminada(self, task_id: int) -> bool:
        """
        Marca una tarea como terminada.
        """

        query = """
            UPDATE task
            SET terminada = TRUE
            WHERE id = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (task_id,))

        self.connection.commit()

        actualizado = cursor.rowcount > 0

        cursor.close()

        return actualizado