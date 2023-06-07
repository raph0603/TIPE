import csv
import time
import datetime

# Nom du fichier CSV contenant les données
filename = "eco2mix_2012.csv"

# Collecte des données
data = []

def season(day, month):
    if month >= 3 and month <= 5 and day >=1 and day <=31:
        return 0
    elif month >= 6 and month <= 8 and day >=1 and day <=31:
        return 1
    elif month >= 9 and month <= 11 and day >= 1 and day <=31:
        return 2
    elif (month == 12 or (month >=1 and month <=2)) and day >=1 and day<=31:
        return 3
    else:
        return -1

# Ouverture du fichier CSV
with open(filename, "r", encoding = "utf-8") as file:
    # Lecture du contenu du fichier CSV
    clefs = file.readline().strip("\n")
    donnees = file.readlines()
    file.close()
    clefs= clefs.split(",")
    nb_clefs = len(clefs)

    for ligne in donnees:
        dico = {}
        ligne = ligne.strip("\n").split(",")
        for i in range(nb_clefs) :
            dico[clefs[i]] = ligne[i]

        heures = dico["Heures"].split(":")
        heure = int(heures[0])
        minute = int(heures[1])
        if minute == 15 or minute == 45: continue
        date = dico["Date"].split("-")
        annee = int(date[0])
        mois = int(date[1])
        jour = int(date[2])
        if mois == 2 and jour == 29 : continue
        consommation = float(dico["Consommation"])
        date_obj = datetime.date(annee, mois, jour)
        jour_semaine = date_obj.weekday()
        dico = {"jour" : jour,
                "mois": mois,
                "annee" : annee,
                "heure": heure,
                "minute" : minute,
                "jour_semaine": jour_semaine,
                "saison": season(jour,mois),
                "consommation": consommation
                }
        data.append(dico)
    # Parcours des lignes du fichier CSV
    # for row in donnees:
    #     # Extraction des variables pertinentes
    #     heures = row["Heures"].split(":")
    #     heure = int(heures[0])
    #     minute = int(heures[1])
    #     if minute == 15 or minute == 45: continue
    #     date = row["Date"].split("-")
    #     annee = int(date[0])
    #     mois = int(date[1])
    #     jour = int(date[2])
    #     if mois == 2 and jour == 29 : continue
    #     consommation = float(row["Consommation"])

    #     date_obj = datetime.date(annee, mois, jour)
    #     jour_semaine = date_obj.weekday()
        
    #     # Ajout des données collectées à la liste
    #     data.append({
    #         "jour" : jour,
    #         "mois": mois,
    #         "annee" : annee,
    #         "heure": heure,
    #         "jour_semaine": jour_semaine,
    #         "saison": season(jour,mois),
    #         "consommation": consommation
    #     })

# Affichage des données collectées
print("Données collectées :")
for entry in data:
    print(entry)

# affichage de la consommation moyenne par saison
consommation_saison = [0,0,0,0]
nb_jours_saison = [0,0,0,0]
for entry in data:
    consommation_saison[entry["saison"]] += entry["consommation"]
    nb_jours_saison[entry["saison"]] += 1

for i in range(4):
    consommation_saison[i] /= nb_jours_saison[i] # type: ignore

print("Consommation moyenne par saison :" , consommation_saison)

# Affichage de la consommation moyenne par jour de la semaine
consommation_jour_semaine = [0,0,0,0,0,0,0]
nb_jours_semaine = [0,0,0,0,0,0,0]
for entry in data:
    consommation_jour_semaine[entry["jour_semaine"]] += entry["consommation"]
    nb_jours_semaine[entry["jour_semaine"]] += 1

for i in range(7):
    consommation_jour_semaine[i] /= nb_jours_semaine[i] # type: ignore
    
print("Consommation moyenne par jour de la semaine :" , consommation_jour_semaine)

# Affichage de la consommation moyenne par heure
consommation_heure = [0]*24
nb_jours_heure = [0]*24
for entry in data:
    consommation_heure[entry["heure"]] += entry["consommation"]
    nb_jours_heure[entry["heure"]] += 1

for i in range(24):
    consommation_heure[i] /= nb_jours_heure[i] # type: ignore

print("Consommation moyenne par heure :" , consommation_heure)

# Affichage de la consommation sur un jour donné avec pyplot
import matplotlib.pyplot as plt

# Collecte des données
consommation = []
for entry in data:
    if entry["jour"] == 4 and entry["mois"] == 6 and entry["annee"] == 2012:
        consommation.append(entry["consommation"]) 

# Affichage de la consommation
plt.plot(consommation)
plt.show()
