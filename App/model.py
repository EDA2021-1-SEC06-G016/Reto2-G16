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
def newCatalog():
    catalog = {'artists': None,  #books->artist
               'artworks': None,
               'mapMedium':None}    #authors->artworks

    catalog['artists'] = lt.newList("ARRAY_LSIT") #USANDO "type" con el código comentado en vez del tipo de lista
    catalog['artworks'] = lt.newList("ARRAY_LSIT")
    catalog['mapMedium'] = mp.newMap(numelements=1000, maptype='PROBING',loadfactor=0.5,comparefunction=compareMediums)
    return catalog


def compareMediums(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def addArtist(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo 
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'], 
    artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artists'], t)

def addArtwork(catalog, artwork):
    """
    Adiciona un tag a la lista de tags
    """
    t = (artwork['ObjectID'], artwork['Title'], artwork['ConstituentID'], #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'], 
    artwork['CreditLine'], artwork['AccessionNumber'], artwork['Classification'], 
    artwork['Department'], artwork['DateAcquired'], artwork['Cataloged'], 
    artwork['URL'], artwork['Circumference (cm)'], artwork['Depth (cm)'], 
    artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], 
    artwork['Weight (kg)'], artwork['Width (cm)'], artwork['Seat Height (cm)'], 
    artwork['Duration (sec.)'])
    lt.addLast(catalog['artworks'], t)

#Todo
    medium = artwork['Medium']
    esta = mp.contains(catalog['mapMedium'], medium)
    if( esta == True):
        #*["value"] solo retorna el value, y no la pareja llave valor
        lista = mp.get(catalog['mapMedium'],medium)["value"]
        lt.addLast(lista,artwork)
        #!map llave valro con lista
        mp.put(catalog['mapMedium'],medium,lista)

    else:
        #! repasar
        lista = lt.newList()
        lt.addLast(lista,artwork)
        mp.put(catalog['mapMedium'],medium,lista)
# Funciones para agregar informacion al catalogo
# Construccion de modelos


###EMPIEZA EJEMPLO
def newCatalog():
    
    catalog = {'books': None,
               'bookIds': None,
               'authors': None,
               'tags': None,
               'tagIds': None,
               'years': None}
    
    catalog['books'] = lt.newList('SINGLE_LINKED')
    catalog['bookIds'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None)
    
    catalog['tags'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=None)
    return catalog
###TERMINA EJEMPLO


def newCatalog():
    catalog = {'artists': None,  
               'artworks': None,
               "artistsID": None,
               "artworksID": None,
               "medium": None}

    catalog['artists'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None) 
    catalog['artworks'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None)

    catalog["artistsID"] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None)


    catalog["artworksID"] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=None)
    
    catalog["medium"] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0)
    return catalog
# Funciones para creación de datos ##########################################################################


# Funciones para agregar informacion al catalogo#####################################################################
###EMPIEZA EJEMPLO

###TERMINA EJEMPLO 

#PARA CAMBIAR DEBIDO A LOS MAPS#//
def addArtist(catalog, artist):
    """
    Agrega una relación entre un libro y un tag.
    Para ello se adiciona el libro a la lista de libros
    del tag.
    """
    artistID = catalog['ConstituentID']
    entry = mp.contains(catalog['ConstituentID'], artistID)
    newartist = (artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo 
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'], 
    artist['Wiki QID'], artist['ULAN'])

    if entry == False:
       mp.put(catalog["artists"], artist["ConstituentID"], newartist)
    
#########para eliminar
"""
def addArtist(catalog, artist):
    
    
    t = (artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo 
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'], 
    artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artists'], t)
"""
def addArtwork(catalog, artwork):

    artistID = catalog['ObjectID']
    entry = mp.contains(artwork['ObjectID'], artistID)
    newartwork = ((artwork['ObjectID'], artwork['Title'], artwork['ConstituentID'], #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'], 
    artwork['CreditLine'], artwork['AccessionNumber'], artwork['Classification'], 
    artwork['Department'], artwork['DateAcquired'], artwork['Cataloged'], 
    artwork['URL'], artwork['Circumference (cm)'], artwork['Depth (cm)'], 
    artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], 
    artwork['Weight (kg)'], artwork['Width (cm)'], artwork['Seat Height (cm)'], 
    artwork['Duration (sec.)']))

    if entry == False:
       mp.put(catalog["artists"], artwork['ObjectID'], newartwork)
###para eliminar
"""
def addArtwork(catalog, artwork):
    
    t = (artwork['ObjectID'], artwork['Title'], artwork['ConstituentID'], #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'], 
    artwork['CreditLine'], artwork['AccessionNumber'], artwork['Classification'], 
    artwork['Department'], artwork['DateAcquired'], artwork['Cataloged'], 
    artwork['URL'], artwork['Circumference (cm)'], artwork['Depth (cm)'], 
    artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'], 
    artwork['Weight (kg)'], artwork['Width (cm)'], artwork['Seat Height (cm)'], 
    artwork['Duration (sec.)'])
    lt.addLast(catalog['artworks'], t)
"""
###Obviar esto, es para adelantar lo del medium
"""
def artistID(catalog, artists, name):
    artists = catalog['artists']
    existname = mp.contains(artists, existname)
    if existname:
        entry = mp.get(artists, existname)
        artist = me.getValue(entry)
    else:
        author = newAuthor(authorname)
        mp.put(authors, authorname, author)
    lt.addLast(artists['DisplayName'], book)

    totbooks = lt.size(author['books'])
"""   
    
# Funciones para creacion de datos############################################################################


###EMPIEZA EJEMPLO

###TERMINA EJEMPLO 


"Aquí empieza el CODE"

# Funciones de consulta#######################################################################################


###EMPIEZA EJEMPLO
"""
def getBooksByAuthor(catalog, authorname):
    
    author = mp.get(catalog['authors'], authorname)
    if author:
        return me.getValue(author)
    return None

def booksSize(catalog):
    
    return lt.size(catalog['books'])
"""
###TERMINA EJEMPLO 


"Aquí empieza el CODE"
# Funciones utilizadas para comparar elementos dentro de una lista###########################


###EMPIEZA EJEMPLO
"""
def compareMapBookIds(id, entry):
    
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1
"""
###TERMINA EJEMPLO 


"Aquí empieza el CODE"
# Funciones de ordenamiento##############################################


###EMPIEZA EJEMPLO

###TERMINA EJEMPLO 


"Aquí empieza el CODE"