import json
import os



def listar():
    print("Listado de peliculas: ")
    for camper in lista_peliculas:
        print(camper)

def read_actores():
    try:
        with open(os.path.join("data","actores.json"), 'r') as peliculas_json:        
            lista_peliculas = json.load(peliculas_json)
            print("La lista de ha sido cargada")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
def read_formatos():
    try:
        with open(os.path.join("data","formatos.json"), 'r') as peliculas_json:        
            lista_peliculas = json.load(peliculas_json)
            print("La lista de ha sido cargada")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
def read_generos():
    try:
        with open(os.path.join("data","generos.json"), 'r') as peliculas_json:        
            lista_peliculas = json.load(peliculas_json)
            print("La lista de ha sido cargada")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []
def read_peliculas():
    try:
        with open(os.path.join("data","peliculas.json"), 'r') as peliculas_json:        
            lista_peliculas = json.load(peliculas_json)
            print("La lista de ha sido cargada")
            return lista_peliculas
    except FileNotFoundError:
        print("El archivo 'Ingresos.json' no existe. Devolviendo una lista vacía.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return []

lista_actores = read_actores()
lista_formatos = read_formatos()
lista_generos = read_generos()
lista_peliculas = read_peliculas()






