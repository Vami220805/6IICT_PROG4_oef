import random
class Familie:
    haarkleuren = ["blond", "bruin", "ginger", "zwart"]
    def __init__(self,ras,geslacht,haar,leeftijd, naam):
        self.naam = naam
        self.ras = ras
        self.geslacht = geslacht
        self.haar = haar
        self.leeftijd = leeftijd
    
    def is_leeftijd(self):
        print(f"{self.naam} is {self.leeftijd} jaar oud.")
    
    def is_geslacht(self):
        print(f"Het geslacht van {self.naam} is {self.geslacht}.")

    def verjaardag(self):
        self.leeftijd = self.leeftijd +1
        print(f"{self.naam} is weer een jaartje ouder, hij/haar/het is nu {self.leeftijd} jaar oud. Gefeliciteerd!")
    
    def verf_haar(self):
        oude_haarkleur = self.haar
        self.haar = random.choice(self.haarkleuren)
        print(f"{self.naam} heeft zijn/haar haar geverfd en is van {oude_haarkleur} naar {self.haar} gegaan.")
    
    def uitleg(self):
        print(f"Dit is {self.naam}. Hij/haar/het is {self.leeftijd} jaar oud en is {self.ras}. {self.naam} is {self.geslacht} en heeft {self.haar} haar.")

jur = Familie("afrikaans", "onzijdig", "blond", 69, "Jur")
jur.is_leeftijd()
jur.is_geslacht()
jur.verjaardag()
jur.verf_haar()
jur.uitleg()