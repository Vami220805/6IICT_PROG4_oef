class Hond:
    def __init__(self, naam, massa):
        self.naam = naam
        self.massa = massa

    def wijzig_naam(self, naam):
        print(f"{self.naam} is de oude naam en {naam} is de nieuwe naam.")
        self.naam = naam

    def blaf(self):
        print(f"{self.naam} zegt blaf")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa} KG")
    
    def eten(self):
        self.massa = self.massa + 0.3 * 0.5
        print(f"{self.naam} heeft gegeten en weegt nu {round(self.massa,2)} KG.")


hond = Hond("Jur",4)
hond.eten()
hond.eten()
hond.eten()
hond1 = Hond("Rens",7)
hond1.eten()
hond1.eten()
hond1.eten()