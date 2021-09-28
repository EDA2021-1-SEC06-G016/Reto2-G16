"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos######################################################################################


###EMPIEZA EJEMPLO
def newCatalog():
    
    catalog = {'books': None,
               'bookIds': None,
               'authors': None,
               'tags': None,
               'tagIds': None,
               'years': None}
    
    catalog['books'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['bookIds'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapBookIds)
    
    catalog['tags'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareTagNames)
    return catalog
###TERMINA EJEMPLO


def newCatalog():

    catalog = {}
# Funciones para agregar informacion al catalogo#####################################################################
###EMPIEZA EJEMPLO
def addBookTag(catalog, tag):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    bookid = tag['goodreads_book_id']
    tagid = tag['tag_id']
    entry = mp.get(catalog['tagIds'], tagid)

    if entry:
        tagbook = mp.get(catalog['tags'], me.getValue(entry)['name'])
        tagbook['value']['total_books'] += 1
        tagbook['value']['count'] += int(tag['count'])
        book = mp.get(catalog['bookIds'], bookid)
        if book:
            lt.addLast(tagbook['value']['books'], book['value'])
###TERMINA EJEMPLO 


"Aquí empieza el CODE"
# Funciones para creacion de datos############################################################################


###EMPIEZA EJEMPLO

###TERMINA EJEMPLO 


"Aquí empieza el CODE"

# Funciones de consulta#######################################################################################


###EMPIEZA EJEMPLO
def getBooksByAuthor(catalog, authorname):
    """
    Retorna un autor con sus libros a partir del nombre del autor
    """
    author = mp.get(catalog['authors'], authorname)
    if author:
        return me.getValue(author)
    return None

def booksSize(catalog):
    """
    Número de libros en el catago
    """
    return lt.size(catalog['books'])
###TERMINA EJEMPLO 


"Aquí empieza el CODE"
# Funciones utilizadas para comparar elementos dentro de una lista###########################


###EMPIEZA EJEMPLO
def compareMapBookIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
###TERMINA EJEMPLO 


"Aquí empieza el CODE"
# Funciones de ordenamiento##############################################


###EMPIEZA EJEMPLO

###TERMINA EJEMPLO 


"Aquí empieza el CODE"