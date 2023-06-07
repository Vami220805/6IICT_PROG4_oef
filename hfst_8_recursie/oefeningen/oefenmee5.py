""" Niveau 1: los omdraaien van woord recursief op """

def draaiom(woord):
    if len(woord) == 0:
        return woord
    else:
        return draaiom(woord[1:]) + woord[0]



# print( draaiom("Hallo") )       # ollaH
# print( draaiom("Dag") )         # gaD
# print( draaiom("f"))            # f
# print( draaiom("Iedereen") )    # neeredeI

""" Niveau 2: los omdraaien van woord met while-loops op """

def draaiom_while(woord):
    while True:
        if len(woord) == 0: 
            return woord
        else:
            return woord[1:] + woord[0]


print( draaiom_while("Hallo") )       # ollaH
print( draaiom_while("Dag") )         # gaD
print( draaiom_while("f"))            # f
print( draaiom_while("Iedereen") )    # neeredeI