""" Oefening 4 (  / 2)
Maak onderstaande opdrachten over dictionaries.

Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" Opdracht 1:
Zoek in onderstaande dictionary de club die het MEESTE kaarten heeft ontvangen.
Print deze club. Opgelet! Dit programma moet ook blijven werken als de dictionary wijzigt.

RESULTAAT: Nederland
"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

maximum = max(aantal_kaarten_wk, key=aantal_kaarten_wk.get)#neem het maximum value van de dict en neem van deze max value de key en sla deze op in var maximum
print(maximum)#print maximum

""" Opdracht 2:
Print de waarde bij de key "corners".
"""
wk = {"Duitsland": {"status": "uitgeschakeld", "matchen_gespeeld": 3, "statistieken": {"kaarten": 14, "corners": 9.8, "CS%": 10}}}

print(wk["Duitsland"]["statistieken"]["corners"])#ga naar key corners en print de value

""" Opdracht 3:
Vraag de gebruiker om een letter. Verwijder vervolgens alle keys waarin deze letter staat.
    Tip: gebruik if ... in ... om te controleren of een bepaalde letter in de key voorkomt.

Print de gewijzigde dictionary. 
Opgelet! Het programma mag geen onderscheid maken tussen kleine en grote letters.

VOORBEELD:
    Geef een letter op: L
    {"Spanje": 7}

    Geef een letter op: N
    {}

    Geef een letter op: z
    {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

"""
aantal_kaarten_wk = {"Duitsland": 14, "Nederland": 24, "Spanje": 7, "Polen": 20}

dic = {}#maak een nieuwe lege dictonary aan
letter = input("Geef een letter op: ")#vraag de gebruiker om een letter
for key,value in aantal_kaarten_wk.items():#doorloop alle keys en values in de dict met functie items
    if letter.lower() not in key.lower():#als letter (in kleine letters) niet in key(in kleine letters) is
        dic[key] = value#voeg de key en value toe aan de nieuwe dict
print(dic)#print de dict