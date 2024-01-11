import json
from read_json import *
def guardar_peliculas():
    try:
      with open(os.path.join("data","peliculas.json"), 'w') as peliculas_json:
        json.dump(lista_peliculas, peliculas_json, indent=2)
        print("La lista de ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
    
def guardar_actores():
    try:
      with open(os.path.join("data","actores.json"), 'w') as actores_json:
        json.dump(lista_actores, actores_json, indent=2)
        print("La lista de ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_formatos():
    try:
      with open(os.path.join("data","formatos.json"), 'w') as actores_json:
        json.dump(lista_formatos, actores_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_generos():
    try:
      with open(os.path.join("data","actores.json"), 'w') as actores_json:
        json.dump(lista_generos, actores_json, indent=2)
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")