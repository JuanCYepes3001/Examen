from read_json import*
from w_json import *
from validaciones import validar_ids_existen
def crear_pelicula():
    nueva_pelicula = {}

    nueva_pelicula['id'] = input("Ingrese la ID de la nueva película: ")

    if any(pelicula['id'] == nueva_pelicula['id'] for pelicula in lista_peliculas):
        print("Error: La ID de la película ya existe.")
        return

    nueva_pelicula['nombre'] = input("Ingrese el nombre de la nueva película: ")
    nueva_pelicula['duracion'] = input("Ingrese la duración de la nueva película: ")
    nueva_pelicula['sinopsis'] = input("Ingrese la sinopsis de la nueva película: ")

    nueva_pelicula['generos'] = input("Ingrese las IDs de géneros separadas por comas: ")
    ids_generos = [g.strip() for g in nueva_pelicula['generos'].split(',')]
    if not validar_ids_existen(ids_generos, lista_generos):
        print("Error: Una o más IDs de géneros no existen.")
        return

    nueva_pelicula['actores'] = input("Ingrese las IDs de actores separadas por comas: ")
    ids_actores = [a.strip() for a in nueva_pelicula['actores'].split(',')]
    if not validar_ids_existen(ids_actores, lista_actores):
        print("Error: Una o más IDs de actores no existen.")
        return

    nueva_pelicula['formato'] = input("Ingrese las IDs de formatos separadas por comas: ")
    ids_formatos = [f.strip() for f in nueva_pelicula['formato'].split(',')]
    if not validar_ids_existen(ids_formatos, lista_formatos):
        print("Error: Una o más IDs de formatos no existen.")
        return

    lista_peliculas.append(nueva_pelicula)
    print("Película creada con éxito.")
    guardar_peliculas()

def crear_actores():
    nuevo_actor={}
    nuevo_actor['id']=input("Ingrese el id del actor: ")
    if any(actor['id'] == nuevo_actor['id'] for actor in lista_actores):
        print("Error: La ID de la película ya existe.")
        return
    nuevo_actor['nombre'] = input("Ingrese el nombre del actor: ")
   

    lista_peliculas.append(nuevo_actor)
    print("Se creó el actor con éxito")
    guardar_actores()

def crear_formato():
    nuevo_formato={}
    nuevo_formato['id']=input("Ingrese el id del formato: ")
    if any(formato['id'] == nuevo_formato['id'] for formato in lista_formatos):
        print("Error: La ID de la película ya existe.")
        return
    nuevo_formato['nombre'] = input("Ingrese el nombre del formato: ")
   

    lista_peliculas.append(nuevo_formato)
    print("Se creó el formato con éxito")
    guardar_formatos()

def crear_genero():
    nuevo_genero={}
    nuevo_genero['id']=input("Ingrese el id del genero: ")
    if any(genero['id'] == nuevo_genero['id'] for genero in lista_generos):
        print("Error: La ID de la película ya existe.")
        return
    nuevo_genero['nombre'] = input("Ingrese el nombre del genero: ")
   

    lista_peliculas.append(nuevo_genero)
    print("Se creó el genero con éxito")
    guardar_generos()