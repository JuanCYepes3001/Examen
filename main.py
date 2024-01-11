from utils.validaciones import limpiar_pantalla
from utils.menus import *
from utils.crear import *
from utils.eliminar import *
from utils.buscar import *
from utils.modificar import *
def Ingresar():
    limpiar_pantalla()
    op=menu_info()
    if  op==1:
        crear_actores
    elif op==2:
        crear_genero
    elif op==3:
        crear_pelicula
    elif op==4:
        crear_formato

def Eliminar():
    limpiar_pantalla()
    op=menu_info()
    if  op==1:
        eliminar_actor_por_id()
    elif op==2:
        eliminar_genero_por_id()
    elif op==3:
        eliminar_pelicula_por_id()
    elif op==4:
        eliminar_formato_por_id()

def Editar():
    limpiar_pantalla()
    op=menu_info()
    if  op==1:
        modificarActor
    elif op==2:
        modificarGenero
    elif op==3:
        modificar_pelicula
    elif op==4:
        modificarFormato
def Buscar():
    limpiar_pantalla()
    buscar()

while True: 
   limpiar_pantalla()
   op=menu_principal()
   if  op==1:
       Ingresar()
   elif op==2:
       Eliminar()
   elif op==3:
       Editar()
   elif op==4:
       Buscar()
   elif op==5:
       print("Saliendo")
       break