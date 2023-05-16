
# -*- coding: utf-8 -*-

def somme_matrice(A, B):
	"""retourne la somme de deux matrices"""
	am = len(A)
	an = len(A[0])
	bm = len(B)
	bn = len(B[0])
	if am != bm or an != bn:
		return None
	C = [[0 for j in range(an)] for i in range(am)]
	for i in range(am):
		for j in range(an):
			C[i][j] = A[i][j] + B[i][j]
	return C

def produit_matrice(A, B):
	"""retourne le produit de deux matrices"""
	am = len(A)
	an = len(A[0])
	bm = len(B)
	bn = len(B[0])
	if an != bm:
		print("Les matrices ne sont pas compatibles\n")
		return None
	C = [[0 for j in range(bn)] for i in range(am)]
	for i in range(am):
		for j in range(bn):
			for k in range(an):
				C[i][j] += A[i][k] * B[k][j]
	return C

def repr_matrice(M):
	"""affiche une matrice"""
	n = len(M)
	m = len(M[0])
	for i in range(n):
		for j in range(m):
			print("|", M[i][j],"|", end="")
		print("")
	print("\n")

def produit_scalaire_matrice(M, s):
	"""multiplie une matrice par un scalaire"""
	n = len(M)
	m = len(M[0])
	for i in range(n):
		for j in range(m):
			M[i][j] *= s
	return M

def inverse_lignes(M, i, j):
	"""inverse les lignes i et j de la matrice M"""
	temp = M[i]
	M[i] = M[j]
	M[j] = temp
	return M
	
def combinaison_lineaire_de_ligne(M, i, j, ci, cj):
	"""retourne la combinaison lineaire de la ligne i et de la ligne j de la matrice M par les coefficients ci et cj"""
	# print("L",i,"<-",ci,"*L",i,"+",cj,"*L",j)
	n = len(M)
	P = [[k == l for k in range(n)] for l in range(n)]
	if cj != 0:
		if ci != 0:
			P[i][i], P[i][j] = ci, cj
		else:
			P[i][j] = cj
	else:
		if ci != 0:
			P[i][i]= ci
	return produit_matrice(P, M)

def repr_matrice_augmentee(M, I):
	"""représente la matrice augmentée de M avec I"""
	nA, nI = len(M), len(I)
	mA, mI = len(M[0]), len(I[0])
	if nA != nI or mA != mI:
		return None
	for i in range(nA):
		for j in range(mA):
			print("|", M[i][j],"|", end="")
		print("░", end="")
		for j in range(mI):
			print("|", I[i][j],"|", end="")
		print("")
	print("\n")

def op_matrice_augmentee(func, args, matriceMI):
	"""réalise les opérations simultanéments sur les matrices M et I"""
	n = len(matriceMI)
	if n == 1:
		return func(*matriceMI, *args)
	elif n == 2:
		M = func(matriceMI[0], *args)
		I = func(matriceMI[1], *args)
		return M,I
	
def elimination_gauss(M,I):
	def elimination_colonne(i,j,M,I):
		n = len(M)
		for k in range(i,n):
			# print("sur la ligne ",k," -> ", M[k][j],": ", end='')
			if M[k][j] != 0:
				# print("ça marche")
				M,I = op_matrice_augmentee(inverse_lignes, [i,k], [M,I])
				# print("L",i, "<-> L",k)
				# repr_matrice_augmentee(M,I)
				break
			# print("on ne peut rien faire")
		if M[i][j] == 0:
			print("Pas inversible")
			return M,I
		else :
			for k in range(i+1, n):
				# print("i:",i, "k:",k)
				if M[k][j] != 0:
					M,I = op_matrice_augmentee(combinaison_lineaire_de_ligne, [k,i, 1, -(M[k][i]/M[i][j])], [M,I])
					# print("repr : matrice augmenté ( M | I )")
					# repr_matrice_augmentee(M,I)
			return M,I
	def elimination_colonne_sup(i,j,M,I):
		# print("je suis là")
		for k in range(0, i):
			# print("i:",i, "k:",k)
			if M[k][j] != 0:
				M,I = op_matrice_augmentee(combinaison_lineaire_de_ligne, [k,i, 1, -(M[k][i]/M[i][j])], [M,I])
				# print("repr : matrice augmenté ( M | I )")
				# repr_matrice_augmentee(M,I)
		return M,I
	def un_colonne(i,M,I):
		if M[j][j] != 1:
			M,I = op_matrice_augmentee(combinaison_lineaire_de_ligne, [j,j, 1/M[j][j], 0], [M,I])
			# print("repr : matrice augmenté ( M | I )")
			# repr_matrice_augmentee(M,I)
		return M,I
	for j in range(len(M)):
		M,I= elimination_colonne(j,j,M,I)
	for j in range(len(M)):
		M,I= elimination_colonne_sup(j,j,M,I)
	for j in range(len(M)):
		M,I= un_colonne(j,M,I)
	return M,I

def inverse_matrice(M):
	# print("repr : M")
	# repr_matrice(M)
	I = [[1 if i==j else 0 for i in range(len(M))] for j in range(len(M))]
	# print("repr : matrice augmenté ( M | I )")
	# repr_matrice_augmentee(M, I)
	M,I = elimination_gauss(M,I)
	# print("repr : matrice augmenté ( M | I )")
	# repr_matrice_augmentee(M,I)
	return I
		

# exemple = [[1,2, 3], [4, 5, 6], [7, 8, 10]]
# print("repr : M")
# repr_matrice(exemple)
# I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# print("repr : matrice augmenté ( exemple | I )")
# repr_matrice_augmentee(exemple, I)
# args = [I]
# print("repr : matrice augmenté 2 ( exemple | I )")
# op_matrice_augmentee(repr_matrice_augmentee, args, [exemple])
# args2 = [2,1,1,-(exemple[2][1]/exemple[1][1])]
# matriceMI = [exemple, I]
# res = op_matrice_augmentee(combinaison_lineaire_de_ligne, args2, matriceMI)
# print("repr : matrice augmenté ( res[0] | res[1] )")
# repr_matrice_augmentee(res[0], res[1])
# M,I = elimination_gauss(exemple,I)
# print("repr : matrice augmenté ( M | I )")
# repr_matrice_augmentee(M,I)
