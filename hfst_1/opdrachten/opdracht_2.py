films = [ "Monty Python and the Holy Grail",
          "Monty Python's Life of Brian",
          "Monty Python's Meaning of Life",
          "And Now For Something Completely Different"]

scores = [
    [ 9, 10, 9.5, 8.5, 3, 7.5 ,8 ], # Grail
    [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ], # Brian
    [ 7, 6, 5 ], # Life
    [ 6, 5, 6, 6 ] # Different
] 

dict = {}
som = 0
for i in range(len(films)):
    titel = films[i]
    rating= scores[i]
    dict[titel]= rating
print(dict)

for key,value in dict.items():
    som= sum(value)
    gemiddelde = round(som/len(value),1)
    print(gemiddelde)