# Importeer tkinter module. Geef naam tk.
import tkinter as tk

from functools import partial

# Maak een lege GUI aan.
venster = tk.Tk()

veld = tk.Entry(master=venster, font=("Helvetica",14), border=10, borderwidth=5, bg="green")
veld.grid(row=0, column=0, columnspan=3)


# Label toevoegen aan de master (in dit geval venster).     

def getal(getal):
    print(getal)

getalfunctie = partial(getal, 1)
knop1 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="1", width = 5, command= getalfunctie)
knop1.grid(row=1, column=0)
getalfunctie = partial(getal, 2)
knop2 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="2", width = 5, command= getalfunctie)
knop2.grid(row=1, column=1)
getalfunctie = partial(getal, 3)
knop3 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="3", width = 5, command= getalfunctie)
knop3.grid(row=1, column=2)

getalfunctie = partial(getal, 4)
knop4 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="4", width = 5, command= getalfunctie)
knop4.grid(row=2, column=0)
getalfunctie = partial(getal, 5)
knop5 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="5", width = 5, command= getalfunctie)
knop5.grid(row=2, column=1)
getalfunctie = partial(getal, 6)
knop6 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="6", width = 5, command= getalfunctie)
knop6.grid(row=2, column=2)

getalfunctie = partial(getal, 7)
knop7 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="7", width = 5, command= getalfunctie)
knop7.grid(row=3, column=0)
getalfunctie = partial(getal, 8)
knop8= tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="8", width = 5, command= getalfunctie)
knop8.grid(row=3, column=1)
getalfunctie = partial(getal, 9)
knop9 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="9", width = 5, command= getalfunctie)
knop9.grid(row=3, column=2)

getalfunctie = partial(getal, 0)
knop0 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="0", width = 5, command= getalfunctie)
knop0.grid(row=4, column=0)
knop10= tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="+", width = 5)
knop10.grid(row=4, column=1)
knop11 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="-", width = 5)
knop11.grid(row=4, column=2)

knop12 = tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="=", width = 5)
knop12.grid(row=5, column=0)
knop13= tk.Button(master=venster, font=("Helvetica",14), border=10, borderwidth=2, text="CLR", width = 10)
knop13.grid(row=5, column=1, columnspan=2)


# knop = tk.Button(master=venster, command=label, text="Voeg toe aan string:", width=50)
# knop.grid(row=1, column=0, pady=10, padx= 10)
#partial functie


# Maak de GUI zichtbaar op de computer.
venster.mainloop()