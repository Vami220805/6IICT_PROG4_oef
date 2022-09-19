""" 
Voorbeeld:

>>> input() = "Dit is een zin"
>>> Dict    = {"Dit": "tiD", "is": "si", "een": "nee", "zin": "niz"}

Tip: je hebt al in de reeksen gezien hoe een woord om te keren.

"""

zin = input("Geef een zin op: ")
dictionary = {}
lijst_gesplitst = zin.split()
for woord in lijst_gesplitst:
    reverse = woord[::-1]
    dictionary[woord]= reverse
print(dictionary)