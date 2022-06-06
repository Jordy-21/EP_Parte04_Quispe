import modulos

def menu():
    print("\n\n*************MENU************\n"+
          "1. Listar\n"+
          "2. Agregar \n"+
          "3. Salir\n")

    opcion = int(input("\n Ingrese una opcion: "))
    return opcion



def leerArchivo(nombre):
    archivo = open(nombre, "rt", encoding = "utf8")
    contenido = archivo.read()
    contenido = contenido.split('\n')
    return contenido




usuarioRespuesta = leerArchivo('usuarios.txt')
claveRespuesta = leerArchivo('claves.txt')

bandera = True
contador = 0

while bandera == True:
    usuario = input('Ingresa el usuario: ')
    clave = input('Ingresa la clave: ')

    if contador == 2: 
        print('\n3 intentos fallidos, se le denegó el acceso')
        bandera = False
    
    opcion=1

    for usuarioItem in usuarioRespuesta:
        if usuario == usuarioItem:
            for claveoItem in claveRespuesta:
                if clave == claveoItem:
                    bandera = False
                    while opcion!=3:
                     opcion = menu()
                     if opcion == 1:
                        modulos.listar_producto()
                     if opcion == 2:
                       modulos.agregar_producto()
                     if opcion == 3:
                        modulos.salir()
                     if opcion<1 or opcion>3:
                        print("opcion incorrecta, intente de nuevo")


    if bandera == True:
        print('Usuario o contraseña incorrectas')
        contador = contador + 1 
    
    print('\n ')

