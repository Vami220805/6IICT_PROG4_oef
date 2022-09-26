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

# def punten_berekenen(puntenlijst):
#     dict = {}
#     for counter,lijst_met_aantal_punten in enumerate(puntenlijst):
#         for letter in lijst_met_aantal_punten:
#             kleine_letter = letter.lower()
#             dict[kleine_letter] = counter + 1
#     gesorteerde_dict = sorted(dict.items())
#     return gesorteerde_dict
# print(punten_berekenen(puntenlijst))

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
    dict = {}
    for counter,lijst_met_aantal_punten in enumerate(puntenlijst):
        for letter in lijst_met_aantal_punten:
            kleine_letter = letter.lower()
            dict[kleine_letter] = counter + 1
    gesorteerde_dict = sorted(dict.items())
    return gesorteerde_dict
print(punten_berekenen_niveau2(puntenlijst_en))