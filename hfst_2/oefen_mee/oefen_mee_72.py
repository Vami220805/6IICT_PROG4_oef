import csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" )
csv_reader = csv.DictReader( fp , delimiter=";")

eruptions_ld = [] # ld = lijst van dictionaries
for rij in csv_reader:
    eruptions_ld.append(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar

eruptions_ld_verwerkt = []

for index, rij in enumerate(eruptions_ld):
    dict = {}
    dict["Year"] = abs(int(rij["Year"]))
    dict["Name"] = rij["Name"].lower()
    eruptions_ld_verwerkt.append(dict)
header = ["Year", "Name"]#de header voor het csv bestand is 

fp = open( "csv_bestanden/csv_verwerkt_dict.csv", "w", newline="" )
csv_writer = csv.DictWriter( fp , delimiter=";", fieldnames=header)

csv_writer.writeheader()
for rij in eruptions_ld_verwerkt:
    csv_writer.writerow(rij)

fp.close() # Na sluiten is CSV niet meer bruikbaar