""" 
Visualiseren met Matplotlib
    Opgelet: rotatie_1, rotatie_2, gem_rot_1, gem_rot_2, med_rot_1, med_rot_2 en tijd
             zijn variabelen bekomen uit het CSV-bestand. Hoe deze bekomen zijn, wordt hier niet getoond.
"""
import matplotlib.pyplot as plt
import csv

tijd = 0

fp = open( "csv_bestanden/experiment.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=";")#gebruik de functie csv.reader om het bestand te lezen
"Hier de csv nummers omzetten naar de benodigde variabelen"
rotatie_1 = 0
rotatie_2 = 0
gem_rot_1 = 0
gem_rot_2 = 0
med_rot_1 = 0
med_rot_2 = 0
fp.close() # Na sluiten is CSV niet meer bruikbaar

plt.subplot(1,2,1)  # Maak de linkse van twee figuren aan.
plt.xlim(0,20)      # Stel de breedte in de x-as. Laat de eerste 20s zien.
plt.grid()          # Voeg raster toe aan grafiek.
plt.plot(tijd, rotatie_1, 'g')                                  # Plot de rotatie ten opzichte van de tijd.
plt.plot(tijd, [gem_rot_1]*len(tijd), ':g')                     # Plot de gemiddelde rotatie ten opzichte van de tijd.
plt.plot(tijd, [med_rot_1]*len(tijd), '--g')                    # Plot de mediaan rotatie ten opzichte van de tijd.
plt.legend(['ogenblikkelijke w', 'gemiddelde w', 'mediaan w'])  # Zet plots in een legende.        
plt.xlabel('tijd (s)')                      # Benoem de x-as
plt.ylabel('rotatiesnelheid w (rad/s)')     # Benoem de y-as
plt.title("GSM op 10 inch velg")            # Geef figuur een titel.   

plt.subplot(1,2,2)  # Maak de rechtse van twee figuren aan.
plt.xlim(0,20)
plt.grid()
plt.plot(tijd, rotatie_2, 'r')
plt.plot(tijd, [gem_rot_2]*len(tijd), ':r')
plt.plot(tijd, [med_rot_2]*len(tijd), '--r')
plt.legend(['ogenblikkelijke w', 'gemiddelde w', 'mediaan w'])
plt.xlabel('tijd (s)')
plt.ylabel('rotatiesnelheid w (rad/s)')
plt.title("GSM op 12 inch velg")

plt.show() # Toon de grafiek.
