import random
class Auto:
    kleuren= ["goud","rood", "roze", "blauw"]
    def __init__(self, verbruik, kleur, tank_vol, tank_huidig):
        self.verbruik = verbruik
        self.kleur = kleur
        self.tank_vol = tank_vol
        self.tank_huidig = tank_huidig

    def verven(self):
        self.kleur = random.choice(self.kleuren)
        print(f"Mijn auto is nu {self.kleur}")

    def check_tank(self):
        actieradius = self.tank_huidig * self.verbruik
        print(f"Met een tank van {self.tank_huidig} liter kan ik nog {actieradius} km rijden.")

    def tanken(self):
        self.tank_huidig = self.tank_vol
        print(f"Tank is weer vol met {self.tank_vol} liter.")

    def rijden(self, afstand):
        if self.tank_huidig < afstand:
            print(f"{self.tank_huidig} liter is te weinig om {afstand} te rijden.")
        else:
            self.tank_huidig = self.tank_huidig - afstand/self.verbruik
            print(f"{afstand} km afgelegd zonder problemen, nog {round(self.tank_huidig,2)} liter over.")
Buggati_Veyron = Auto(4, "matzwart", 100, 2)
Buggati_Veyron.verven()
Buggati_Veyron.check_tank()
Buggati_Veyron.tanken()
Buggati_Veyron.rijden(45)
Buggati_Veyron.check_tank()
