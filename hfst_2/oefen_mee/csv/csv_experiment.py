""" 
Visualiseren met Matplotlib
    Opgelet: rotatie_1, rotatie_2, gem_rot_1, gem_rot_2, med_rot_1, med_rot_2 en tijd
             zijn variabelen bekomen uit het CSV-bestand. Hoe deze bekomen zijn, wordt hier niet getoond.
"""
import matplotlib.pyplot as plt
import statistics
import csv

plt.subplot(1,2,1)  # Maak de linkse van twee figuren aan.
plt.xlim(0,20)      # Stel de breedte in de x-as. Laat de eerste 20s zien.
plt.grid()          # Voeg raster toe aan grafiek.

totaal1 = 0
totaal2 =0
tijd1= []
tijd2= []
snelheid1 = []
snelheid2 = []
fp = open( "csv_bestanden/experiment10in.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=",")#gebruik de functie csv.reader om het bestand te lezen
for index, rij in enumerate(csv_reader):#doorloop iedere rij in het bestand
    if index != 0:
        tijd1.append(float(rij[0]))
        snelheid1.append(float(rij[1]))
fp.close() # Na sluiten is CSV niet meer bruikbaar

plt.plot(tijd1, snelheid1, 'g')     # Plot de rotatie ten opzichte van de tijd.
for element in snelheid1:
    totaal1 += element
gem_rot_1 = totaal1/len(snelheid1)
plt.plot(tijd1, [gem_rot_1]*len(tijd1), ':g')                     # Plot de gemiddelde rotatie ten opzichte van de tijd.
med_rot_1 = statistics.median(snelheid1)
plt.plot(tijd1, [med_rot_1]*len(tijd1), '--g')                    # Plot de mediaan rotatie ten opzichte van de tijd.
plt.legend(['ogenblikkelijke w', 'gemiddelde w', 'mediaan w'])  # Zet plots in een legende.        
plt.xlabel('tijd (s)')                      # Benoem de x-as
plt.ylabel('rotatiesnelheid w (rad/s)')     # Benoem de y-as
plt.title("GSM op 10 inch velg")            # Geef figuur een titel.   
plt.subplot(1,2,2)  # Maak de rechtse van twee figuren aan.
plt.xlim(0,20)
plt.grid()

fp = open( "csv_bestanden/experiment12in.csv", "r" )#open het csv bestand met lees modus
csv_reader = csv.reader( fp , delimiter=",")#gebruik de functie csv.reader om het bestand te lezen
for index, rij in enumerate(csv_reader):#doorloop iedere rij in het bestand
    if index !=0:
        tijd2.append(float(rij[0]))
        snelheid2.append(float(rij[1]))
fp.close() # Na sluiten is CSV niet meer bruikbaar
plt.plot(tijd2, snelheid2, 'r')
for element in snelheid2:
    totaal2 += element
gem_rot_2 = totaal2/len(snelheid2)
plt.plot(tijd2, [gem_rot_2]*len(tijd2), ':r')
med_rot_2 = statistics.median(snelheid2)
plt.plot(tijd2, [med_rot_2]*len(tijd2), '--r')
plt.legend(['ogenblikkelijke w', 'gemiddelde w', 'mediaan w'])
plt.xlabel('tijd (s)')
plt.ylabel('rotatiesnelheid w (rad/s)')
plt.title("GSM op 12 inch velg")

plt.show() # Toon de grafiek.