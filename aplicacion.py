# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:25:24 2024

@author: Dell
"""

login = open("login.txt","rt")
leerLogin = login.read()
password = open("clave.txt","rt")
leerPassword = password.read()
intentos = 0
while intentos < 2:
    user = input("Ingrese su usuario: ")
    clave = input("Ingrese la clave: ")
    if user == leerLogin and clave == leerPassword:
        print("Datos de la Persona")
        print("1. Listar las personas")
        print("2. Agregar las personas")
        print("3. Salir")
        break  # Salir del bucle si las credenciales son correctas
    else:
        print("El usuario y/o clave es incorrecto")
        intentos += 1
        if intentos == 2:
            print("Número máximo de intentos alcanzado. Saliendo del programa.")
            break