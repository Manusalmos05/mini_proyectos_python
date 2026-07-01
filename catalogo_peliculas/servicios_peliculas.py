import os.path
from pelicula import Pelicula
import pelicula

#creaccion de archivo para manejar las peliculas
class ServiciosPeliculas: 
    nombre_archivo = 'peliculas.txt'

    def __init__(self):
        self.peliculas = []
        #revisar archivo primero
        #obtener datos d epeliculas
        if os.path.exists(self.nombre_archivo):
            self.peliculas=self.obtener_peliculas()
        #sino, cargar peliculas de prueba
        else:
            self.cargar_peliculas_prueba()
    

    def cargar_peliculas_prueba(self):
        peliculas_prueba = [
        Pelicula('EL PADRINO'),
        Pelicula('BABE EL CERDITO VALIENTE'),
        Pelicula('EL SEÑOR DE LOS ANILLOS')
        ]

        self.peliculas.extend(peliculas_prueba)
        self.guardar_peliculas(peliculas_prueba)

    #guarda las peliculas en el archivo
    
    def guardar_peliculas(self, peliculas):
        try:
            with open(self.nombre_archivo, 'a') as archivo:
                for pelicula in peliculas:
                    archivo.write(f'{pelicula.nombre}\n')
        except Exception as e:
            print(f'Error al guardar las peliculas: {e}')

    #agrega nuevos titulos al archivo de peliculas
    
    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_peliculas([pelicula])

    #muestra en consola las peliculas disponibles en el archivo de peliculas

    def listar_peliculas(self):
        print("-----------Peliculas disponibles-----------")
        with open(self.nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())

    #obtiene las peliculas del archivo de peliculas y las devuelve en una lista de objetos Pelicula

    def obtener_peliculas(self):
        peliculas = []
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                for linea in archivo:
                    nombre = linea.strip()
                    peliculas.append(Pelicula(nombre))
        except Exception as e:
            print(f'Error al obtener las peliculas: {e}')
        return peliculas


    #elimina un titulo de pelicula del archivo de peliculas
    def eliminar_pelicula(self):
        print("dime el nombre de la pelicula que quieres eliminar")
        try:
            nombre = input().strip().upper()
            print(nombre)

        except ValueError:
            print("Error: Debes introducir un titulo de pelicula valido.")
      
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                lineas = [linea.strip().upper() for linea in archivo]


            if nombre in lineas:
                lineas.remove(nombre)
                with open(self.nombre_archivo, 'w') as archivo:
                    lineas_con_salto = [f"{pelicula}\n" for pelicula in lineas]
                    archivo.writelines(lineas_con_salto)
                print(f'La pelicula "{nombre}" ha sido eliminada del catalogo.')
        except Exception as e:
            print(f'Error al eliminar la pelicula: {e}')

    