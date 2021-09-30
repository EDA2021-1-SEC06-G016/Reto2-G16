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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

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
    print("1- Cargar información en el catálogo.")
    print("2- Las n obras más antiguas para un medio específico")
    print("ant2 3real- REQ2/GRUPAL/- Ordenar catalogo de obras por año de adquisición-PARARETO NO SE HA EMPEZADO")
    print("4- Clasificar obras de un artista por tecnica-PARARETO NO SE HA EMPEZADO")
    print("5- Clasificar obras por nacionalidad de creadores-PARARETO NO SE HA EMPEZADO")
    print("6- Transportar obras de un departamento-PARARETO NO SE HA EMPEZADO")
    print("ant6 7real- REQ6/BONO/- Proponer un nueva exposición en el museo-PARARETO NO SE HA EMPEZADO")
    print("0- Salir")

def initCatalog(): #Va "typelist" como parametro
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = controller.newCatalog() 
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtists(catalog):
    """
    Carga los libros del archivo. Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artistsfile = cf.data_dir + 'GoodReads/Artists-utf8-small.csv' #para cambiar el archivo
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        controller.addArtist(catalog, artist)

def loadArtworks(catalog):
    """
    Carga los libros del archivo. Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    artworksfile = cf.data_dir + 'GoodReads/Artworks-utf8-small.csv' #para cambiar el archivo
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artwork in input_file:
        controller.addArtwork(catalog, artwork)

    
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()   
        loadData(catalog)

        print('Artistas cargados: ' + str(lt.size(catalog['artists'])))
        #books -> artist 
        print('Obras cargadas: ' + str(lt.size(catalog['artworks'])))
        #authors->artwork
    elif int(inputs[0]) == 2:
        x = input("Número de obras más antiguas: ")
        func = controller.topmed(catalog, artwork,x)
        print(func)