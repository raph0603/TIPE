import matrice as m
import gauss as g
import matplotlib.pyplot as plt
import numpy as np
import random

#-----------------IMPORTATION DES DONNEES-----------------#

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

Time_series = [int(item["Consommation"]) for item in dico]

#-----------------FONCTIONS-----------------#

def moyenne(tableau):
	return sum(tableau) / len(tableau)

def creer_matrices_S1_S2(X, Y, degree):
	# X = Les abscisses
	# Y = Les ordonnées
	S1 = [[0 for i in range(degree + 1)] for j in range(degree + 1)]
	S2 = [[0] for i in range(degree + 1)]
	for i in range(degree + 1):
		for j in range(degree + 1):
			# print("S1:", i, j, 2*degree - (i + j))
			# print([x ** (2*degree - (i + j)) for x in X])
			# print(sum([x ** (2*degree - (i + j)) for x in X]))
			# print("\n")
			S1[i][j] = sum([x ** (2*degree - (i + j)) for x in X])
		# print("S2 :", i, 0, degree - i)
		# print(list(zip(X, Y)))
		# print([x ** (degree - i) * y for x, y in zip(X, Y)])
		# print(sum([x ** (degree - i) * y for x, y in zip(X, Y)]))
		# print("\n")
		S2[i][0] = sum([x ** (degree - i) * y for x, y in zip(X, Y)])
	return S1, S2

def solution_MCO(X, Y, degree):
	S1, S2 = creer_matrices_S1_S2(X, Y, degree)
	S1_1 = g.inverse_matrice(S1)
	g.repr_matrice(S1_1)
	g.repr_matrice(S2)
	return m.produit_matrice(S1_1, S2)

def R2(X,Y):
	x_ = moyenne(X)
	y_ = moyenne(Y)
	s1 = 0
	s2 = 0
	s3 = 0
	for i in range(len(X)):
		s1+= (X[i]- x_)*(Y[i]-y_)
		s2+= (X[i]- x_)**2
		s3+= (Y[i]- y_)**2
	# print(s1,s2,s3)
	return (s1**2)/(s2*s3)

def prediction(X,Y,degree,nb_nodes):
	res = []
	for i in range(nb_nodes, len(X)):
		X_train = X[i - nb_nodes:i]
		Y_train = Y[i - nb_nodes:i]
		S = solution_MCO(X_train, Y_train, degree)
		res.append(sum([S[j][0] * X[i] ** (degree - j) for j in range(degree + 1)]))
	return res
	

def afficher_graphique_points_reliee(X, Y, degree):
	S = solution_MCO(X, Y, degree)
	x = [i / 10 for i in range(0, len(X)*10)]
	y = [sum([S[i][0] * x ** (degree - i) for i in range(degree + 1)]) for x in x]
	plt.scatter(X, Y)
	plt.plot(x, y,'r')
	plt.suptitle('R²: ' + str(R2(X, Y)))
	for abscisse, ordonnee in zip(X, Y):
		plt.plot([abscisse, abscisse], [ordonnee, sum([S[i][0] * abscisse ** (degree - i) for i in range(degree + 1)])], color ='blue', linewidth=1.5, linestyle="--")
	plt.show()

def afficher_graphique_pred(X, Y, degree, nb_nodes):
	plt.plot(X, Y, 'r')
	plt.plot(X[nb_nodes:], prediction(X, Y, degree, nb_nodes), 'b')
	plt.show()

#-----------------MAIN-----------------#
	
X = [i for i in range(0, len(Time_series))]
afficher_graphique_pred(X, Time_series, 1, 2)