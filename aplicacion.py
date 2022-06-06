import os

def menu():
    print("*************MENU************\n"+
          "1. Listar\n"+
          "2. Agregar \n"+
          "3. Salir\n")



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
        print('3 intentos fallidos')
        bandera = False

    for usuarioItem in usuarioRespuesta:
        if usuario == usuarioItem:
            for claveoItem in claveRespuesta:
                if clave == claveoItem:
                    bandera = False
                    print('Sesión iniciada !!')
                    opcion = menu()

    if bandera == True:
        print('Usuario o contraseña incorrectas, intente nuevamente')
        contador = contador + 1 
    
    print('\n ')
