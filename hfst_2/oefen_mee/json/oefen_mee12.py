import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee12.json", "r")
agenda = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

input1 = input("Welke dag wilt u weten?  ")

for key, value in agenda.items():
    if input1 == key:
        print(f"Op {key} heb je de volgende dingen gepland: ")
        if type(value) == list:
            for element in value:
                print(element)
        else:
            print(value)
        print("")
        vraag = input("Wil je deze activiteit wijzigen (j/n)? ")
        if vraag == "j":
            toevoegen= input("Geef nieuwe activiteit(en) in: ")
            toevoeg_lijst = toevoegen.split()
            agenda[key] = toevoeg_lijst
            # agenda[key] = toevoegen
fp = open("hfst_2/oefen_mee/json/oefen_mee12.json", "w")
json.dump(agenda, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar


#deel 2:
# if vraag == "j":
#     toevoegen= input("Geef nieuwe activiteit(en) in: ")
#     agenda[key] = toevoegen