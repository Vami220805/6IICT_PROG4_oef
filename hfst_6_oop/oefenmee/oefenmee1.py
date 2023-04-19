class Hond:
    naam = "Borysz"
    massa = "200kg"

hond = Hond()
huisdier = Hond()

# print(hond.naam)
# print(hond.massa)

honden = []

for _ in range(10):
    honden.append(Hond())


for index,hond in enumerate(honden):
    print(f"Hond {index} heet {hond.naam}")