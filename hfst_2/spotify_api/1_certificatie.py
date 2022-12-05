import requests, json

client_id = "b21b9c59d6534052a691402188d37c1b"
client_secret = "406ca2e1c1a9494eab39276ff72df506"

# Herinner je dat een API gewoon een speciale URL is...
# Via deze URL kunnen we ons inlogtoken aanvragen.
url = 'https://accounts.spotify.com/api/token'

# Deze zaken moeten we de API geven om een inlogtoken te genereren.
inloggegevens = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# requests het inlogtoken, haal de tekst uit deze request en zet in cred_response
cred_resp = requests.post(url, inloggegevens).text
# Opgelet! Onderstaande regel is BELANGRIJK. 
cred_resp = json.loads(cred_resp)

print(cred_resp)

""" Oefen mee 2: 
zet de dictionary cred_resp in JSON-bestand met de naam certificatie.json

"""

fp = open("hfst_2/spotify_cred.json", "w")
json.dump(cred_resp, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar