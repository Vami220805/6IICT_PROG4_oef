import requests #importeer de module requests

antwoord = requests.get("https://api.covid19api.com/world/total").text  #gebruik de get functie om de informatie van de api te krijgen en zet 
                                                                        #dit om naar tekst(string) met text functie
print(antwoord)#print het antwoord
