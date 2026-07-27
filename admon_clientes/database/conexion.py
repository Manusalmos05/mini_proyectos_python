from mysql.connector import pooling
from mysql.connector import Error


class Conexion:
    DATABASE='admon_clientes' 
    USERNAME='root'
    PASSWORD='Manuela0512*'
    DB_PORT='3306'
    HOST='localhost'
    POOL_SIZE=5
    POOL_NAME='admon_clientes_pool'
    pool=None


    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # se crea este ojbjeto pool
            try:
                cls.pool=pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool

            except Error as e:
                print(f'ocurrio un error al obtener pool: {e}')

        else:
            return cls.pool


    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

