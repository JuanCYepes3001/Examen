from read_json import *
from w_json import *

def eliminar_genero_por_id():
    id_a_eliminar = input("Ingrese el 'id' del elemento que desea eliminar: ")
    try:
        lista_generos = read_generos()

        lista_generos_filtrada = [genero for genero in lista_generos if genero["id"] != id_a_eliminar]
        
        guardar_generos(lista_generos_filtrada)
    
        print(f"Elemento con id '{id_a_eliminar}' eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el elemento: {e}")

def eliminar_formato_por_id():
    id_a_eliminar = input("Ingrese el 'id' del elemento que desea eliminar: ")
    try:
        lista_formatos = read_formatos()

        lista_formatos_filtrada = [formato for formato in lista_formatos if formato["id"] != id_a_eliminar]
        
        guardar_formatos(lista_formatos_filtrada)
    
        print(f"Elemento con id '{id_a_eliminar}' eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el elemento: {e}")

def eliminar_actor_por_id():
    id_a_eliminar = input("Ingrese el 'id' del elemento que desea eliminar: ")
    try:
        lista_actors = read_actores()

        lista_actors_filtrada = [actor for actor in lista_actors if actor["id"] != id_a_eliminar]
        
        guardar_actores(lista_actors_filtrada)
    
        print(f"Elemento con id '{id_a_eliminar}' eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el elemento: {e}")

def eliminar_pelicula_por_id():
    id_a_eliminar = input("Ingrese el 'id' del elemento que desea eliminar: ")
    try:
        lista_peliculas = read_peliculas()

        lista_peliculas_filtrada = [pelicula for pelicula in lista_peliculas if pelicula["id"] != id_a_eliminar]
        
        guardar_peliculas(lista_peliculas_filtrada)
    
        print(f"Elemento con id '{id_a_eliminar}' eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar el elemento: {e}")