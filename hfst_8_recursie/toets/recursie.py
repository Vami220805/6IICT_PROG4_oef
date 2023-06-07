"""
Gebruik recursie om een machtsberekening uit te voeren.
Je mag tijdens deze oefening geen gebruik maken van **, pow() of soortgelijke functies.

Tip: de base case is wanneer exponent == 1. Wat is dan de return waarde?
"""
def bepaal_macht(getal, exponent):
    if exponent == 1:
        return getal
    return getal * bepaal_macht(getal, exponent -1 )



print( bepaal_macht(2, 3) ) # 2**3 = 8
print( bepaal_macht(9, 3) ) # 9**3 = 729
print( bepaal_macht(3, 1) ) # 3**1 = 3