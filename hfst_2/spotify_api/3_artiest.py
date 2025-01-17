import requests, json, csv

""" Oefen mee 6:
Haal de dictionary op uit credentials.json.

Zet de waarde van de key "access_token" (de zeer lange string),
in de variabele wachtwoord. (Idem aan oefen mee 3)
"""
fp = open("hfst_2/spotify_cred.json", "r")
dic = json.load(fp)
fp.close()  # Na sluiten is JSON niet meer bruikbaar

wachtwoord = dic["access_token"]

""" Oefen mee 7:
Stel zelf de request op. Baseer je op voorgaande bestanden en de documentatie.
Alle info die de request nodig heeft, is reeds gegeven.
"""
headers = {
    "Authorization": f"Bearer {wachtwoord}"
}
artist_id = '15x1sKugh3vsyFDj5ooa0c'
url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=BE"


beste_liedjes = requests.get(url, headers=headers).text
beste_liedjes = json.loads(beste_liedjes)

""" Oefen mee 8:
Zet de variabele lied in een JSON-bestand lied.json.

Welke artiest heb je net opgehaald?
"""
fp = open("hfst_2/beste_liedjes.json", "w")
json.dump(beste_liedjes, fp)
fp.close() # Na sluiten is JSON niet meer bruikbaar

""" Oefen mee 9:
Vul de lijst van lijsten overzicht met info over de liedjes (baseer je op de header)
"""
overzicht = []
header = ["naam_lied", "lengte (sec)", "populariteit", "externe_url"]
overzicht.append(header)
for index, lied in enumerate(beste_liedjes["tracks"]):
    # Haal uit ieder lied de informatie beschreven in de header. Zet deze in lied_info.
    # De lijst lied_info wordt tenslotte toegevoegd aan het overzicht.
    # print(lied) 
    naam = lied["name"] 
    lengte = lied["duration_ms"]
    populariteit = lied["popularity"]
    url = lied["external_urls"]["spotify"]
    lied_info = [naam, lengte, populariteit, url] # Vul aan!
    overzicht.append(lied_info)

print(overzicht)
""" Oefen mee 10:
Maak een CSV-bestand beste_liedjes.csv aan op basis van het opgestelde overzicht.
"""
fp = open( "hfst_2/beste_liedjes.csv", "w", newline="")#open het bestand in schrijf modus
csv_writer = csv.writer( fp , delimiter=";")#gebruik de functie csv.writer om het bestand te schrijven
for rij in overzicht: #doorloop de rijen in film_kritieken
    csv_writer.writerow(rij)#scrijf een rij als csv in het write bestand 

fp.close() # Na sluiten is CSV niet meer bruikbaar