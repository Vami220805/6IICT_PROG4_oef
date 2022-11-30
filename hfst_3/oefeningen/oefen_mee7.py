""" Niveau 1 """
num_lijst = [ 100, 101, 0, "103", 104 ]
try:
    index = input( "Geef een index: " )
    if "." in index:
        index = float( index )
    else:
        index = int( index )
except ValueError:
    print("Deze waarde is niet correct") 
except KeyboardInterrupt:
    print("Programma onderbroken.")
else:
    try:
        print( f"100 / {num_lijst[index]} = {100/num_lijst[index]}" ) 
    except TypeError:
        print("Deze waarde is verkeerd ingevoerd.")   
    except ZeroDivisionError:
        print("Deze berekening werkt niet.")
    except IndexError:
        print("Deze index werkt niet.")

""" Niveau 3 (haal uit commentaar) """
print( "Geldig getal als index opgegeven." )
