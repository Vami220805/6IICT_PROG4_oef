# Open lied.txt in Python
lied = open("hfst_1/opdrachten/lied_2.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)

""" Begin eigen code hier """

# niveau 1
# lijst_lied = lied.split()
# dict = {}
# for woord in lijst_lied:
#     if woord not in dict:
#         dict[woord] = lijst_lied.count(woord)
# print(dict)

lijst_lied = lied.split()
dict = {}
for woord in lijst_lied:
    if woord not in dict:
        dict[woord] = lijst_lied.count(woord)
print(dict)
