"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If wnot, see <http://www.gnu.org/licenses/>.
 """
import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

import csv
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catalogo....")
    print("2- Cargar catalogo...")
    print("3- Artistas en orden")
    print("4- Adquisiciones cronologicamente")
    print("5- Clasificar obras de un artista por tecnica")
    print("0- Salir")

def initCatalog(): #Va "typelist" como parametro
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = controller.initCatalog() 
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    controller.loadData(catalog)


    
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando catálogo ....")
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        inicio = time.time()
        print("Cargando información de los archivos ....")
        catalog =controller.loadData(cont)
        #Cantidad artistas   
        print('Artistas cargados: ' + str(controller.artistsSize(cont)))
        #Cantidad obras
        print('Obras cargadas: ' + str(controller.artworksSize(cont)))
        #Cantidad nacionalidades
        print("Nacionalidades cargadas: " + str(controller.nationalitiesSize(cont)))
        fin = time.time()
        timeex = round((fin-inicio), 2)
        print("Tiempo de ejecución de carga de datos " + str(timeex))
    elif int(inputs[0]) == 3:
        initano = input("Escriba un año inicial: ")
        endano = input("Escriba un año final: ")
        func = controller.namefunct(catalog, parameters)
        print(func)
    elif int(inputs[0]) == 4:
        inidate = input("Escriba una fecha inicial: ")
        enddate = input("Escriba una fecha final: ")
        func = controller.namefunct(catalog, parameters)
        print(func)
    elif int(inputs[0]) == 5:
        name = input("Escriba el nombre del artista: ")
        func = controller.namefunct(catalog, parameters)
        print(func)
    else:
        sys.exit(0)
sys.exit(0)