import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee_9.json", "r")
bestand = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

print(bestand)