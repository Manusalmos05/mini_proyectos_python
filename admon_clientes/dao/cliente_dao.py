from mysql.connector import Error
from admon_clientes.database.conexion import Conexion
from admon_clientes.models.cliente import Cliente

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


if __name__=='__main__':
    clientes=ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)