from models.task import Task



class TaskRepository:
    """
    Repositorio encargado de realizar todas las operaciones
    CRUD sobre la tabla tasks.
    """

    def __init__(self, database):
        self.connection = database.get_connection()

    def add_task(self, task: Task) -> int:
        """
        Guarda una nueva tarea en la base de datos.

        Args:
            task (Task): Objeto Task.

        Returns:
            int: ID generado por MySQL.
        """

        query = """
            INSERT INTO tasks
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

        task.id_task = cursor.lastrowid

        cursor.close()

        return task.id_task

    def get_all_tasks(self) -> list[Task]:
        """
        Devuelve todas las tareas almacenadas.
        """

        query = """
            SELECT
                id
                nombre,
                descripcion,
                fecha_creacion,
                fecha_limite,
                prioridad,
                terminada
            FROM tasks
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

    def get_task_by_id(self, task_id: int) -> Task | None:
        """
        Busca una tarea por su ID.
        """

        query = """
            SELECT *
            FROM tasks
            WHERE id_task = %s
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

    def update_task(self, task: Task) -> bool:
        """
        Actualiza una tarea existente.
        """

        query = """
            UPDATE tasks
            SET
                nombre = %s,
                descripcion = %s,
                fecha_creacion = %s,
                fecha_limite = %s,
                prioridad = %s,
                terminada = %s
            WHERE id_task = %s
        """

        valores = (
            task.nombre,
            task.descripcion,
            task.fecha_creacion,
            task.fecha_limite,
            task.prioridad,
            task.terminada,
            task.id_task
        )

        cursor = self.connection.cursor()

        cursor.execute(query, valores)

        self.connection.commit()

        actualizado = cursor.rowcount > 0

        cursor.close()

        return actualizado

    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea.
        """

        query = """
            DELETE FROM tasks
            WHERE id_task = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (task_id,))

        self.connection.commit()

        eliminado = cursor.rowcount > 0

        cursor.close()

        return eliminado

    def mark_completed(self, task_id: int) -> bool:
        """
        Marca una tarea como terminada.
        """

        query = """
            UPDATE tasks
            SET terminada = TRUE
            WHERE id_task = %s
        """

        cursor = self.connection.cursor()

        cursor.execute(query, (task_id,))

        self.connection.commit()

        actualizado = cursor.rowcount > 0

        cursor.close()

        return actualizado