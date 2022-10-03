""" Niveau 1 """
puntenlijst = [
    ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"], # 1 punt
    ["D", "G"],                                         # 2 punten
    ["B", "C", "M", "P"],                               # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    ["K"],                                              # 5 punten
    ["J", "X"],                                         # 6 punten
    ["Q","Z"]                                           # 7 punten
]

def punten_berekenen(puntenlijst):
    dict1 = {}
    gesorteerde_dict = {}
    for counter,lijst_met_aantal_punten in enumerate(puntenlijst):
        for letter in lijst_met_aantal_punten:
            kleine_letter = letter.lower()
            dict1[kleine_letter] = counter + 1
    for i in sorted(dict1):
        gesorteerde_dict[i] = dict1[i]
    return gesorteerde_dict
punten_berekenen(puntenlijst)
""" Niveau 2"""
puntenlijst_en = [
    ["A", "E", "I", "O", "U", "L", "N", "S", "T"],      # 1 punt
    ["D", "G", "K"],                                    # 2 punten
    ["B", "M", "P", "Q", "R"],                          # 3 punten
    ["F", "H", "V", "W", "Y"],                          # 4 punten
    [],                                                 # 5 punten
    ["J", "X"],                                         # 6 punten
    ["C","Z"]                                           # 7 punten
]

def punten_berekenen_niveau2(puntenlijst):
    dict1 = {}
    gesorteerde_dict = {}
    for counter,lijst_met_aantal_punten in enumerate(puntenlijst):
        for letter in lijst_met_aantal_punten:
            kleine_letter = letter.lower()
            dict1[kleine_letter] = counter + 1
    for i in sorted(dict1):
        gesorteerde_dict[i] = dict1[i]
    return gesorteerde_dict
punten_berekenen_niveau2(puntenlijst_en)

""" Niveau 3"""
##gemaakt met de dictonary

def spel_dictonary():
    woord = input("Geef een woord op om het spel te starten: ")
    dict = punten_berekenen(puntenlijst)
    som = 0
    for letter in woord:
        if letter in dict:
            value = dict.get(letter)
            som = som + value
    print(f"Uw score is {som}")
    return dict
spel_dictonary()

#gemaakt met de lijst van lijsten


def spel_lijsten(puntenlijst):
    woord = input("Geef een woord op om het spel te starten (IN HOOFDLETTERS): ")
    som= 0
    for letter in woord:
        for index,lijst in enumerate(puntenlijst):
            if letter in lijst:
                punt = index+1
                som = som + punt
    einde = f"Uw score is {som}"
    return einde
print(spel_lijsten(puntenlijst))