from commons.validaciones import validar_opcion 
def menu_principal():
    print("----------- Menú Principal-----------")
    print("1. Ingresar informacion")
    print("2. Eliminar informacion")
    print("3. Editar informacion")
    print("4. Buscar pelicula")
    print("5. Salir")       
    print("-------------------------------------")
    op=validar_opcion("Opcion: ",1,5)
    return op

def menu_busquedas():
    print("----------- Menú Busquedas-----------")
    print("1. Buscar por genero")
    print("2. Buscar por codigo")
    print("3. Salir")       
    op=validar_opcion("Opcion: ",1,3)
    return op

def menu_info():
    print("-----------Ingresa informacion a-----------")
    print("1. Agregar actor")
    print("2. Agregar genero")
    print("3. Agregar pelicula")
    print("4. Agregar formato")
    print("5. Salir")       
    op=validar_opcion("Opcion: ",1,5)
    return op
def menu_info2():
    print("-----------Eliminar informacion a-----------")
    print("1. Eliminar actor")
    print("2. Eliminar genero")
    print("3. Eliminar pelicula")
    print("4. Eliminar formato")
    print("5. Salir")       
    op=validar_opcion("Opcion: ",1,5)
    return op
def menu_info3():
    print("-----------Editar informacion a-----------")
    print("1. Editar actor")
    print("2. Editar genero")
    print("3. Editar pelicula")
    print("4. Editar formato")
    print("5. Salir")       
    op=validar_opcion("Opcion: ",1,5)
    return op
def mod_pelicula():
    print("----------- Modificar pelicula-----------")
    print("Seleccione el dato que desea modificar")
    print("1. Id")
    print("2. Nombre")
    print("3. Duracion")
    print("4. Sinopsis")
    print("5. Generos")
    print("6. Actores")
    print("7. Formato")
    print("8. Salir")       
    print("-------------------------------------")
    op=validar_opcion("Opcion: ",1,8)
    return op