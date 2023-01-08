""" Oefening 1 (  / 2)
Maak onderstaande opdrachten over dictionaries.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Print voor IEDER element in onderstaande dictionary volgende tekst:
    <key> heb ik <value> uren per week

Voorbeeld:
    wisk heb ik 4 uren per week
    ...
    sph heb ik 2 uren per week
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}

for key,value in vakken.items():#doorloop de dictonary en neem hiervan de key en de value
    print(f"{key} heb ik {value} uren per week")#print de huidige key en value in een f string om een zin te krijgen

""" Opdracht 2:
Vraag de gebruiker naar een vak. Print het aantal uur dat dit vak voorkomt in de dictionary.
Als het ingegeven vak niet bestaat, print dan "vak bestaat niet".

VOORBEELD:
    Geef een vak op: wisk
    4

    Geef een vak op: huppel
    vak bestaat niet
"""
vakken = {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}

vak = input("Geef een vak op: ")#vraag aan de gebruiker om een vak op te geven
if vak in vakken:#als het opgegeven vak in de dictonary zit
    print(vakken.get(vak))#print de value van dit vak (oftewel het aantal uren)
else: #als het opgegeven vak niet in de dictonary zit
    print("vak bestaat niet")#print dat het vak niet bestaat

""" Opdracht 3:
Schrijf een programma dat onderstaande 2 lijsten combineert in een dictionary.
print deze dictionary. Opgelet! Dit programma moet ook blijven werken als de lijsten wijzigen.
                                De lijsten zullen wel altijd evenveel elementen bevatten.

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
namen = ["wisk", "prog", "cosn", "sph"]
uren = [4,4,2,2]

dict = {}#lege dictonary
for index, element in enumerate(namen):#doorloop de lijst namen en neem de index en het element ervan met de functie enumerate()
    if element not in dict:#als huidig element niet al in de dict zit
        dict[element]= uren[index]#voeg element toe met als value het aantal uren op dezelfde index
print(dict)#print de dictonary

""" Opdracht 4:
Verander in onderstaande dictionary de key "error" naar "cosn". 
De volgorde van de dictionary hoeft niet hetzelfde te blijven. Print de dictionary. 

RESULTAAT: {"wisk": 4, "prog": 4, "cosn": 2, "sph": 2}
"""
vakken = {"wisk": 4, "prog": 4, "error": 2, "sph": 2}

if "error" in vakken:#als key error in de dictonary zit
    vakken["cosn"] = vakken.pop("error")#verwijder de key error en vervang deze door "cosn"
print(vakken)#print de dict