import csv #importeer de module

film_kritieken = [ 
    ["FILM", "SCORE"],
    ["Monty Python and the Holy Grail", 8],   
    ["Monty Python's Life of Brian", 8.5],
    ["Monty Python's Meaning of Life", 7]
]#maak lijst film_kritieken met lijsten van film scores

fp = open( "kritieken_to_csv.csv", "w", newline="")#open het bestand in schrijf modus
csv_writer = csv.writer( fp , delimiter=";")#gebruik de functie csv.writer om het bestand te schrijven

for rij in film_kritieken: #doorloop de rijen in film_kritieken
    csv_writer.writerow(rij)#scrijf een rij als csv in het write bestand 

fp.close() # Na sluiten is CSV niet meer bruikbaar