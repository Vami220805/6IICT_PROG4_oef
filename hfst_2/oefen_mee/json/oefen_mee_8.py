import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/agenda.json", "r")
agenda = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

input = input("Welke dag wilt u weten?  ")

for key, value in agenda.items():
    if input == key:
        if type(value) == list:
            for element in value:
                print(element)
        else:
            print(value)