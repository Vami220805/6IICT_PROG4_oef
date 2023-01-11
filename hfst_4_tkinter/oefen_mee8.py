# Importeer de module en geef deze naam tk
import tkinter as tk

# Maak een lege GUI aan.
venster = tk.Tk()

# Label aanmaken.
    # master: geef aan tot welke GUI het label behoort.
    # text: boodschap van het label.
label = tk.Label(master=venster, text="Welke website wil je bezoeken?", height=2)

# Label toevoegen aan de master (in dit geval venster).     
label.grid(row=0, column=0, columnspan=2)

# Voeg invoervlak toe aan master
link_1 = tk.Entry(master=venster, width=33, font=("Helvetica",14),
                  border=10, borderwidth=5)

# Link toevoegen aan master
link_1.grid(row=1, column=0)

# Voeg invoervlak toe aan master
link_2 = tk.Entry(master=venster, width=33, font=("Helvetica",14), 
                  border=10, borderwidth=5)

# Link toevoegen aan master
link_2.grid(row=1, column=1)

# Functie voor resetten invoervelden
def reset_links():
    link_1.delete(0, 1)# verwijder eerste element van vlak 1

    web_2 = link_2.get()#neem ingevoerde waarde
    link_2.delete( 0, web_2.find(".")+1 )#zoek index van eerstvolgend . en tel daar 1 bij op. Verwijder vanaf 0 tot de index van . +1

# Knop voor tonen resultaat.
knop = tk.Button(master=venster, command=reset_links, 
                 text="Reset input!", width=50)
knop.grid(row=2, column=0, columnspan=2)

# Maak de GUI zichtbaar op de computer.
venster.mainloop()