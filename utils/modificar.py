from read_json import *
from w_json import *
from menus import mod_pelicula
from validaciones import validar_ids_existen
def modificarActor():
    if not lista_actores:
        print("No hay actores registrados.")
        return

    id_actor = input("Ingrese el id del actor que desea modificar: ")

    for actor in lista_actores:
        if actor['id'] == id_actor:
            print(f"Datos actuales del actor {id_actor}:")
            print(actor)
            dato_a_modificar = input("¿Qué dato desea modificar? (id/nombre): ").lower()
            if dato_a_modificar == "id":
                nuevo_valor = input("Nuevo id del actor: ")
                if nuevo_valor:
                    actor['id'] = nuevo_valor
            elif dato_a_modificar == "nombre":
                nuevo_valor = input("Nueva nombre del actor : ")
                if nuevo_valor:
                    actor['nombre'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Actor modificado con éxito.")
      
            guardar_actores()
            return

    print(f"No se encontró un actor con el id {id_actor}.")

def modificarFormato():
    if not lista_formatos:
        print("No hay formato registrados.")
        return

    id_formato = input("Ingrese el id del formato que desea modificar: ")

    for formato in lista_formatos:
        if formato['id'] == id_formato:
            print(f"Datos actuales del formato {id_formato}:")
            print(formato)
            dato_a_modificar = input("¿Qué dato desea modificar? (id/nombre): ").lower()
            if dato_a_modificar == "id":
                nuevo_valor = input("Nuevo id del formato: ")
                if nuevo_valor:
                    formato['id'] = nuevo_valor
            elif dato_a_modificar == "nombre":
                nuevo_valor = input("Nueva nombre del formato : ")
                if nuevo_valor:
                    formato['nombre'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("formato modificado con éxito.")
      
            guardar_formatos()
            return

    print(f"No se encontró un formato con el id {id_formato}.")

def modificarGenero():
    if not lista_generos:
        print("No hay genero registrados.")
        return

    id_genero = input("Ingrese el id del genero que desea modificar: ")

    for genero in lista_generos:
        if genero['id'] == id_genero:
            print(f"Datos actuales del genero {id_genero}:")
            print(genero)
            dato_a_modificar = input("¿Qué dato desea modificar? (id/nombre): ").lower()
            if dato_a_modificar == "id":
                nuevo_valor = input("Nuevo id del genero: ")
                if nuevo_valor:
                    genero['id'] = nuevo_valor
            elif dato_a_modificar == "nombre":
                nuevo_valor = input("Nueva nombre del genero : ")
                if nuevo_valor:
                    genero['nombre'] = nuevo_valor
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("genero modificado con éxito.")
      
            guardar_generos()
            return

    print(f"No se encontró un genero con el id {id_genero}.")

def modificar_pelicula():
    if not lista_peliculas:
        print("No hay películas registradas.")
        return

    id_pelicula = input("Ingrese la ID de la película que desea modificar: ")

    for pelicula in lista_peliculas:
        if pelicula['id'] == id_pelicula:
            print(f"Datos actuales de la película con ID {id_pelicula}:")
            print(pelicula)
            op = mod_pelicula()

            if op == 1:
                nuevo_valor = input("ID: ")
                if nuevo_valor:
                    pelicula['id'] = nuevo_valor
            elif op == 2:
                nuevo_valor = input("Nombre: ")
                if nuevo_valor:
                    pelicula['nombre'] = nuevo_valor
            elif op == 3:
                nuevo_valor = input("Duración: ")
                if nuevo_valor:
                    pelicula['duracion'] = nuevo_valor
            elif op == 4:
                nuevo_valor = input("Sinopsis: ")
                if nuevo_valor:
                    pelicula['sinopsis'] = nuevo_valor
            elif op == 5:
                nuevo_valor = input("Géneros separados por comas: ")
                if nuevo_valor:
                    ids_generos = [g.strip() for g in nuevo_valor.split(',')]
                    if validar_ids_existen(ids_generos, lista_generos):
                        pelicula['generos'] = ids_generos
                    else:
                        print("Error: Una o más IDs de géneros no existen.")
            elif op == 6:
                nuevo_valor = input("Actores separados por comas: ")
                if nuevo_valor:
                    ids_actores = [a.strip() for a in nuevo_valor.split(',')]
                    if validar_ids_existen(ids_actores, lista_actores):
                        pelicula['actores'] = ids_actores
                    else:
                        print("Error: Una o más IDs de actores no existen.")
            elif op == 7:
                nuevo_valor = input("Formatos separados por comas: ")
                if nuevo_valor:
                    ids_formatos = [f.strip() for f in nuevo_valor.split(',')]
                    if validar_ids_existen(ids_formatos, lista_formatos):
                        pelicula['formato'] = ids_formatos
                    else:
                        print("Error: Una o más IDs de formatos no existen.")
            else:
                print("Opción no válida. No se realizaron modificaciones.")
                return

            print("Película modificada con éxito.")
            guardar_peliculas()
            return

    print(f"No se encontró una película con la ID {id_pelicula}.")

