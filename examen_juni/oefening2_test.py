from oefening2_bib import Boek, Bibliotheek

""" NIVEAU 1  (  / 7) """
" Aanmaken van Boeken. "
boek_1 = Boek("Python Programming", "John Smith", 2019)
boek_2 = Boek("Introduction to Physics", "Jane Johnson", 2020)
boek_3 = Boek("Mathematics in Game Design", "Kevin Doe", 2014)

" Lenen van boeken aan personen. "
boek_1.lenen("Jan")     # Python Programming geleend aan Jan.
boek_3.lenen("Joris")   # Mathematics in Game Design geleend aan Joris.
boek_3.lenen("Korneel") # Mathematics in Game Design is reeds geleend aan Joris.

print("\n################\n")

"Inleveren van boeken. "
boek_1.inleveren()      # Jan levert Python Programming in.
boek_2.inleveren()      # Kan Introduction to Physics niet inleveren, het is niet geleend.

print("\n################\n")

" Uitleg van boeken opvragen "
boek_1.uitleg()         # Python Programming is geschreven door John Smith in 2019.
boek_3.uitleg()         # Mathematics in Game Design is geschreven door Kevin Doe in 2014.
                        # Mathematics in Game Design is momenteel uitgeleend aan Joris.


""" Niveau 2 (  / 7) """
" Aanmaken van Boeken & Bibliotheken. "
boek_1 = Boek("Python Programming", "John Smith", 2019)                 
boek_2 = Boek("Introduction to Physics", "Jane Johnson", 2020)
boek_3 = Boek("Mathematics in Game Design", "Kevin Doe", 2014)
boek_4 = Boek("ifconfig & other linux commands", "Linus Torval", 2005)

bib_1 = Bibliotheek("Maaseik")
bib_2 = Bibliotheek("Genk")

" Toevoegen van boeken aan bibliotheken. "
bib_1.toevoegen_boek(boek_1)        # Python Programming toegevoegd aan bib Maaseik.
bib_1.toevoegen_boek(boek_3)        # Mathematics in Game Design toegevoegd aan bib Maaseik.

bib_2.toevoegen_boek(boek_2)        # Introduction to Physics toegevoegd aan bib Genk.
bib_2.toevoegen_boek("GEEN BOEK")   # Kan enkel boeken toevoegen aan een bib.
bib_2.toevoegen_boek(boek_4)        # ifconfig & other linux commands toegevoegd aan bib Genk. 

print("\n################\n")

" Lenen van boeken aan personen. "
bib_1.leen_boek(boek_1.titel, "Jan")        # Python Programming geleend aan Jan.
bib_1.leen_boek(boek_2.titel, "Jan")        # Introduction to Physics niet gevonden in bib Maaseik. 

bib_2.leen_boek(boek_2.titel, "Joris")      # Introduction to Physics geleend aan Joris.
bib_2.leen_boek(boek_2.titel, "Korneel")    # Introduction to Physics is reeds geleend aan Joris.
bib_2.leen_boek(boek_4.titel, "Korneel")    # ifconfig & other linux commands geleend aan Korneel.

print("\n################\n")

" Overzicht van bibliotheek oproepen. "
bib_2.uitleg_boeken()   # Introduction to Physics is geschreven door Jane Johnson in 2020.
                        # Introduction to Physics is momenteel uitgeleend aan Joris.
                        # ifconfig & other linux commands is geschreven door Linus Torval in 2005.
                        # ifconfig & other linux commands is momenteel uitgeleend aan Korneel.
                        

""" Niveau 3 (  / 1) """
" Aanmaken van Boeken & Bibliotheken. "
boek_1 = Boek("Python Programming", "John Smith", 2019)

bib_1 = Bibliotheek("Maaseik")
bib_2 = Bibliotheek("Genk")

" Toevoegen van boek_1 aan beide bibliotheken. "
bib_1.toevoegen_boek(boek_1)     # Python Programming toegevoegd aan bib Maaseik.
bib_2.toevoegen_boek(boek_1)    # Python Programming toegevoegd aan bib Genk.

print("\n################\n")

" Het boek wordt in bib_1 uitgeleend door jan. In bib_2 zou het dus nog beschikbaar moeten zijn. "
bib_1.leen_boek(boek_1.titel, "Jan")    # Python Programming geleend aan Jan.
bib_2.leen_boek(boek_1.titel, "Jan")    # Python Programming reeeds uitgeleend aan Jan.

print("\n################\n")

" In bib_2 is boek_1 schijnbaar ook uitgeleend aan Jan.  "
bib_2.uitleg_boeken()   # Python Programming is geschreven door John Smith in 2019.
                        # Python Programming is momenteel uitgeleend aan Jan.

