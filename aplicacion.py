# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:25:24 2024

@author: Dell
"""
def leer_archivo():
    with open("dni.txt", "rt", encoding='utf8') as dni_file:
        datos_dni = dni_file.read()
        
    with open("nombre.txt", "rt", encoding='utf8') as nombre_file:
        datos_nombre = nombre_file.read()
        
    with open("apellido.txt", "rt", encoding='utf8') as apellido_file:
        datos_apellido = apellido_file.read()
        
    return datos_dni, datos_nombre, datos_apellido

def agregar_persona(dni_content, nombre_content, apellido_content):
    with open("dni.txt", "at", encoding='utf8') as dni_file:
        dni_file.write(dni_content)
        
    with open("nombre.txt", "at", encoding='utf8') as nombre_file:
        nombre_file.write(nombre_content)
        
    with open("apellido.txt", "at", encoding='utf8') as apellido_file:
        apellido_file.write(apellido_content)

def menu():
    print("MENU PRINCIPAL")
    print("1. Listar personas")
    print("2. Agregar personas")
    print("3. Salir")
    
def listar():
    dni, nombre, apellido = leer_archivo()
    print("DNI:\n", dni + "\t")
    print("Nombre:\n", nombre + "\t")
    print("Apellido:\n", apellido + "\t")



def agregar():
    dni_content = input("Ingrese DNI: ")
    nombre_content = input("Ingrese nombre: ")
    apellido_content = input("Ingrese apellido: ")
    agregar_persona(dni_content + "\n", nombre_content + "\n", apellido_content + "\n")
    print("Persona agregada con éxito.")


def salir():
    print("Gracias por su visita....")

def error():
    print("Opción incorrecta")

login = open("login.txt","rt")
leerLogin = login.read()
password = open("clave.txt","rt")
leerPassword = password.read()
intentos = 0
while intentos < 2:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user == leerLogin and clave == leerPassword:
        opcion = 1
        while True:
            menu()
            opcion = int(input("\nopcion: "))
            if opcion == 1:
                listar()
            elif opcion == 2:
                agregar()
            elif opcion == 3:
                salir()
                break
            else:
                error()
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("El usuario y/o clave es incorrecto")
        intentos += 1
        if intentos == 2:
            print("Número máximo de intentos alcanzado. Saliendo del programa.")
            break
