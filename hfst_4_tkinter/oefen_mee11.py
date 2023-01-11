# Importeer tkinter module. Geef naam tk.
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

woord = ""
woord1 = ""
lijst = []

veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5)
veld.grid(row=0, column=0)

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is toevoegen van Entry veld aan Label onder de knop.
def label():
    tekst1= veld.get()#neem ingevoerde waarde
    woord = ""
    for karakter in tekst1:
        woord = woord + karakter
    # Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
    label = tk.Label(master=venster, text= woord1, height=2, fg = "red")

    # Label toevoegen aan de master (in dit geval venster).     
    label.grid(row = 2, column=0, columnspan=2)


knop = tk.Button(master=venster, command=label, text="Voeg toe aan string:", width=50)
knop.grid(row=1, column=0, pady=10, padx= 10)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()