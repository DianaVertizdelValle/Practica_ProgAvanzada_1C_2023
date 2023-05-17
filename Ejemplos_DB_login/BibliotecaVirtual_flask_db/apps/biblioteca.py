# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 10:46:25 2023
@author: je_su(Diana)
"""
from modules.archivos import cargar_lista_desde_archivo, guardar_lista_en_archivo


OPCIONES = """
Ingrese su opción:
1. Ingresar libro
2. Listar libros
3. Salir
"""
RUTA = "./data/"
ARCHIVO = RUTA + "libros_leidos1.txt"

def main():
    lista_libros = []
    salir = False
    
    try:
        cargar_lista_desde_archivo(ARCHIVO, lista_libros)            
    except FileNotFoundError:
        with open(ARCHIVO, "w") as archi:
            pass
    
    
    while not salir:
        opcion = input(OPCIONES)
        
        if opcion == "1":
            nombre_libro = input("Ingrese el nombre del libro: ")
            autor_libro = input("Ingrese el nombre del autor: ")
            puntaje_libro = input("Ingrese el puntaje de 0 a 10: ")
            libro = {
             "nombre": nombre_libro,
             "autor": autor_libro,
             "puntaje": puntaje_libro
            }
            lista_libros.append(libro)
            
        elif opcion == "2":
            if len(lista_libros) == 0:        
                print("La lista de libros está vacía")
            else:
                for libro in lista_libros:
                    nombre = libro["nombre"]
                    autor = libro["autor"]
                    puntaje = libro["puntaje"]
                    print(f"{nombre} - {autor} - {puntaje}/10")
                    
        elif opcion == "3":
            print("salir")
            guardar_lista_en_archivo(ARCHIVO, lista_libros) 
            salir = True
        else:
            print("La opción es incorrecta")



if __name__=="__main__":
    main()
    
    
    
    
    