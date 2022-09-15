# Maak onderstaande functies af.
# Testen kan MBV de oproepen onder iedere oefeningen.
# Tip: gebruik CTRL + / om meerdere lijnen in/uit commentaar te zetten.

# Deze websites geven meer info over de verschillende methodes van strings:
# https://www.w3schools.com/python/python_strings_methods.asp 
# https://www.programiz.com/python-programming/methods/string 

def aantal_karakters(zin):
    """ return het aantal letters in een zin """
    return len(zin)

# print( aantal_karakters("Hallo") )
# print( aantal_karakters("2 plus 2 is 4") )
# print( aantal_karakters("de kat krabt de krullen van de traf af.") )

def titel(zin):
    """ return de zin waarbij ieder woord een hoofdletter heeft
    
        >>> print( titel("de kat krabt") ) --> De Kat Krabt
    """
    zin1= zin.title()
    return zin1

# print( titel("de kat krabt") )
# print( titel("krullen van de trap af") )
# print( titel("ditisslechts1woord") ) 

def kort_af(woord):
    """ return de eerste, middelste en laatste karakter van een wokord 
    
        Indien het woord even is, return enkel het eerste en laatste karakter.
        >>> print( hoofdletter("krabt") ) --> kat
    """
    resultaat = []
    lengte = len(woord) 
    eerste_karakter= woord[0]
    resultaat.append(eerste_karakter)
    middelste_karakter = woord[(lengte//2)]
    if lengte %2 != 0:
        resultaat.append(middelste_karakter)
    laatste_karakter= woord[lengte-1]
    resultaat.append(laatste_karakter)
    return resultaat

# print( kort_af("krabt") )
# print( kort_af("belgie") )
# print( kort_af("mosa-rt") )

def vervang(woord, kar):
    """ return het aangepaste woord 
    
        Vervang ieder karakter kar door een uitroepteken.
        >>> print( vervang("katten", "t") ) --> ka!!en
    """
    nieuw_woord= woord.replace(kar, "!")
    return nieuw_woord

    # for index,karakter in enumerate(woord):
    #     if karakter == kar:
    #         karakter = "!"
# print( vervang("katten", "t") )
# print( vervang("de koetsier poetst de postkoets met postkoetspoets", "oe") )
# print( vervang("Nog een paar tongbrekers", "i") )

def is_laag(zin):
    """ return True of False (boolean!)
    
        True: de zin bevat enkel kleine letters.
        False: de zin bevat ook grote letters.
        >>> print( vervang("Dit is fout!") ) --> False
    """
    return zin.islower()

# print( is_laag("Dit is fout!") )
# print( is_laag("een twee drie vIer") )
# print( is_laag("een correcte zin") )

def is_getal(kar):
    """ return True of False (boolean!) 
    
        True: het karakter kar is een getal
        False: het karakter kar is geen getal.

        Indien True, voor de return, converteer str kar naar int.
        Print het kwadraat van de waarde.
        >>> print( is_getal("5") ) --> 25
                                   --> True
    """
    karakter=kar.isnumeric()
    if karakter ==True:
        getal= int(kar)
        kwadraat = getal **2
    return karakter, kwadraat


# print( is_getal("5")  )
# print( is_getal("e")  )
# print( is_getal("44") )

def draai_om(zin):
    """ return de zin met alle karakters omgedraaid. 

        >>> print( draai_om("Palindroom") ) --> moordnilaP
    """
    omgedraaide_zin = zin [::-1]
    return omgedraaide_zin

# print( draai_om("Palindroom")  )
# print( draai_om("de kat krabt")  )
# print( draai_om("racecar") )

def tel_klinkers(zin):
    """ return het aantal klinkers in een zin. 

        >>> print( tel_klinkers("De kat krabt") ) --> 3
    """
    klinkers = ["a","e","u","i","o"]
    aantal_klinkers=0
    for i in klinkers:
        aantal = zin.count(i)
        aantal_klinkers +=aantal
    return aantal_klinkers

# print( tel_klinkers("De kat krabt") )
# print( tel_klinkers("de krullen van de trap af") )
# print( tel_klinkers("Belgie") )