from database.connection import DatabaseConnection
from models.task import Task


class TaskRepository:
    """
    Repositorio encargado de realizar todas las operaciones
    sobre la tabla tasks. es una forma de reutilizar el código y mantenerlo organizado, evitando la duplicación de código en diferentes partes de la aplicación.
    """

    def __init__(self, database):
        self.connection = database.get_connection()



