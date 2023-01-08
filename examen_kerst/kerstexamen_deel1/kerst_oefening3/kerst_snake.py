""" Oefening 3 (  / 3)
Dit bestand bevat het spel Snake, gemaakt met Pygame.
Het bestand maakt gebruik van oefening3.json om de instellingen te bewaren. 
oefening3.json is echter niet volledig.

Je moet enkel commentaar schrijven bij code die je zelf hebt geschreven.
"""

""" STAP 1:
Vul het bestand oefening3.json verder aan met de ontbrekende instellingen (ingeladen op regel 35). 
Je mag de waardes van deze instellingen zelf kiezen (kies wel logische waarden).
    Tip: voer de code uit en kijk op welke regels er foutmeldingen ontstaan.
"""

""" STAP 2:
Voeg code toe die de highscore in het JSON-bestand update als de speler deze verbreekt.
    Tip: Je zult oefening3.json volledig moeten overschrijven, niet enkel de score.
         Zorg dus ook dat de waarde van alle andere instellingen opnieuw in oefening3.json worden gezet.

VOORBEELD:
    De highscore is 1. Een speler haalt score 3 vooraleer dood te gaan.
    De highscore in het bestand wordt geupdatet naar waarde 3.

    De highscore is 4. Een speler haalt score 3 vooraleer dood te gaan.
    De score is niet hoger dan de highscore. Deze wordt dan ook niet gewijzigd.

Vergeet niet bij iedere regel code commentaar te schrijven.
"""

import pygame, time, random
 

 
""" Teken huidige score op scherm """
def toon_score(venster, kleuren, score):
    value = pygame.font.SysFont("comicsansms", 35).render("SCORE: " + str(score), True, kleuren["wit"])
    venster.blit(value, [0, 0])
 
""" Teken highscore op scherm """
def toon_highscore(venster, kleuren, highscore):
    value = pygame.font.SysFont("comicsansms", 35).render("HIGHSCORE: " + str(highscore), True, kleuren["wit"])
    venster.blit(value, [value.get_width(), 0])
 
""" Teken slang op scherm """
def slang(venster, kleuren, slang_blok, snake_lijst):
    for x in snake_lijst:
        pygame.draw.rect(venster, kleuren["groen"], [x[0], x[1], slang_blok, slang_blok])

def start_spel(venster, klok, highscore, breedte, hoogte, slang_blok, slang_snelheid, eten_blok, kleuren):
    """ Klaarzetten spelvariabelen """
    running = True
    x_pos, y_pos = breedte / 2, hoogte / 2
    x_snel, y_snel = 0, 0

    slang_lijst = []

    score = 0

    eten_x = round(random.randrange(0, breedte - eten_blok) / 10.0) * 10.0
    eten_y = round(random.randrange(0, hoogte - eten_blok) / 10.0) * 10.0

    """ De gameloop zelf """
    while running: 
        """ Is er een toets ingedrukt? """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_snel, y_snel = -slang_blok, 0
                elif event.key == pygame.K_RIGHT:
                    x_snel, y_snel = slang_blok, 0
                elif event.key == pygame.K_UP:
                    y_snel, x_snel = -slang_blok, 0
                elif event.key == pygame.K_DOWN:
                    y_snel, x_snel = slang_blok, 0

        """ Beweeg & update slang """
        x_pos += x_snel
        y_pos += y_snel
        slang_hoofd = []
        slang_hoofd.append(x_pos), slang_hoofd.append(y_pos), slang_lijst.append(slang_hoofd)
        if len(slang_lijst) > score+1:
            del slang_lijst[0]
        if x_pos >= breedte or x_pos < 0 or y_pos >= hoogte or y_pos < 0:
            running = False
        
        """ Kleur het venster in met de verschillende elementen """
        venster.fill(kleuren["blauw"])
        pygame.draw.rect(venster, kleuren["rood"], [eten_x, eten_y, eten_blok, eten_blok])
        slang(venster, kleuren, slang_blok, slang_lijst), toon_score(venster, kleuren, score), toon_highscore(venster, kleuren, highscore)

        """ Update het scherm """
        pygame.display.update()

        """ Heeft slang zijn eten te pakken? """
        if x_pos+slang_blok > eten_x and x_pos < eten_x+eten_blok:
            if y_pos+slang_blok > eten_y and y_pos < eten_y+eten_blok:
                eten_x = round(random.randrange(0, breedte - eten_blok) / 10.0) * 10.0
                eten_y = round(random.randrange(0, hoogte - eten_blok) / 10.0) * 10.0
                score += 1

        klok.tick(slang_snelheid)
    
    return score
