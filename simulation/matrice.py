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
	assert am != bn # les matrices ne sont pas compatibles
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

def transposee_matrice(a):
	"""retourne la transposee d'une matrice"""
	n = len(a)
	m = len(a[0])
	b = [[0 for j in range(n)] for i in range(m)]
	for i in range(n):
		for j in range(m):
			b[j][i] = a[i][j]
	return b

def determinant_matrice(a):
	"""retourne le determinant d'une matrice"""
	n = len(a)
	m = len(a[0])
	if n != m:
		print("La matrice n'est pas carree\n")
		return None
	if n == 1:
		return a[0][0]
	if n == 2:
		return a[0][0] * a[1][1] - a[0][1] * a[1][0]
	det = 0
	for j in range(n):
		b = [[a[l+1][k + (k >= j)] for k in range(n-1)] for l in range(n-1)]
		det += (-1) ** j * a[0][j] * determinant_matrice(b)
	return det

def comatrice_matrice(a):
	"""retourne la comatrice d'une matrice"""
	n = len(a)
	m = len(a[0])
	if n != m:
		print("La matrice n'est pas carree\n")
		return None
	b = [[0 for j in range(n)] for i in range(n)]
	for i in range(n):
		for j in range(n):
			c = [[0 for k in range(n - 1)] for l in range(n - 1)]
			for k in range(n):
				for l in range(n):
					if k != i and l != j:
						c[k - (k > i)][l - (l > j)] = a[k][l]
			b[i][j] = determinant_matrice(c) * (-1) ** (i + j)
	return b

def produit_scalaire_matrice(s, a):
	"""multiplie une matrice par un scalaire"""
	n = len(a)
	m = len(a[0])
	for i in range(n):
		for j in range(m):
			a[i][j] *= s
	return a

def inverse_matrice(a):
	"""retourne l'inverse d'une matrice"""
	det = determinant_matrice(a)
	if det == 0:
		print("La matrice n'est pas inversible\n")
		return None
	b = comatrice_matrice(a)
	# repr_matrice(b)
	b = transposee_matrice(b)
	# repr_matrice(b)
	# print(1/det)
	b = produit_scalaire_matrice(1 / det, b) # type: ignore
	return b

matrice = [[5, 7, -3], [4, 2, -1], [9, -4, 6]]
repr_matrice(matrice)
# c = comatrice_matrice(matrice)
# repr_matrice(c)
det = determinant_matrice(matrice)
print(det)
# print(1 / det)
# repr_matrice(transposee_matrice(comatrice_matrice(matrice)))
# inv = inverse_matrice(matrice)
# repr_matrice(inv)