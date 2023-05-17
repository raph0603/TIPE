# -*- coding: utf-8 -*-
import random
import matrice as m
import gauss as g
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

a = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]

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
	# g.repr_matrice(S1_1)
	return m.produit_matrice(g.inverse_matrice(S1), S2)

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

# def search_better_degree(X,Y,Calculated,degree,max):
# 	if Calculated == []: 
# 		S = solution_MCO(X, Y, degree)
# 		y = [sum([S[i][0] * x ** (degree - i) for i in range(degree + 1)]) for x in X]
# 		Calculated[degree-1] = R2(Y,y)
# 		print(Calculated[degree-1])
# 	else:
# 		S = solution_MCO(X, Y, degree)
# 		y = [sum([S[i][0] * x ** (degree - i) for i in range(degree + 1)]) for x in X]
# 		Calculated[degree-1] = R2(Y,y)
# 		print(Calculated[degree-1])
# 		moy = 5 + 

	

def afficher_graphique(X, Y, degree):
	S = solution_MCO(X, Y, degree)
	x = [i / 10 for i in range(0, 100)]
	y = [sum([S[i][0] * x ** (degree - i) for i in range(degree + 1)]) for x in x]
	plt.scatter(x, y)
	plt.plot(x, y, 'r',color='red')
	plt.show()

def afficher_graphique_points_reliee(X, Y, degree):
	S = solution_MCO(X, Y, degree)
	x = [i / 10 for i in range(0, len(X)*10)]
	y = [sum([S[i][0] * x ** (degree - i) for i in range(degree + 1)]) for x in x]
	plt.scatter(X, Y)
	plt.plot(x, y,'r')
	# plt.suptitle('R²: ' + str(R2(X, Y)))
	for abscisse, ordonnee in zip(X, Y):
		plt.plot([abscisse, abscisse], [ordonnee, sum([S[i][0] * abscisse ** (degree - i) for i in range(degree + 1)])], color ='blue', linewidth=1.5, linestyle="--")
	plt.show()

# S1, S2 = creer_matrices_S1_S2([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 2)
# m.repr_matrice(S1)
# m.repr_matrice(S2)
# S = solution_MCO([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 2)
# print("Solution MCO :", S)
# m.repr_matrice(S)
# afficher_graphique([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 2)

# # test avec des données formant une courbe quadratique
# X = [i for i in range(0, 10)]
# Y = [x ** 2 for x in X]
# afficher_graphique(X, Y, 2)

# # test avec des données formant une courbe cubique
# X = [i for i in range(0, 10)]
# Y = [x ** 3 for x in X]
# afficher_graphique(X, Y, 3)

# test avec des données aléatoires avec aussi du négatif
r = 0.4
for i in range(0,1):
	X = [j for j in range(0, 10)]
	Y = [x**4 +x ** 2 + 2 * x + 3 + 15 * (15 * r - 1) for x in X]
	afficher_graphique_points_reliee(X, Y, 10)	