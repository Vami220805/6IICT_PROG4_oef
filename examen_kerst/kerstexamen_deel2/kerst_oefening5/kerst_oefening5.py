""" Oefening 5 (  / 4)
Het JSON-bestand kerst_oefening5.json bevat een agenda.
Het zou echter handiger zijn als deze agenda in een CSV-bestand stond.

Lees kerst_oefening5.json in, in een Python variabele.
Schrijf deze vervolgens weg naar een bestand kerst_oefening5.csv.
kerst_voorbeeld5.csv toont hoe dit CSV-bestand er uit moet zien.

ALLES wat je naar dit CSV-bestand schrijft, moet uit het JSON-bestand komen. Manueel zaken ingeven mag dus niet.
Dit zodat het converteren blijft werken, ook wanneer je een andere JSON-agenda zou gebruiken.
Je mag ervanuit gaan dat iedere dag HETZELFDE aantal activiteiten heeft.
"""

import csv,json #import de module csv om csv bestanden te lezen en schrijven en module json om json bestanden te lezen en schrijven

fp = open( "examen_kerst/kerstexamen_deel2/kerst_oefening5/kerst_oefening5.json", "r" )#open het json bestand met lees modus
agenda = json.load(fp)#laad json bestand in variabele agenda
fp.close()#sluit het bestand

header = []#lege lijst header
lijst1=[]#lege lijst 1
lijst2=[]#lege lijst 2
lijst3=[]#lege lijst 2
for key,value in agenda.items():#doorloop de keys en values van de agenda met functie items
    header.append(key)#voeg huidige key toe aan lijst header
    lijst1.append(value[0])#voeg value op index 0 toe aan lijst1
    lijst2.append(value[1])#voeg value op index 1 toe aan lijst2
    lijst3.append(value[2])#voeg value op index 2 toe aan lijst3

fp = open( "kerst_oefening5.csv", "w", newline="")#open het file path
csv_writer = csv.writer( fp , delimiter=",")#schrijf in csv met functie csv.writer
csv_writer.writerow(header)#scrijf de header als csv in het write bestand 
csv_writer.writerow(lijst1)#scrijf een lijst als csv in het write bestand 
csv_writer.writerow(lijst2)#scrijf een lijst als csv in het write bestand 
csv_writer.writerow(lijst3)#scrijf een lijst als csv in het write bestand 
fp.close()#sluit het bestand