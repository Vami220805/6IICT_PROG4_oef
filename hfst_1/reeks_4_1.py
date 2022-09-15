# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.

# Deze websites geven meer info over de verschillende methodes van strings:
# https://www.w3schools.com/python/python_ref_list.asp
# https://www.programiz.com/python-programming/methods/list

def laatste_element(lijst):
    """ return het laatste element uit een lijst """
    return lijst[-1]

# print( laatste_element([3]) )
# print( laatste_element([1, 2, 3, 4, 5]) )
# print( laatste_element([2, 6, 8, 23, 12, 2]) )

def som_lijst(lijst):
    """ return de som van alle getallen uit een lijst """
    return sum(lijst)

# print( som_lijst([3]) )
# print( som_lijst([1, 2, 3, 4, 5]) )
# print( som_lijst([2, 6, 8, 23, 12, 2]) )

def gemiddelde_lijst(lijst):
    """ return het gemiddelde van alle getallen uit een lijst """
    som = sum(lijst)
    aantal_karakters = len(lijst)
    print (aantal_karakters)
    gemiddelde= som / aantal_karakters
    return gemiddelde

# print( gemiddelde_lijst([3]) )
# print( gemiddelde_lijst([1, 2, 3, 4, 5]) )
# print( gemiddelde_lijst([2, 6, 8, 23, 12, 2]) )

def min_max_lijst(lijst):
    """ return het minimum en het maximum van alle getallen uit een lijst
    
        >>> print( berekeningen([2, 6, 8, 23, 12, 2]) ) --> (2, 23)
    """
    return min(lijst), max(lijst)

# print( min_max_lijst([3]) )
# print( min_max_lijst([1, 2, 3, 4, 5]) )
# print( min_max_lijst([2, 6, 8, 23, 12, 2]) )


def kwadraat_lijst(lijst):
    """ return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst
        >>> print( squared_list([2,3]) ) --> [4, 9]
    """
    kwadraten_lijst = []
    for i in lijst:
        kwadraat = i **2
        kwadraten_lijst.append(kwadraat)
    return kwadraten_lijst

# print( kwadraat_lijst([3]) )
# print( kwadraat_lijst([1, 2, 3, 4, 5]) )
# print( kwadraat_lijst([2, 6, 8, 23, 12, 2]) )


def verschil_lijst(lijst_1, lijst_2):
    """ return een nieuwe lijst met alle getallen die lijst_1 en lijst_2 niet gemeen hebben """

    lijst_verschil=[]
    for element in lijst_1:
        if element not in lijst_2:
                if element not in lijst_verschil:
                    lijst_verschil.append(element)

    for element in lijst_2:
        if element not in lijst_1:
                if element not in lijst_verschil:
                    lijst_verschil.append(element)
    return lijst_verschil

# print( verschil_lijst([0], [0]) )
# print( verschil_lijst([2, 2, 4], [1, 1, 1]) )
# print( verschil_lijst([1, 2, 3, 4, 5], [2, 6, 8, 23, 12, 2]) )

def oneven_getallen(x):
    """ return een lijst met de eerste 'x' oneven getallen.
    
        >>> print( oneven_getallen(5) ) --> [1, 3, 5, 7 , 9]
    """
    getal = 1 
    oneven_lijst= []
    for i in range(x):
        oneven_lijst.append(getal)
        getal =getal+2
    return oneven_lijst

# print( oneven_getallen(5) )
# print( oneven_getallen(9) )
# print( oneven_getallen(2) )

def draai_om(lijst):
    """ return de lijst waarbij alle elementen omgewisseld zijn. """
    lengte= len(lijst)
    nieuwe_lijst= []
    for i in range(lengte):
        nieuwe_lijst.append(lijst[-i-1])
    return nieuwe_lijst

# print( draai_om([0]) )
# print( draai_om([1, "k", 3, 4, 5]) )
# print( draai_om([2, 6, 8, "v", 12, 2]) )

def sorteer(lijst): 
    """ return de lijst met de getallen gesorteerde van hoog naar laag. """
    lijst.sort()
    return lijst

# print( sorteer([0]) )
# print( sorteer([1, 5, 3, 4, 5]) )
# print( sorteer([2, 6, 8, 23, 12, 2]) )