""" Oefening 3 (  / 2)
Dit bestand roept het spel Snake op, gemaakt in kerst_snake.py 
(je hoeft kerst_snake.py NIET te bekijken om deze oefening te maken).

Dit bestand haalt hiervoor instellingen uit kerst_oefening3.json. Deze is echter zo goed als leeg.
Volg de 2 stappen om het spel werkende te krijgen.
"""

""" STAP 1: 
Vul kerst_oefening3.json aan op basis van onderstaande instellingen (vanaf regel 32).
De waardes van de instellingen zijn ernaast in commentaar geschreven.

Als je de instellingen correct hebt, kan je door kerst_oefening3.py uit te voeren Snake starten.
Het is niet nodig om commentaar aan te brengen in het JSON-bestand.
"""

import kerst_snake as snake, pygame, json

""" JSON-bestand inladen. Let op voor het pad! """
fp = open("examen_kerst/kerstexamen_deel1/kerst_oefening3/kerst_oefening3.json", "r")
info = json.load(fp)
fp.close()

""" Instellingen die reeds in kerst_oefening3.json staan. """
highscore = info["highscore"]

""" Instellingen die nog ontbreken (zie Stap 1) """
breedte        = info["scherm"]["breedte"]  # 600
hoogte         = info["scherm"]["hoogte"]   # 400
slang_blok     = info["slang"]["grootte"]   # 10
slang_snelheid = info["slang"]["snelheid"]  # 15
eten_blok      = info["eten"]               # 10
kleuren        = {
    "wit": info["kleur"][0],                # [255,255,255]
    "rood": info["kleur"][1],               # [255,0,0]
    "groen": info["kleur"][2],              # [0, 255, 0]
    "blauw": info["kleur"][3]               # [0, 0, 255]
}

""" Pygame klaarzetten voor gebruik """
pygame.init()
venster = pygame.display.set_mode((breedte, hoogte))
pygame.display.set_caption('Snake')
klok = pygame.time.Clock()

""" Start spel. (behaalde_score nodig voor Stap 2) """
behaalde_score = snake.start_spel(venster, klok, highscore, breedte, hoogte, slang_blok, slang_snelheid, eten_blok, kleuren)

""" Stop pygame """
pygame.quit()
quit()
