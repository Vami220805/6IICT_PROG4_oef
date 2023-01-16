# Importeer tkinter module. Geef naam tk.
import tkinter as tk


getal_1 = int(input("Getal1: "))
getal_2 = int(input("Getal2: "))

# TODO: functie aanmaken gelinkt aan Button knop.
#       Doel van functie is optellen van ingegeven getallen en plaatsen in een label.
#       
#       Niveau 2: iedere keer als de knop wordt ingeduwd, verhoogt de waarde van dit label.

# Maak een lege GUI aan.
venster = tk.Tk()

def optellen():
    som = getal_1 + getal_2
    label = tk.Label(master=venster, text= som, height=2, fg = "red")
    label.grid(row= 2, column = 0, columnspan=2)

# Labels aanmaken en plaatsen.
label = tk.Label(master=venster, text="Geef twee getallen in:", height=2, width=50)
label.grid(row=0, column=0, columnspan=2, pady=2)

# Label toevoegen aan de master (in dit geval venster).     
label.grid(row = 3, column=0, columnspan=2)
label_1 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 1: {getal_1}")
label_1.grid(row=1, column=0, padx=10)
label_2 = tk.Label(master=venster, font=("Helvetica",14), border=10, borderwidth=5, text=f"Getal 2: {getal_2}")
label_2.grid(row=1, column=1, padx=10)

# Knop voor tonen resultaat.
knop = tk.Button(master=venster, command=optellen, text="Bereken resultaat:", width=50)
knop.grid(row=3, column=0, columnspan=2, pady=10)

venster.mainloop()

# Maak de GUI zichtbaar op de computer.
venster.mainloop()