import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee_9.json", "r")
agenda = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

print(agenda)