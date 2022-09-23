""" Niveau 1"""
dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# dict= {}
# for key,value in dict_1.items():
#     dict[key] = value
# for key,value in dict_2.items():
#     dict[key] = value
# for key,value in dict_3.items():
#     dict[key] = value
# print(dict)

""" Niveau 2 """
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}
# dict1 = {}
# for key,value in dict.items():
#     if dict[key] != None:
#         dict1[key] = value
# print (dict1)

""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})
dict_4 = {}
for key,value in dict_1.items(): 
    dict_4[key] = value
    for key1, value1 in dict_2.items():
        if key1 == key:
            dict_4[key] = value = value + value1
for key,value in dict_2.items():
    if key not in dict_4:
        dict_4[key] = value
print(dict_4)
