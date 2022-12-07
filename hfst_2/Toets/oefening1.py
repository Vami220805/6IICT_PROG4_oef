""" Algemeen (gaat over oefening 1 en 2): (  / 2)
Schrijf bij iedere regel code commentaar (  / 1)
Zorg dat de code geen geeft foutmeldingen (  / 1)
    Opgelet! Code in commentaar wordt niet bekeken.
"""
import json

""" OEFENING 1: (  / 5)
oefening1.json bevat info over Warren Buffett.
Dit is een zeer bekende investeerder.
"""

""" STAP 1: (  / 1)
laad oefening1.json in Python. Zet deze dictionary in een variabele.
Gebruik voor beide delen de JSON-module van Python.

Lukt dit niet? Dan mag je de dictionary rechtstreeks in de variabele plakken.
               Je krijgt dan wel geen punten voor dit onderdeel.
"""

fp = open("hfst_2/Toets/oefening1.json", "r") #open het bestand via het pad in read modus
dic = json.load(fp)#lees het json bestand en zet het om naar een python dictionary
fp.close()  # Na sluiten is JSON niet meer bruikbaar

""" STAP 2: (  / 1)
print volgende zaken van Warren Buffett in een grote f-string:
    - voornaam
    - geboortedatum
    - bedrijf
    - 1 hobby (bvb. deze op index 3)

Je moet deze info uit de dictionary halen (dus niet manueel invullen).

De print kan er als volgt uit zien:
Warren is geboren op 03-08-1930. Hij is de eigenaar van Berkshire Hathaway. Hiernaast speelt hij ook ukelele.
"""
naam = dic["voornaam"] #naam is de value van key voornaam in dic
datum = dic["geboortedatum"]#datum is de value van key geboordatum in dic
bedrijf = dic["bedrijf"]#bedrijf is de value van key bedrijf in dic
hobby = dic["hobbys"][0]#hobby is de 1ste value(0de index) van de key hobbys(list) in dic

print(f"{naam} is geboren op {datum}. Hij is eigenaar van {bedrijf}. In zijn vrije tijd doet {naam} veel {hobby}.")#print het resultaat in een f string

""" STAP 3: (  / 2)
Gebruik code om het minimale en maximale vermogen in de laatste 5 jaar (2017-2021) te bepalen.
Ook als de cijfers van het vermogen zouden wijzigen, moet de code blijven werken.
    Tip: je kan de functies min() en max() toepassen op lijsten. Dit geeft de kleinste/grootste waarde terug.

Lukt dit niet? Dan mag je het minimale en maximale vermogen zelf bepalen.
               Je krijgt dan wel slechts een deel van de punten voor dit onderdeel

Voeg dit minimale en maximale vermogen toe als value aan de hoofddictionary. 
Gebruik hiervoor de keys verm_min en verm_max.
"""
vermogen = dic["vermogen_in_miljard"]#zet de dictionary van het vermogen in dic naar variabele vermogen

min_key =min(vermogen, key=vermogen.get) #min vermogen van dict vermogen, iedere waarde wordt vergeleken met elkaar d.m.v. de key vermogen.get
max_key =max(vermogen, key=vermogen.get) #max vermogen van dict vermogen, iedere waarde wordt vergeleken met elkaar d.m.v. de key vermogen.get
#deze twee functies returnen het jaar wanneer deze waardes gebeurden, daarom wordt hieronder weer de key gezocht van het jaar
dic["Maximum vermogen"] = vermogen[max_key]#voeg key max vermogen toe aan dic met value max waarde
dic["Minimum vermogen"] = vermogen[min_key]#voeg key min vermogen toe aan dic met value min waarde

""" STAP 4: (  / 1)
Schrijf de gewijzigde dictionary weg naar een NIEUW JSON-bestand.
Bijvoorbeeld oefening1_resultaat.json .
"""
fp = open("hfst_2/toets_oef1.json", "w")#schrijf een nieuw json bestand
json.dump(dic, fp)#dump de python dictonary terug weer naar een json bestand
fp.close() # Na sluiten is JSON niet meer bruikbaar