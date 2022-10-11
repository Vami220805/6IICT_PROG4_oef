import csv # importeer de module csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )# open het bestand in read modus
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") #gebruik functie csv 
# reader om het bestand te lezen
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []# maak een lege lijst aan
for rij in csv_reader: # doorloop de rijen
    eruptions_ll.append([rij[1],rij[4]])# voeg deze rijen toe aan de lege lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

# for eruption in eruptions_ll:#doorloop de lijst
#     print(eruption)# print element van lijst
print(eruptions_ll)#print lijst
