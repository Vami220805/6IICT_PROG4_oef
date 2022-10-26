import json

# Pad is afhankelijk van locatie appel.json
fp = open("hfst_2/oefen_mee/json/oefen_mee13.json", "r")
lijst = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

for index, dict in enumerate(lijst):
    if dict["Date"] == '2022-09-18':
        aantal_vandaag = 0
    else:
        vorige = lijst[index - 1]
        aantal_vandaag = dict["Cases"] - vorige["Cases"]
        print(f"Er zijn op {dict['Date']} {aantal_vandaag} nieuwe besmettingen")
    dict["New Cases"] = aantal_vandaag

fp = open("hfst_2/oefen_mee/json/oefen_mee13_2.json", "w")
json.dump(lijst, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar