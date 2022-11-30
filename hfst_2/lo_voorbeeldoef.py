""" Algemeen:
Schrijf bij iedere regel code commentaar 
De code mag geen foutmeldingen geven
    Opgelet! Code in commentaar wordt niet bekeken.
"""
import json, random

""" 
lo_voorbeeldoefening.json bevat info over het schaakstuk "toren".
"""

""" STAP 1:
laad lo_voorbeeldoefening.json in Python. Zet deze dictionary in een variabele.

Lukt dit niet? Dan mag je de dictionary rechtstreeks hieronder plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""
fp = open("hfst_2/lo_voorbeeldoefening.json", "r")
dic = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

""" STAP 2:
print volgende zaken over de toren:
    - De naam zelf (toren)
    - Hoeveel pionnen deze waard is (5)
    - 1 van de beweging die het kan maken (bvb. boven)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).
"""

for key in dic:
    print(key)
print(dic["toren"]["waarde_pionnen"])
print(dic["toren"]["beweging"][random.randint(0,3)])

""" STAP 3:
Voeg volgende zaken toe aan de dictionary (links staat de key, rechts de value):
    - engelse_naam: rook
    - andere_namen: ["Toring", "Torra", "Rukhkh", "Top"]

"""

dic["toren"]["engelse_naam"] = "rook"
dic["toren"]["andere_naam"]= ["Toring", "Torra", "Rukhkh", "Top"]

""" STAP 4:
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld lo_voorbeeldresultaat.json .
"""
fp1 = open("hfst_2/lo_voorbeeldresultaat.json", "w")
json.dump(dic, fp1)
fp.close() # Na sluiten is JSON niet meer bruikbaar