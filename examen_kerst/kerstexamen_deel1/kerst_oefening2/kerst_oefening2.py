""" Oefening 2 (  / 4)
Bekijk kerst_oefening2.csv. Het bevat de scores die juryleden (rij 1) hebben gegeven in een wedstrijd.
Er waren in totaal 5 deelnemers die beoordeeld zijn (rij 2-6).

In de volgende stappen zal je dit bestand inlezen, verwerken en wegschrijven.
Vergeet niet bij iedere regel code commentaar te schrijven.
"""

""" STAP 1:
Lees kerst_oefening2.csv in, in een variabele van Python. 
"""
import csv #import de module csv om csv bestanden te lezen en te schrijven

fp = open( "examen_kerst/kerstexamen_deel1/kerst_oefening2/kerst_oefening2.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=",")#gebruik de functie csv.reader om het bestand te lezen

lijst = []#maak een lege lijst aan
for rij in csv_reader:#doorloop de rijen in csv_reader
    lijst.append(rij)#voeg de rij toe aan de lege lijst
fp.close()#sluit het bestand
""" STAP 2:
print voor IEDERE deelnemer zijn scores af. 

VOORBEELD (jou print hoeft niet exact hetzelfde te zijn):
    Deelnemer 1 kreeg volgende scores: 9, 8, 9, 10
    ...
    Deelnemer 5 kreeg volgende scores: 7, 4, 6, 7
"""
for index,rij in enumerate(lijst):#doorloop de csv_reader met functie enumerate() om de rijen en de index te nemen
    if index != 0:#als index ongelijk is aan 0 (vermijd de header rij)
        print(f"Deelnemer {index} kreeg volgende scores: {rij}")#print een f string 


""" STAP 3: 
Bereken voor iedere deelnemer de gemiddelde score. 
    Tip: Ieder element in een CSV-bestand is een string. Zet deze eerst om, vooraleer iets te berekenen.

Lukt dit niet?
    Je zult de gemiddelde score nodig hebben voor stap 4. 
    Bereken de gemiddelde score van iedere persoon manueel en voeg deze zelf toe aan de code (bvb. in een lijst).
    Doe je dit, dan krijg je geen punten op STAP 3.
"""
lijst1 = []#maak een nieuwe lijst aan
for index,rij in enumerate(lijst):#doorloop de csv_reader met functie enumerate() om de rijen en de index te nemen
    totaal = 0#totaal is gelijk aan 0
    if index != 0:#als index niet gelijk is aan 0 (vermijd de header rij)
        for element in rij:#doorloop iedere element in de rij
            element = int(element)#maak een integer van ieder element
            totaal += element#tel deze elementen bij elkaar op
        gemiddelde = totaal / len(rij)#gemiddelde is het totaal delen door het aantal elementen in de rij
        rij.append(gemiddelde)#voeg het berekende gemiddelde toe aan de rij
        lijst1.append(rij)#zet de rij in een nieuwe lijst
    else:
        header = rij#maak header gelijk aan de huidige rij

""" STAP 4:
Maak een nieuw bestand kerst_oefening2_verwerkt.csv aan. Dit bestand bevat alle kolommen van kerst_oefening2.csv.
Voeg er nog een nieuwe kolom aan toe. Deze bevat de gemiddelde score van iedere deelnemer (bepaald in STAP 3).

Een voorbeeld van het resultaat is te vinden in kerst_voorbeeld2.csv
"""
fp = open( "kerst_oefening2_verwerkt.csv", "w", newline="")#open het file path
csv_writer = csv.writer( fp , delimiter=",")#schrijf in csv met functie csv.writer
csv_writer.writerow(header)#scrijf een rij als csv in het write bestand 
for rij in lijst1:#doorloop de rijen in de nieuwe lijst
    csv_writer.writerow(rij)#scrijf een rij als csv in het write bestand 
fp.close()#sluit het bestand