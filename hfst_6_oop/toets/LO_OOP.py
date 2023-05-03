class Bankrekening:
    def __init__(self, eigenaar, geld, leeftijd):
        self.eigenaar = eigenaar
        self.geld = geld
        self.leeftijd = leeftijd

    bank = "kbc"

    def storten(self, bedrag, bericht):
        self.geld = self.geld + bedrag
        print(f"{bedrag} euro toegevoegd. Reden: {bericht}.")

    def afhalen(self, bedrag, bericht):
        if self.leeftijd >= 16:
            if self.geld >= bedrag:
                self.geld = self.geld - bedrag
                print(f"{bedrag} euro afgehaald. Reden: {bericht}.")
            else: 
                 print(f"{self.eigenaar} heeft {self.geld} op de rekening. Dit is te weinig om {bedrag} af te halen.")
        else:
             print(f"{self.eigenaar} is te jong om geld af te halen.")

    def overzicht(self):
            print(f"{self.eigenaar} heeft {self.geld} staan bij {self.bank}")


    def overschrijven(self,bedrag, andere_rekening):
        try:
            if self.geld >= bedrag:
                self.geld = self.geld - bedrag
                andere_rekening.geld = andere_rekening.geld + bedrag
                print(f"{self.eigenaar} stort {bedrag} euro naar {andere_rekening.eigenaar}.")
            else: 
                print(f"{self.eigenaar} heeft {self.geld} op de rekening. Dit is te weinig om {bedrag} te storten naar {andere_rekening.eigenaar}")
        except AttributeError:
            print("Geen geldige rekening meegegeven.")
            self.geld = self.geld + bedrag #Geld terugstorten naar originele rekening
