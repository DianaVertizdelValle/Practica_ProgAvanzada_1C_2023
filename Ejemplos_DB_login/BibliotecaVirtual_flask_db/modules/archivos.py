# -*- coding: utf-8 -*-

def cargar_lista_desde_archivo(nombre_archivo, lista_libros):
    """Función para ....

    Args:
        nombre_archivo (str): _description_
        lista_libros (list): _description_
    """
    with open(nombre_archivo, "r") as archi:
        for linea in archi:
            lista_libro = linea.rstrip().split(',')
            libro = {
                "nombre": lista_libro[0],
                "autor": lista_libro[1],
                "puntaje": lista_libro[2] 
            }
            lista_libros. append(libro)   

def guardar_lista_en_archivo(nombre_archivo, lista_libros):  
    with open(nombre_archivo, "w", encoding="utf-8") as archi:                
        for libro in lista_libros:
            nombre = libro["nombre"]
            autor = libro["autor"]
            puntaje = libro["puntaje"]
            archi.write(nombre + "," + autor + "," + puntaje + "\n" )   

def guardar_libro_en_archivo(nombre_archivo, libro):
    
    with open(nombre_archivo, "a") as archi:
        archi.write(f"{libro['nombre']},{libro['autor']},{libro['puntaje']}\n")