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
inicio = time.time()
def newCatalog():
    catalog = {'artists': None, #books->artist
               'artworks': None,
               'mapMedium':None,
               "mapNationality": None} #authors->artworks

    catalog['artists'] = lt.newList("ARRAY_LSIT") #USANDO "type" con el código comentado en vez del tipo de lista
    catalog['artworks'] = lt.newList("ARRAY_LSIT")
    catalog['mapMedium'] = mp.newMap(numelements=1000, maptype='PROBING',loadfactor=0.5,comparefunction=compareMediums)
    catalog["mapNationality"] = mp.newMap(numelements=1000, maptype='PROBING',loadfactor=0.5,comparefunction=compareNation)
    return catalog
fin = time.time()
timeex = round((fin-inicio), 2)
print("Tiempo de ejecución de crga de datos " + str(timeex))

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

def addArtist(catalog, artist):
    """
    Adiciona un artist a la lista de artists
    """
    t = (artist['ConstituentID'], artist['DisplayName'], artist['ArtistBio'], #newArtist al inicio si algo
    artist['Nationality'], artist['Gender'], artist['BeginDate'], artist['EndDate'],
    artist['Wiki QID'], artist['ULAN'])
    lt.addLast(catalog['artists'], t)

#Indice nationality-artist
    nationality = artist["Nationality"]
    esta = mp.contains(catalog["mapNationality"], nationality)
    if (esta == True):
        lista = mp.get(catalog["mapNationality"], nationality)
        lt.addLast(lista, artist)
        
        mp.put(catalog["mapNationality"], nationality, lista)
    
    else:
        lista = lt.newList()
        lt.addLast(lista, artist)
        mp.put(catalog["mapNationality"], nationality, lista)

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

#Indice medium-artworks
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

#Añadir a indice de nacionalidad las obras por artista # NO HECHO, NO SE ENTIENDE
  
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

######################ssssssssssssssssssss

# Construccion de modelos######################################################################################