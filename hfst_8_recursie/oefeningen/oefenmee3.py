""" Bepaal de faculteit van een getal met behulp van een while-loop. """
def facul(n):
    if n == 1:
        return 1
    
    vorige_faculteit = facul( n-1 )
    return n * vorige_faculteit

facul(3) # Faculteit van 3: 6