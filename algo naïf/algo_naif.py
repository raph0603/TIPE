def lecture(nom, separateur=","):
	fichier = open(nom, "r", encoding = "utf-8")
	clefs = fichier.readline().strip("\n")
	donnees = fichier.readlines()
	fichier.close()
	clefs= clefs.split(separateur)
	nb_clefs = len(clefs)
	dico = dict()
	for i in range(nb_clefs):
		dico[clefs[i]] = []
	for ligne in donnees:
		ligne = ligne.strip("\n").split(separateur)
		for i in range(nb_clefs) :
			dico[clefs[i]].append(ligne[i])
	return dico

	
dico = lecture("eCO2mix_RTE_Annuel-Definitif_2016.csv")