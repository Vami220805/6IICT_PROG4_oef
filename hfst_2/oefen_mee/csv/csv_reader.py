import csv #import de module csv om csv bestanden te lezen

fp = open( "hfst_2/oefen_mee/csv/volcanic-eruptions-EU.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=";")#gebruik de functie csv.reader om het bestand te lezen

for rij in csv_reader:#doorloop iedere rij in het bestand
    print(rij[1],rij[4])
fp.close() # Na sluiten is CSV niet meer bruikbaar