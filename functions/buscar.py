from commons.read_json import *

def buscar_peliculas(entrada_busqueda):
    resultados = []

    for pelicula in lista_peliculas:
       
        if entrada_busqueda.lower() in pelicula["nombre"].lower():
            resultados.append(pelicula)
      
        elif entrada_busqueda == pelicula["id"]:
            resultados.append(pelicula)

        elif entrada_busqueda.lower() in [g["nombre"].lower() for g in lista_generos if g["id"] in pelicula["generos"]]:
            resultados.append(pelicula)
        

    return resultados

def buscar():
    try:
       
        entrada_busqueda = input("Ingrese el nombre de la película, el ID de la película o el nombre del género: ")
        resultados = buscar_peliculas(entrada_busqueda)
        if resultados:
            print("Resultados de la búsqueda:")
            for resultado in resultados:
                print(resultado)
        else:
            print("No se encontraron resultados para la búsqueda.")
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")


