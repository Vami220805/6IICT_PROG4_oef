import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee12.json", "r")
agenda = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

vraag_doorgaan  ="j"
while vraag_doorgaan == "j":
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
            vraag = input("Wil je deze activiteit wijzigen (J/N)? ")
            if vraag == "j":
                toevoegen= input("Geef nieuwe activiteit(en) in: ")
                toevoeg_lijst = toevoegen.split()
                agenda[key] = toevoeg_lijst
                # agenda[key] = toevoegen
    vraag_doorgaan = input("Wil je nog een andere dag bekijken (J/N)? ")

fp = open("hfst_2/oefen_mee/json/oefen_mee12.json", "w")
json.dump(agenda, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar