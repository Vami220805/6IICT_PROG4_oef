""" OEFENING 2: (  /3)
Onderstaande code gebruikt een API om twee willekeurig getallen te genereren.
Vervolgens wordt het eerste door het tweede getal gedeeld.

Je hebt de requests module nodig voor deze opgave.
"""

""" STAP 1: (  / 2)
Deze code is niet veilig. Er kunnen (minstens) twee zaken misgaan.
    - Delen door 0 (ZeroDivisionError)
    - Geen verbinding met de API (requests.exceptions.ConnectionError)

Vorm de code om naar een try-except structuur, rekening houdend met deze Errors.
Laat de gebruiker in beide gevallen duidelijk weten wat er misliep (gebruikt dus 2 specifieke Exceptions).
    Tip: je kan de requests.exception.ConnectionError simuleren door je internet af te zetten.

Vang alle andere Errors op met een algemene boodschap (VB: "Er ging iets mis...")
"""

""" STAP 2: (  / 1)
Als zich GEEN Errors voordoen, print dan volgende boodschap:
"Programma kwam geen fouten tegen."
"""
import requests, json # Benodigde modules.
try:#probeer deze code te runnen
    API = "http://www.randomnumberapi.com/api/v1.0/random?min=0&max=3&count=2" # Genereer twee getallen tussen 0 en 5.
    getallen = json.loads(requests.get(API, timeout=3).text) # Haal de twee getallen op als tekst, converteer naar lijst.
    getal_1, getal_2 = getallen[0], getallen[1]   # Zet twee getallen in aparte variabelen.

    print(f"De deling van {getal_1} en {getal_2} is {getal_1/getal_2}") # Print de deling.
except ZeroDivisionError:#als er een zerodivisionerror is
    print("Delen door 0 gaat niet, programma gestopt.")#print een zin
except requests.exceptions.ConnectionError: #als er een verbindingsfout is 
    print("Verbindingsfout met de API, programma gestopt.")#print een zin
except:#als er iets anders fout is
    print("Er is iets mis gegaan.")#print een zin
else:#als er geen fouten zijn
    print("Programma kwam geen fouten tegen.")#print een zin
