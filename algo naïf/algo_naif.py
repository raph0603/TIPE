import numpy as np
from matplotlib.dates import (YEARLY, DateFormatter, rrulewrapper, RRuleLocator, drange)
from matplotlib import pyplot as plt
from matplotlib import dates
from sklearn.linear_model import LinearRegression

def lecture(nom, separateur=","):
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
	
dico = lecture("eCO2mix_RTE_Annuel-Definitif_2016.csv")

def affiche_tab(dico):
	for item in dico:
		print(item)

# affiche_tab(dico)

def conversion_date(dico):
	return dates.date2num([(item["Date"]) for item in dico])

Valeurs = conversion_date(dico)
conso = [int(item["Consommation"]) for item in dico]
# print(type(conversion_date(dico)))

tableau = dates.date2num(["2016-01-01","2016-01-02","2016-01-03"])
cc = [2,3,1]
# plt.plot(tableau, np.array(cc))



fig, ax = plt.subplots()
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
loc = RRuleLocator(rule)
formatter = DateFormatter('%m/%d/%y')
plt.plot(Valeurs, np.array(conso))
ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
plt.show()