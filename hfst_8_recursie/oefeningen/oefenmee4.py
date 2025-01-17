""" Niveau 1: los sommatie recursief op """

def sommatie(n):   
    if n == 1:
        return n
    vorige = sommatie(n-1)
    return n + vorige


# print( sommatie(1) )   # 1
# print( sommatie(2) )   # 3
# print( sommatie(3) )   # 6
# print( sommatie(4) )   # 10
# print( sommatie(5) )   # 15
# print( sommatie(100) ) # 5050


""" Niveau 2: los sommatie met while-loops op """

def sommatie_while(n):
    uitkomst = 0
    while True:
        if n < 1:
            return uitkomst
        uitkomst +=n
        n -= 1


print( sommatie_while(4) )   # 10

