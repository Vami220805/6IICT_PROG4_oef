try:
    getal = int( input("Geef een getal in: ") )
    deling_10 = 10/getal

    print(f"10 gedeeld door {getal} is gelijk aan {deling_10}")

except ValueError:
    print("Er is geen correct getal ingevoerd.")
