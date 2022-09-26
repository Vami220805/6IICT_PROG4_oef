poll_talen = ["Lucas", "Maud", "Jan", "Dillan", 
              "Piet", "Joris"]

favorite_languages = {    
    "Jan": "python",    
    "Piet": "c",    
    "Joris": "ruby"}

for naam in poll_talen:
    taal = favorite_languages.get(naam)
    if taal == None: 
        favoriete_taal= input(f"{naam}, neem alstublieft deel aan onze poll ")
        if favoriete_taal== '':
            print("leeg")
        else: 
            favorite_languages[naam] = favoriete_taal
            print("bedankt!")
    else: 
        print(f"{naam}, bedankt voor deelnemen!")
print(favorite_languages)