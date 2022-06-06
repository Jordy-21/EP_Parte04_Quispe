# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:03:02 2022

@author: Alfonso
"""


def listar_producto():
    f = open("nombre.txt", "r")
    g = open("codigo.txt", "r")
    h = open("precio.txt", "r")
    print("\n***LISTANDO NOMBRE,CÓDIGO Y PRECIO respectivamente.***\n")
    print("\n***NOMBRE   --   CÓDIGO   --   PRECIO***\n")
    while(True):
     nombre = f.readline()
     codigo = g.readline()
     precio = h.readline()
     nombre=nombre.strip('\n')
     codigo=codigo.strip('\n')
     precio=precio.strip('\n')
     print ("{:<15} {:<15} {:<10}".format(nombre,codigo,precio))
     if not nombre:
       break
    
    

def agregar_producto():
    contenido1 = input("Nombre: ")
    archivo1 = open("nombre.txt","at")
    archivo1.write("\n"+ contenido1)
    contenido2 = input("Código: ")
    archivo2 = open("codigo.txt","at")
    archivo2.write("\n"+ contenido2)
    contenido3 = input("Precio: ")
    archivo3 = open("precio.txt","at")
    archivo3.write("\n"+ contenido3)
    archivo1.close()
    archivo2.close()
    archivo3.close()

def salir():
    print("Vuelva pronto...")