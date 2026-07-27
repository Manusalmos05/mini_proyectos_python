from dao.cliente_dao import ClienteDAO
from models.cliente import Cliente







if __name__=='__main__':
    # insertar
    cliente1=Cliente(nombre='Alberto', apellido='Varela', membresia=150)
    cliente_actualizado=ClienteDAO.insertar(cliente1)

    clientes=ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)