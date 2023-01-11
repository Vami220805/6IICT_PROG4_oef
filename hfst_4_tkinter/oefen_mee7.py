import tkinter as tk#imprteer de module en geef deze naam tk

venster = tk.Tk()# Maak een lege GUI aan.

# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
label = tk.Label(master=venster, text="Geef naam op: ", width=15, height=2, 
                 highlightthickness=2, highlightbackground="black")

# Label toevoegen aan de master (in dit geval venster).         
label.grid(row=0, column=0)

# Voeg invoervlak toe aan master
veld = tk.Entry(master=venster, width=50, fg="red")

# Veld toevoegen aan de master
veld.grid(row=0, column=1)

# Neem de ingevoerde naam en toon deze in een zin, onder de knop
def display_naam():
    tekst = f"Hallo, mijn naam is {veld.get()}!"
    label_naam = tk.Label(master=venster, text=tekst, width=50, height=2)
    label_naam.grid(row=2, column=0, columnspan=2)

# Knop voor tonen resultaat.
knop = tk.Button(master=venster, command=display_naam, text="Voer in!", width=50)
knop.grid(row=1, column=0, columnspan=2)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()
