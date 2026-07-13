import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Recuperar las credenciales de forma segura
configuracion = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
   
}

try:
    with mysql.connector.connect(**configuracion) as conexion:
        print("Conectado de forma segura.")
        with conexion.cursor() as cursor:
            cursor.execute("SELECT DATABASE();")
            print(f"Base de datos: {cursor.fetchone()}")
            
except Error as e:
    print(f"Error: {e}")


 