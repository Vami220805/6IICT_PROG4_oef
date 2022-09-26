from unittest.mock import NonCallableMagicMock


poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for naam in poll_talen:
    taal = favorite_languages.get(naam)
    if taal == None: 
        favoriete_taal= input("Neem alstublieft deel aan onze poll ")
        if favoriete_taal== '':
            print("leeg")
        else: 
            favorite_languages[naam] = favoriete_taal
    else: 
        print("Bedankt voor deelnemen!")

print(favorite_languages)