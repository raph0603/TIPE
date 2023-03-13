# -*- coding: utf-8 -*-

def somme_matrice(a, b):
	"""retourne la somme de deux matrices"""
	am = len(a)
	an = len(a[0])
	bm = len(b)
	bn = len(b[0])
	if am != bm or an != bn:
		return None
	c = [[0 for j in range(an)] for i in range(am)]
	for i in range(am):
		for j in range(an):
			c[i][j] = a[i][j] + b[i][j]
	return c

def produit_matrice(a, b):
	"""retourne le produit de deux matrices"""
	am = len(a)
	an = len(a[0])
	bm = len(b)
	bn = len(b[0])
	if an != bm:
		print("Les matrices ne sont pas compatibles\n")
		return None
	c = [[0 for j in range(bn)] for i in range(am)]
	for i in range(am):
		for j in range(bn):
			for k in range(an):
				c[i][j] += a[i][k] * b[k][j]
	return c

def repr_matrice(a):
	"""affiche une matrice"""
	n = len(a)
	m = len(a[0])
	for i in range(n):
		for j in range(m):
			print("|", a[i][j],"|", end="")
		print("")
	print("\n")

def produit_scalaire_matrice(s, a):
	"""multiplie une matrice par un scalaire"""
	n = len(a)
	m = len(a[0])
	for i in range(n):
		for j in range(m):
			a[i][j] *= s
	return a

def inverse_lignes(i, j, M):
	n = len(M)
	P = [[1 if (l == k and (l != i or l != j)) or ((l == i or l == j) and (k == n-i-1 or k == n-j-1)) else 0 for k in range(n)] for l in range(n)]
	return produit_matrice(P, M)
	
def combinaison_lineaire_de_ligne(i, j, M, ci,cj):
	n = len(M)
	P = [[k == l for k in range(n)] for l in range(n)]
	P[]