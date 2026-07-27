from mysql.connector import Error
from database.conexion import Conexion
from models.cliente import Cliente

class ClienteDAO:
    SELECCIONAR='SELECT * FROM cliente ORDER BY id'
    INSERTAR='INSERT INTO cliente(nombre,apellido,membresia)VALUES(%s, %s, %s)'
    ACTUALIZAR='UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR='DELETE FROM cliente WHERE id=%s'


    @classmethod
    def seleccionar(cls):
        conexion=None
        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros=cursor.fetchall()
            #mapeo de clase-tabla cliente

            clientes=[]
            for registro in registros:
                cliente=Cliente(registro[0],registro[1],registro[2],registro[3] ) #id, nombre, apellido y membresia
                clientes.append(cliente)
            return clientes


        except Error as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def insertar(cls, cliente):
        conexion= None

        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar los datos: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def actualizar(cls, cliente):
        conexion= None

        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            valores=(cliente.nombre, cliente.apellido, cliente.membresia,cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar los datos: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion= None

        try:
            conexion=Conexion.obtener_conexion()
            cursor=conexion.cursor()
            id=(cliente.id,)
            cursor.execute(cls.ELIMINAR, id)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar los datos: {e}')

        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)