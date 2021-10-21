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

import time
from DISClib.DataStructures.singlelinkedlist import newList
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

######################sssssssssssssssssss

def newCatalog():
    catalog = {'artists': None,
                "artistsID": None, #books->artist
               'artworks': None,
               "artworksID": None,
               'mapMedium':None,
               "mapNationality": None} #authors->artworks

    catalog['artists'] = mp.newMap(2000, maptype="CHAINING", loadfactor= 2,comparefunction= compareBeginDates) #VÁLIDO "ARRAY_LIST/SINGLE_LINKED"
    catalog['artistsID'] = mp.newMap(2000, maptype="CHAINING", loadfactor= 2,comparefunction= compareArtistIds)
    catalog['artworks'] = mp.newMap(2000, maptype="CHAINING", loadfactor= 2, comparefunction = compareArtworkIds)
    catalog['artworksID'] = mp.newMap(2000, maptype="CHAINING", loadfactor= 2, comparefunction = compareArtworkIds)
    catalog['mapMedium'] = mp.newMap(1000, maptype='PROBING',loadfactor=0.5,comparefunction=compareMediums)
    catalog["mapNationality"] = mp.newMap(200, maptype='PROBING',loadfactor=0.5,comparefunction=compareNation)
    return catalog




def addArtist(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['DisplayName'], artist['BeginDate'],  artist['EndDate'], #newArtist al inicio si algo
    artist['Nationality'], artist['Gender'])
    mp.put(catalog['artists'],artist['BeginDate'], t)

def addArtistID(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'],
    artist['Wiki QID'], artist['ULAN'])
    mp.put(catalog['artistsID'],artist['ConstituentID'], t)

#TODO VERIFICAR CÓMO DEJAR ARTWORKS PARA REQ 2
def addArtwork(catalog, artwork):
    """
    Adiciona un tag a la lista de tags
    """
    artistas = None
    t = (artwork['Title'], artistas, #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'],
    artwork['CreditLine'])
    mp.put(catalog['artworks'],artwork['DateAcquired'],t)

# BUSCAR EN CREDIT LINE = "PURCHASE"
def addArtworkID(catalog, artwork):
    """
    Adiciona un tag a la lista de tags
    """
    artistas = None
    t = (artwork['Title'], artistas, #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'],
    artwork['CreditLine'])
    mp.put(catalog['artworksID'],artwork['ConstituentID'],t)
#Indice nationality-artist
#TODO natio
def addNationality(catalog, artist, artwork):
    """
    Adiciona nacionalidades por key
    """
    x = (artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo
    artist['Gender'], artist['BeginDate'], artist['EndDate'],
    artist['Wiki QID'], artist['ULAN'])
    mapArtistNat = mp.newMap()
    if mp.get(mapArtistNat, artist["Nationality"]) == True:
        mp.put(catalog['mapNationality'],artist["Nationality"] , ++1)
    else:
        mp.put(mapArtistNat, artist["Nationality"], 1)

    mapArtwNat = mp.newMap()
    

#TODO medium
def addMedium(catalog, artwork, artist):
    """
    Adiciona un tag a la lista de tags
    """
    ID = mp.get(catalog['artworksID'],artwork["ConstituentID"])
    esta = mp.contains(catalog["artists"], ID)
    if esta == True:
        ID2= mp.put(catalog["mapMedium"], artwork["medium"], )

    ID2 = mp.put(catalog["artists"], ID)

    artistas = None
    t = (artwork['Title'], artistas, #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'],
    artwork['CreditLine'])
    mp.put(catalog['artworksID'],artwork['ConstituentID'],t)

###Funciones de consulta

def artistsSize(catalog):
    return mp.size(catalog["artists"])

def artworksSize(catalog):
    return mp.size(catalog["artworks"])

def nationalitiesSize(catalog):
    return mp.size(catalog["mapNationality"])

def sortBeginDates(lst, cmpfunction):
    n = lt.size(lst)
    h = 1
    while h < n/3:   # primer gap. La lista se h-ordena con este tamaño
        h = 3*h + 1
    while (h >= 1):
        for i in range(h, n):
            j = i
            while (j >= h) and cmpfunction(
                                lt.getElement(lst, j+1),
                                lt.getElement(lst, j-h+1)):
                lt.exchange(lst, j+1, j-h+1)
                j -= h
        h //= 3    # h se decrementa en un tercio
    return lst

#TODO func generica
def getLast3 (rangecat): #Últimas 3
    lastsartworks = mp.newMap()
    u = mp.size(rangecat["artwork"])
    for i in range(u-2, u+1): #revisar rango
        firstartwork = lt.getElement(rangecat["artwork"], i)
        secondartwork = lt.getElement(rangecat["artwork"], i)
        thirdartwork = lt.getElement(rangecat["artwork"], i)
        lt.addLast(lastsartworks, firstartwork)
        lt.addLast(lastsartworks, secondartwork)
        lt.addLast(lastsartworks, thirdartwork)
    return lastsartworks
#TODO func generica
def getFirst3 (rangecat): #Primeras 3 
    firstsartworks = mp.newMap()
    for i in range(1,4):
        firstartwork = lt.getElement(rangecat["artwork"], i)
        secondartwork = lt.getElement(rangecat["artwork"], i)
        thirdartwork = lt.getElement(rangecat["artwork"], i)
        lt.addLast(firstsartworks, firstartwork)
        lt.addLast(firstsartworks, secondartwork)
        lt.addLast(firstsartworks, thirdartwork)
    return firstsartworks

def topmed(catalog,x):
    artwork = catalog["artworks"]
    artw = artwork["Medium"]
    med = artw["Medium"]
    esta = mp.contains(catalog["mapMedium"], med)
    if esta == True:
        list = mp.valueSet(catalog["mapMedium"], med)
        n = int(len(list))
        gap = int(n/2)
  
        while gap > 0:
            for i in range(int(gap),int(n)):
                temp = list[i]
                j = i
                while  j >= gap and list[j-gap]['DateAcquired'] >temp['DateAcquired']:
                    list[j] = list[j-gap]
                    j -= gap
                list[j] = temp
            gap /= 2
        return lt.getElement(list, x)
    else:
        print("El medio no se encuentra en el catalogo, seleccione uno disponible")

######################Funciones de comparación

def compareBeginDates(id, entry):
    """
    Compara begdates
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return - 1
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

def compareNation(keyname, nationality):
    """
    Compara dos nacionalidades de obra. El primero es una cadena
    y el segundo un entry de un map
    """
    natentry = me.getKey(nationality)
    if (keyname == natentry):
        return 0
    elif (keyname > natentry):
        return 1
    else:
        return -1

def compareArtistIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareArtworkIds(id, entry):
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

# Construccion de modelos######################################################################################