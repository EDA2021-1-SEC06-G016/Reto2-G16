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
    catalog = {'artists': None, #books->artist
               'artworks': None,
               'mapMedium':None,
               "mapNationality": None} #authors->artworks

    catalog['artists'] = mp.newMap(maptype="CHAINING", loadfactor= 2,comparefunction= compareArtistIds) #VÁLIDO "ARRAY_LIST/SINGLE_LINKED"
    catalog['artworks'] = mp.newMap(maptype="CHAINING", loadfactor= 2, comparefunction = compareArtworkIds)
    catalog['mapMedium'] = mp.newMap(1000, maptype='PROBING',loadfactor=0.5,comparefunction=compareMediums)
    catalog["mapNationality"] = mp.newMap(200, maptype='PROBING',loadfactor=0.5,comparefunction=compareNation)
    return catalog




def addArtist(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'],
    artist['Wiki QID'], artist['ULAN'])
    mp.put(catalog['artists'], artist['ConstituentID'], t)

#Indice nationality-artist
#TODO
def addNationality(catalog, nationality):
    artist = catalog["artists"]
    artwork = catalog["artworks"]
    nationality = artist["Nationality"]
    #IdArtist = artist["ConstituentID"]
    #IdArtwork = artwork["ConstituentID"]
    esta = mp.contains(catalog["mapNationality"], nationality)
    
    #sumar uno a la nacio
    
    if (esta == True): 
        pareja = mp.get(catalog["mapnationality"], nationality)
        valor = int(me.getValue(pareja)) + 1
        mp.put(catalog["mapNationality"], nationality, valor)
    
    else: #crear pareja llave-val e iniciar con 1
        
        mp.put(catalog["mapNationality"], nationality, 1)

def addArtwork(catalog, artwork):
    """
    Adiciona un tag a la lista de tags
    """
    t = (artwork['ObjectID'] , artwork['Title'],  #newArtwork al inicio
    artwork['Date'], artwork['Medium'], artwork['Dimensions'],
    artwork['CreditLine'], artwork['AccessionNumber'], artwork['Classification'],
    artwork['Department'], artwork['DateAcquired'], artwork['Cataloged'],
    artwork['URL'], artwork['Circumference (cm)'], artwork['Depth (cm)'],
    artwork['Diameter (cm)'], artwork['Height (cm)'], artwork['Length (cm)'],
    artwork['Weight (kg)'], artwork['Width (cm)'], artwork['Seat Height (cm)'],
    artwork['Duration (sec.)'])
    mp.put(catalog['artworks'],artwork['ConstituentID'],t)

#TODO
#Indice medium-artworks
    #medium = artwork['Medium']
    #esta = mp.contains(catalog['mapMedium'], medium)
    #if( esta == True):
    #    #*["value"] solo retorna el value, y no la pareja llave valor
    #    lista = mp.get(catalog['mapMedium'],medium)["value"]
    #    lt.addLast(lista,artwork)
    #    #!map llave valro con lista
    #    mp.put(catalog['mapMedium'],medium,lista)

    #else:
    #    #! repasar
    #    lista = lt.newList()
    #    lt.addLast(lista,artwork)
    #    mp.put(catalog['mapMedium'],medium,lista)

###Funciones de consulta

def artistsSize(catalog):
    return mp.size(catalog["artists"])

def artworksSize(catalog):
    return mp.size(catalog["artworks"])

def nationalitiesSize(catalog):
    return mp.size(catalog["mapNationality"])
#Añadir a indice de nacionalidad las obras por artista # NO HECHO, NO SE ENTIENDE
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