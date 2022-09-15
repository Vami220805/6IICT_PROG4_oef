from random import random


def maak_rij_nul(breedte):
    """ return een lijst gevuld met nullen van de gegeven breedte
    
        breedte: het aantal nullen in een lijst

        >>> print( maak_rij_nul(3) ) --> [0, 0, 0]
    """
    lijst_nullen=[]
    for i in range(breedte):
        lijst_nullen.append(0)
    return lijst_nullen


def maak_veld_nul(hoogte, breedte):
    """ return een geneste lijst met grootte hoogte x breedte

        hoogte: het aantal lege lijsten dat gemaakt moet worden.
        breedte: het aantal nullen in iedere lege lijst.

        >>> print( maak_veld_nul(2,3) ) --> [
                                             [0, 0, 0],
                                             [0, 0, 0]
                                            ]

        Tip: Maak de geneste lijst door maal_rij_nul op te roepen.
             Het aantal oproepen is gelijk aan de waarde van hoogte.
             Zie ook reeks_4 voor het invoegen van een lijst in een lijst.
    """
    geneste_lijst = []
    for i in range(hoogte):
        lijst_aantal_nullen=maak_rij_nul(breedte)
        geneste_lijst.append(lijst_aantal_nullen)
    return geneste_lijst


def maak_veld_nul_levend(veld, kans_levend):
    """ return een veld, waarbij een aantal van de cellen een waarde 1 bevatten 
    
        veld: het veld bekomen uit maak_veld_nul.
        kans_levend: de kans (tussen 0 en 1) die een cel heeft om waarde 1 te krijgen.

        Overloop alle cellen in de geneste lijst. Een aantal van deze cellen moet 
        waarde 1 krijgen. Om te bepalen welke gebruik je kans_levend en de random module.

        veld = [
                [0, 0, 0],
                [0, 0, 0]
               ]

        >>> print( maak_veld_nul_levend(veld, 1  ) ) --> [
                                                          [1, 1, 1],
                                                          [1, 1, 1]
                                                         ]
        >>> print( maak_veld_nul_levend(veld, 0.5) ) --> [
                                                          [1, 0, 1],
                                                          [9, 0, 1]
                                                         ]
    """
    for rij in veld:
        print (len(rij))
        for i in range(len(rij)):
            del rij[i]
            if 1 >= kans_levend:
                rij.insert(i,0)
            else:
                rij.insert(i,1)
    return veld
print(maak_veld_nul_levend(maak_veld_nul(3, 3), 1))



