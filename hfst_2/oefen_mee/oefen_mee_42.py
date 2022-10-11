import csv# importeer module csv

fp = open( "hfst_2/oefen_mee/volcanic-eruptions-EU.csv", "r" ) # open het 
# bestand
csv_reader = csv.DictReader( fp , delimiter=";")#gebruik de 
# functie csv reader om het bestand de lezen als Dict

eruptions_ld = [] # ld = lijst van dictionaries
nieuwe_dict = {}
for dict in csv_reader: #doorloop de rijen van de lezer
    print(dict)#print deze dict
    for key,value in dict.items():
        if key == "Year":
            nieuwe_dict[key] =value
        if key == "Name":
            nieuwe_dict[key] = value
        eruptions_ld.append(nieuwe_dict)
fp.close() # Na sluiten is CSV niet meer bruikbaar

print("")# print lege lijn
print(eruptions_ld) #print de lijst
