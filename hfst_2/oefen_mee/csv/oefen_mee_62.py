import csv#importeer de module csv

film_kritieken = [
    {"FILM": "Monty Python and the Holy Grail", "SCORE": 8},
    {"FILM": "Monty Python's Life of Brian", "SCORE": 8.5},
    {"FILM": "Monty Python's Meaning of Life", "SCORE": 7}
]#maak lijst film_kritieken een lijst van dictionaries
film_header = ["FILM", "SCORE"]#de header voor het csv bestand is 

fp = open( "kritieken_to_csv2.csv", "w", newline="" )#open het csv bestand in schrijf modus
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=film_header)#schrijf de csv met functie csv_dictwriter en als header film_header

csv_writer.writeheader()#schrijf de header
for rij in film_kritieken:#doorloop de rijen in film_kritieken
    csv_writer.writerow(rij)#schrijf die rijen in het csv bestand

fp.close() # Na sluiten is CSV niet meer bruikbaar
