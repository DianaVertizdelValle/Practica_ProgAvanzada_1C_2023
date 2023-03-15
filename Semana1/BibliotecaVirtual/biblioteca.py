# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:12:19 2023

@author: je_su
"""

OPCIONES = """
Elige una opción:
1. Ingresar libro nuevo
2. Listar libros
3. Salir
"""
ARCHIVO = "libros_leidos.txt"

#print(__name__)

def main():
    lista_libros = []
    salir = False
    
    try:
        with open(ARCHIVO, "r") as archi:
            for linea in archi:
                lista_lib = linea.rstrip().split(",")
                libro = {
                        "nombre": lista_lib[0],
                        "autor": lista_lib[1],
                        "puntaje": lista_lib[2],
                    }
                lista_libros.append(libro)
    except FileNotFoundError:
        with open(ARCHIVO, "w") as archi:
            pass    
    
    while not salir:
        opcion = input(OPCIONES)
        if opcion == "1":
            nombre_libro = input("ingresar nombre del libro: ")
            autor_libro = input("ingresar autor del libro: ")
            puntaje_libro = input("ingresar puntaje del libro: ")
            libro = {
                "nombre": nombre_libro,
                "autor": autor_libro,
                "puntaje": puntaje_libro
                }
            lista_libros.append(libro)
        elif opcion == "2":
            if len(lista_libros)== 0:
                print("La Biblioteca está vacía")
            else:
                for libro in lista_libros:
                    print(f"{libro['nombre']} - {libro['autor']} - {libro['puntaje']}/10")
        elif opcion == "3":
            with open(ARCHIVO, "w") as archi:                
                for libro in lista_libros:
                    archi.write(f"{libro['nombre']},{libro['autor']},{libro['puntaje']}\n")
            salir = True
        else:
            print("La opción ingresada no es correcta")
        


if __name__ == "__main__":
    main()