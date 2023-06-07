"""
Bepaal recursief de som van alle elementen in een lijst.
De lijst bestaat uit veel verschillende niveau's.
"""


def som_lijst(lijst):
    som =0
    for i in lijst:
        if type(i) == list:
            som = som + som_lijst(i)
        if type(i) == int:
            som = som +i 

    return som

print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10
