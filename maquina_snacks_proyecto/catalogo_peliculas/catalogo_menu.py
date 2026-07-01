from servicios_peliculas import ServiciosPeliculas
from pelicula import Pelicula

class CatalogoMenu:
    def __init__(self):
        self.servicios_peliculas = ServiciosPeliculas()
        self.catalogo=[]

    def catalogo_inicio(self):
        salir = False
        print("Bienvenido al catalogo de peliculas")
        self.servicios_peliculas.listar_peliculas()
        while not salir:
            try:
                opcion=self.mostrar_menu()
                salir=self.ejecutar_opcion(opcion)
            except ValueError:
                print("Opcion invalida. Por favor, ingrese un numero valido.")
    
    def mostrar_menu(self):
        print(f'''Menu de opciones:
            1. Agregar pelicula
            2. listar peliculas
            3. Eliminar pelicula
            4. Salir''')
        return int(input("Ingrese el numero de la opcion que desea ejecutar: "))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.agregar_pelicula()
            self.servicios_peliculas.listar_peliculas()
        elif opcion == 2:
            self.servicios_peliculas.listar_peliculas()
        elif opcion == 3:
            self.servicios_peliculas.eliminar_pelicula()
           
        elif opcion == 4:
            print("Saliendo del catalogo de peliculas...")
            return True
        else:
            print("Opcion invalida. Por favor, ingrese un numero valido.")
        return False
    
    def agregar_pelicula(self):
        nombre = input("Ingrese el nombre de la pelicula que desea agregar: ")
        nombre = nombre.upper()
        nueva_pelicula = Pelicula(nombre)
        self.servicios_peliculas.agregar_pelicula(nueva_pelicula)
        print(f'La pelicula "{nombre}" ha sido agregada al catalogo.')
    
if __name__ == "__main__":
    catalogo_menu = CatalogoMenu()
    catalogo_menu.catalogo_inicio()