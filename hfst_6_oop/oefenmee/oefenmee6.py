class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def blaf(self):
        print(f"{self.naam} zegt blaf")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa} KG")


hond1 =Hond("Floris", 8)
hond2 =Hond("Fido", 3)

hond1.weegschaal()
hond2.weegschaal()