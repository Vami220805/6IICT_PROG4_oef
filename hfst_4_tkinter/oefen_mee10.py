# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Vraag om de lievelingskleur van de gebruiker (rood, groen of blauw)
kleur = input("Wat is je favoriete kleur? ")

# Maak een lege GUI aan.
venster = tk.Tk()

dict1 = {
    "rood": "red",
    "groen": "green",
    "blauw": "blue"
}
# TODO: vertaal input van gebruiker naar het Engels
for key, value in dict1.items():
    if kleur == key: 
        color = value

# TODO: maak functie aan die het label in de ingegeven kleur laat zien.
def kleur_fav(): 
    # Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
    label = tk.Label(master=venster, text=f"Mijn favoriete kleur is {kleur}!", height=2, fg = color)

    # Label toevoegen aan de master (in dit geval venster).     
    label.grid(column=0, columnspan=2)


knop1 = tk.Button(master=venster, command=kleur_fav, text="Klik op mij!")
knop1.grid(row=0)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()