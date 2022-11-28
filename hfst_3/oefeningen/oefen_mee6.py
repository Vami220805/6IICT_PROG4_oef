fruit_lijst = ["Appel", "Banaan", "Kers"]

try:
    getal = input( "Geef een getal: " )
    if "." in getal:
        getal = float( getal )
    else:
        getal = int( getal )
    print( fruit_lijst[getal] )
except IndexError:
    print("Deze index is niet juist.")
except ValueError:
    print("Deze waarde is niet correct")
except TypeError:
    print("Deze waarde is verkeerd ingevoerd.")

# getal = input( "Geef een getal: " )
# if "." in getal:
#     getal = float( getal )
# else:
#     getal = int( getal )
# print( fruit_lijst[getal] )

print("Programma klaar")  
