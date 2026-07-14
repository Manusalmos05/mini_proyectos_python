import mysql.connector
from mysql.connector import Error

from database.config import DB_CONFIG



class DatabaseConnection:
    """
    Gestiona la conexión con la base de datos MySQL.
    """

    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        """
        Establece la conexión con la base de datos.
        """
        try:
            self.connection = mysql.connector.connect(**DB_CONFIG)

            if self.connection.is_connected():
                print("Conexión con MySQL realizada correctamente.")

        except Error as error:
            print(f"Error al conectar con MySQL: {error}")

    def get_connection(self):
        """
        Devuelve la conexión activa.
        """
        return self.connection

    def close_connection(self):
        """
        Verifica si la conexión está activa y la cierra.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada.")


