import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee_9.json", "r")
bestand = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar



for key,onderwerp in bestand["quiz"].items():
    for key2,vraag in onderwerp.items():
        print(vraag["vraag"])
        antwoorden = vraag["opties"]
        print(f"Mogelijke antwoorden zijn: {antwoorden}")
        antwoord = input("Antwoord: ")
        juiste_antwoord =vraag["antwoord"]
        if antwoord == juiste_antwoord:
            print(f"{antwoord} is correct!")
        else:
            print(f"{antwoord} is fout. Het correcte antwoord is {juiste_antwoord}")
        print("")