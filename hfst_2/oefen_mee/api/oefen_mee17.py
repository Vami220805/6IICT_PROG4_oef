import json, requests # Benodigde modules

""" STAP 1: API klaarmaken om JSON in string-formaat te downloaden """
# Geef tweeletter-code van land (https://www.iban.com/country-codes)
land = input("Geef tweeletter-code van land (Belgie = BE): ")
# Geef stad:
stad = input(f"Geef stad (in het Engels): ")
# Geef API-key:
API_key = "fbf4dc9f73c6bb468fb08fa5375cb058"

# Stel de api op, waarmee we data kunnen afhalen van openweathermap.org
api = f"https://api.openweathermap.org/data/2.5/forecast?q={stad},{land}&appid={API_key}"

""" STAP 2: Haal JSON-string af van OpenWeatherMap.org """
# Roep weerdata op via api.
antwoord = requests.get(api).text

# Haal uit commentaar om onbewerkte JSON text te zien.
# print(antwoord) 

""" Stap 3: Vorm JSON-string om naar Python structuur (lijst of dictionary). 
       Tip: Schrijf structuur weg naar JSON-bestand, je kan deze gebruiken voor stap 4. 
"""
antwoord_dict = json.loads(antwoord)
print(antwoord_dict)

""" Stap 4: Print weerbeschrijving op basis van structuur 
       Tip: analyseer hiervoor de verkregen data. 
            Welke structuren zijn aanwezig? Via welke keys/index krijg ik de benodigde data?
"""

# print(f"Huidig weer in {stad}")
# main = antwoord_dict['list']['weather']['main']
# desc = antwoord_dict['list']['weather']['description']
# print(f"{main} - {desc}")


# print(f"Morgen:")
# main = antwoord_dict['list']['weather']['main']
# desc = antwoord_dict['list']['weather']['description']
# print(f"{main} - {desc}")

# print("Overmorgen:")
# main = antwoord_dict['list']['weather']['main']
# desc = antwoord_dict['list']['weather']['description']
# print(f"{main} - {desc}")