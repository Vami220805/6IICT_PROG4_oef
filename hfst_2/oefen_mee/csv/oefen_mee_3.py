import csv # importeer de module csv

fp = open( "volcanic-eruptions-EU.csv", "r" )# open het bestand in read modus
# var csv_reader kan je niet rechtstreeks wijzigen of oproepen.
csv_reader = csv.reader( fp , delimiter=";") #gebruik functie csv 
# reader om het bestand te lezen
# print(csv_reader[3]) # Voorbeeld

# Aanmaken ECHTE lijst van lijsten (ll) en hierin gegevens stoppen
eruptions_ll = []# maak een lege lijst aan
for rij in csv_reader: # doorloop de rijen
    eruptions_ll.append(rij)# voeg deze rijen toe aan de lege lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

for eruption in eruptions_ll:#doorloop de lijst
    print(eruption)# print element van lijst



import csv# importeer module csv

fp = open( "volcanic-eruptions-EU.csv", "r" ) # open het 
# bestand
csv_reader = csv.DictReader( fp , delimiter=";")#gebruik de 
# functie csv reader om het bestand de lezen als Dict

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader: #doorloop de rijen van de lezer
    print(rij)#print deze rij
    eruptions_ld.append(rij)# voeg deze rij toe aan lege lijst

fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")# print lege lijn
print(eruptions_ld) #print de lijst
