class Boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel 
        self.auteur = auteur 
        self.jaar = jaar 
        self.geleend_aan = ""

    def lenen(self, persoon): 
        if len(self.geleend_aan) > 0:
            print(f"{self.titel} is reeds uitgeleend aan {self.geleend_aan}.")
        else:
            self.geleend_aan = persoon
            print(self.geleend_aan)
            print(f"{self.titel} geleend aan {self.geleend_aan}.")

    def inleveren(self):
        if self.geleend_aan == "":
            print(f"Kan {self.titel} niet inleveren, het is niet geleend.")
        else:
            print(f"{self.geleend_aan} levert {self.titel} in.")
            self.geleend_aan = ""

    def uitleg(self):
        print(f"{self.titel} is geschreven door {self.auteur} in {self.jaar}") 
        if self.geleend_aan != "":
            print(f"{self.titel} is momenteel uitgeleend aan {self.geleend_aan}")

class Bibliotheek:
    def __init__(self, naam):
        self.naam = naam 
        self.boeken = []
    
    def toevoegen_boek(self,boek):
        if isinstance(boek, Boek):
            self.boeken.append(boek)
            print(f"{boek.titel} toegevoegd aan bib {self.naam}. ")
        else: 
            print(f"Kan enkel boeken toevoegen aan een bib.")

    def uitleg_boeken(self):
        for boek in self.boeken:
            boek.uitleg()

    def leen_boek(self, titel, persoon):
        for boek in self.boeken:
            if boek.titel == titel:
                boek.lenen(persoon)
                return
        if titel not in self.boeken:
            print(f"{titel} niet gevonden in bib {self.naam}")

    def lever_boek_in(self,titel):
        for boek in self.boeken:
            if boek == titel:
                boek.inleveren()
        if titel not in self.boeken:
            print(f"{titel} niet gevonden in de bib {self.naam}")


# """ Niveau 3: Leg in dit tekstveld uit waarom het aangegeven probleem optreed. 
#               Leg ook uit hoe je het kan oplossen.
# Het probleem ontstaat doordat de string geleend_aan niet leeg gemaakt wordt als iemand zou wisselen van bibliotheek. Zo blijft
# de naam Jan staan in geleend_aan en lijkt het alsof dit boek ook uitgeleend is in de andere bibliotheek.
# Dit is op te lossen door de andere bibliotheek te herkennen en op verandering het geleend_aan leeg te maken.
# Ik heb het opgelost op deze manier:

    # def lenen(self, naam_bib, persoon): 
    #     if len(self.previous)> 0:
    #         if self.previous != naam_bib:
    #             self.geleend_aan = ""
    #     if len(self.geleend_aan) > 0:
    #         print(f"{self.titel} is reeds uitgeleend aan {self.geleend_aan}.")
    #     else:
    #         self.geleend_aan = persoon
    #         print(self.geleend_aan)
    #         print(f"{self.titel} geleend aan {self.geleend_aan}.")
    #         self.previous = naam_bib
# """