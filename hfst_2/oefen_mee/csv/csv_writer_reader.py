import csv

fp = open( "nieuwe_csv.csv", "w", newline="")

csv_writer = csv.writer( fp , delimiter=";")
csv_writer.writerow( ["FILM", "SCORE"] )
csv_writer.writerow( ["Monty Python and the Holy Grail", 8] )
csv_writer.writerow( ["Monty Python's Life of Brian", 8.5] )
csv_writer.writerow( ["Monty Python's Meaning of Life", 7] )
csv_writer.writerow( ["New KIDS", 1000] )

fp.close() # Na sluiten is CSV niet meer bruikbaar


fp = open( "nieuwe_csv.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=";")#gebruik de functie csv.reader om het bestand te lezen

for rij in csv_reader:#doorloop iedere rij in het bestand
    print(rij)
    
fp.close() # Na sluiten is CSV niet meer bruikbaar