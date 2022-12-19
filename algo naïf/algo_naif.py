import numpy as np
from matplotlib.dates import (YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
from matplotlib import pyplot as plt
from matplotlib import dates
from sklearn.linear_model import LinearRegression

def lecture(nom, separateur=","):
    """Lecture d'un fichier csv et renvoie une liste de dictionnaires"""
    fichier = open(nom, "r", encoding = "utf-8")
    clefs = fichier.readline().strip("\n")
    donnees = fichier.readlines()
    fichier.close()
    clefs= clefs.split(separateur)
    nb_clefs = len(clefs)
    liste_dico = []
    for ligne in donnees:
        dico = {}
        ligne = ligne.strip("\n").split(separateur)
        for i in range(nb_clefs) :
            dico[clefs[i]] = ligne[i]
        liste_dico.append(dico)
    return liste_dico
	
dico = lecture("eCO2mix_RTE_Annuel-Definitif_2016.csv") # importation des données

def affiche_tab(dico):
    """Affiche le contenu d'un tableau de dictionnaires"""
    [print(item) for item in dico]

affiche_tab(dico)

def conversion_date(dico):
    """Conversion sous un autre format de la date"""
    return dates.date2num([(item["Date"]) for item in dico])

Valeurs = conversion_date(dico) # conversion de la date
conso = [int(item["Consommation"]) for item in dico] # extraction de la consommation
# print(type(conversion_date(dico)))

tableau = dates.date2num(["2016-01-01","2016-01-02","2016-01-03"]) # tableau de test
cc = [2,3,1] # tableau de test
# plt.plot(tableau, np.array(cc))

# Affichage de la courbe

x = np.array(Valeurs).reshape((-1, 1)) 
y = np.array(conso)
model = LinearRegression().fit(x, y)
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

fig, ax = plt.subplots()
rule = rrulewrapper(YEARLY, byeaster=1, interval=3)
loc = RRuleLocator(rule)
formatter = DateFormatter('%d-%m-%y')
ax.plot(Valeurs, np.array(conso))
ax.plot(Valeurs, [model.intercept_ + model.coef_ * i for i in Valeurs]) # affichage de la droite de régression
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
plt.show()