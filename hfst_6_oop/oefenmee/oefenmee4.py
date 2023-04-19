class Hond:
    

    def blaf(self):
        print(f"{self.naam} zegt blaf")

    def weegschaal(zichzelf):
        print(f"{zichzelf.naam} weegt {zichzelf.massa}")

    def benoem(self,naam):
        self.naam = naam
    
    def wegen(self,massa):
        self.massa = massa

dier = Hond()
dier.benoem("Fifi")
dier.wegen(3)
dier.weegschaal()
