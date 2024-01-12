from commons.read_json import *
from commons.w_json import *

def eliminar_elemento_por_id(file_path):
    try:
        id_a_eliminar = input(f"Ingrese el 'id' del elemento que desea eliminar en {file_path}: ")

        with open(file_path, 'r') as json_file:
            lista_elementos = json.load(json_file)

        # Mensajes de depuración
        print(f"Antes de la eliminación: {lista_elementos}")

        lista_elementos_filtrada = [elemento for elemento in lista_elementos if elemento["id"] != id_a_eliminar]

        # Mensajes de depuración
        print(f"Después de la eliminación: {lista_elementos_filtrada}")

        with open(file_path, 'w') as json_file:
            json.dump(lista_elementos_filtrada, json_file, indent=2)

        print(f"Elemento con ID '{id_a_eliminar}' eliminado correctamente en {file_path}.")
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no existe.")
    except Exception as e:
        print(f"Error al eliminar el elemento: {e}")
        
def eliminar_genero_por_id():
    eliminar_elemento_por_id("data/generos.json")
def eliminar_formato_por_id():
    eliminar_elemento_por_id("data/formatos.json")
def eliminar_actor_por_id():
    eliminar_elemento_por_id("data/actores.json")

def eliminar_pelicula_por_id():
    eliminar_elemento_por_id("data/peliculas.json")


