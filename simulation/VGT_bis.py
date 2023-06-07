import matplotlib.pyplot as plt
import matrice as mat

#-----------------CLASSES-----------------#

class graph:

    def __init__(self, vertices):
        """Initialise le graphe avec le nombre de sommets donné"""
        self.V : int = vertices
        self.E : float = 0
        self.P : list[list[float]] = [[0 for column in range(vertices)] for row in range(vertices)]
        self.graph : list[list[int]] = [[0 for column in range(vertices)] for row in range(vertices)]

    def __repr__(self):
        return str(self.graph)
    
    def __str__(self):
        return str(self.graph)
    
    def __getitem__(self, i):
        return self.graph[i]
    
    def __setitem__(self, i, j, value):
        print("i :", i, "j :", j, "value :", value)

    def __len__(self):
        return self.V 
    
#-----------------FONCTIONS-----------------#

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


def is_visible(Y, i, j):
    if i>j: 
        return is_visible(Y, j, i)
    for k in range(i,j):
        if k != i and k != j:
            # print(Y[k], "<", Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i))
            if not(Y[k] < Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i)):
                return False
    return True

def visibility_graph(Y):
    g = graph(len(Y))
    for i in range(len(Y)):
        for j in range(len(Y)):
            if i != j:
                if is_visible(Y, i, j):
                    g[i][j] = 1
    return g

def plot_visibility_graph(Y,graph):
    for i in range(len(Y)):
        for j in range(len(Y)):
            if graph[i][j] == 1:
                plt.plot([i, j], [Y[i], Y[j]], 'r',color='red')
    plt.stem(range(len(Y)), Y)
    plt.show()

def is_voisin(g : graph, i, j):
    print("i :", i, "j :", j)
    print("g.graph[i][j] :", g.graph[i][j])
    return g.graph[i][j] == 1

def ki(g : graph, i):
    return sum(g.graph[i])

def jaccard(g: graph, i, j):
    inter = 0
    for k in range(len(g.graph[i])):
        if is_voisin(g, j, k):
            print("k :", k)
            inter += 1
    print("inter :", inter)
    return inter / (ki(g, i) + ki(g, j))


# def E(g : graph):
#     g.E = sum([ki(g, i) for i in range(len(g))]) / 2

def Pij(g : graph, i, j):
    return g[i][j] / ki(g, i)

# def P(g : graph):
    g.P = [[Pij(g, i, j) for j in range(len(g))] for i in range(len(g))]

def produit_mat_vect(Pt, v):
    res = []
    for i in range(len(Pt)):
        res.append(sum([Pt[i][j] * v[j] for j in range(len(Pt))]))
    return res

# def pi(Pt, i, t):
    if t == 0:
        return [1 if i == j else 0 for j in range(len(Pt))]
    else:
        return produit_mat_vect(Pt, pi(Pt, i, t-1))
    
# def Sij(g : graph, i, j , t):
    E(g)
    P(g)
    return ((ki(g,i)/(2*g.E)) * (pi(g.P, i, t)[j])) + ((ki(g,j)/(2*g.E)) * (pi(g.P, j, t)[i]))

# def Sij_better(g : graph, i, j , t):
    return sum([Sij(g, i, j, l) for l in range(t)])

def distance(i,j):
    return abs(i-j)

def y_(g : graph, Y):
    S = [(i,jaccard(g, i, len(g)-1)) for i in range(len(g)-1)]
    print("S:", S)
    stot = sum([s for (_,s) in S])
    print("stot:", stot)
    w = [s/stot for (_,s) in S]
    sorted(S, key=lambda x: x[1])
    print("S:", S)
    # ytp1 = ((Y[-1]-Y[S[0][0]])/(len(g)-1-S[0][0])) + Y[-1]
    ytp = [((Y[-1]-Y[S[i][0]])/(len(g)-1-S[i][0])) + Y[-1] for (i,_) in S]
    yntp = sum([w[i] * ytp[i] for i in range(len(ytp))])
    # w1 = 1/ distance(S[0][0], len(g))
    # w2 = distance(S[0][0], len(g)-1) / distance(S[0][0], len(g))
    # yntp1 = w1 * Y[-1] + w2 * ytp1
    return yntp

# def y_s(g : graph, Y):
    S = [(i,jaccard(g, i, len(g)-1)) for i in range(len(g)-1)]
    print("S:", S)
    stot = sum([s for (_,s) in S])
    print("stot:", stot)
    w = [s/stot for (_,s) in S]
    sorted(S, key=lambda x: x[1])
    print("S:", S)
    # ytp1 = ((Y[-1]-Y[S[0][0]])/(len(g)-1-S[0][0])) + Y[-1]
    ytp = [((Y[-1]-Y[S[i][0]])/(len(g)-1-S[i][0])) + Y[-1] for (i,_) in S]
    yntp = sum([w[i] * ytp[i] for i in range(len(ytp))])
    # w1 = 1/ distance(S[0][0], len(g))
    # w2 = distance(S[0][0], len(g)-1) / distance(S[0][0], len(g))
    # yntp1 = w1 * Y[-1] + w2 * ytp1
    # affiche le graphique
    for i in range(len(Y)):
        for j in range(len(Y)):
            if g.graph[i][j] == 1:
                plt.plot([i, j], [Y[i], Y[j]], 'r',color='red')
    plt.stem(range(len(Y)), Y)
    for i in range(len(ytp)):
        plt.stem(range(len(Y), len(Y)+1), [ytp[i]], "g")
        plt.plot([len(Y)-1, len(Y)], [Y[len(Y)-1], ytp[i]], 'r',color='blue')
    plt.stem(range(len(Y), len(Y)+1), [yntp], "red")
    plt.show()
    return ytp

def predict(Y, T):
    PTS = [y for y in Y]
    res = []
    for t in range(T):
        g = visibility_graph(PTS)
        plot_visibility_graph(PTS, g)
        PTS.append(y_(g, PTS))
        res.append(PTS[-1])
    return res

def plot_visibility_graph_pred(Y,graph, pred):
    for i in range(len(Y)):
        for j in range(len(Y)):
            if graph[i][j] == 1:
                plt.plot([i, j], [Y[i], Y[j]], 'r',color='red')
    plt.stem(range(len(Y)), Y)
    plt.stem(range(len(Y), len(Y)+len(pred)), pred, "g")
    plt.plot([len(Y)-1, len(Y)], [Y[len(Y)-1], pred[0]], 'r',color='green', linestyle='dashed')
    plt.plot(range(len(Y), len(Y)+len(pred)), pred , 'r',color='green', linestyle='dashed')
    plt.show()

def pred_seq(Y, nb_nodes):
    res = []
    for i in range(len(Y)-nb_nodes):
        g = visibility_graph(Y[i:i+nb_nodes])
        res.append(y_(g, Y[i:i+nb_nodes]))
    return res

def covariance(X, Y):
	n = len(X)
	x_ = 1/n * sum(X)
	m = len(Y)
	y_ = 1/m * sum(Y)
	return 1/n * sum([((X[i] - x_)**2)*(Y[i]-y_)  for i in range(len(X))])

def ecart_type(X):
	n = len(X)
	x_ = 1/n * sum(X)
	return (1/n * sum([(X[i] - x_)**2 for i in range(len(X))]))**0.5

def correlation(X, Y):
	return covariance(X, Y)/(ecart_type(X)*ecart_type(Y))

def plot_visibility_graph_pred_seq(Y,nb_nodes, pred):
    plt.plot(range(len(Y)), Y , 'r',color='red')
    plt.plot(range(nb_nodes,len(Y)), pred , 'r',color='blue')
    print("correlation", correlation(Y[nb_nodes:], pred))
    plt.legend(["Consommation d'électricité en MW au cours du temps", "Prédiction"])
    plt.xlabel("Temps (en jours)")
    plt.ylabel("Consommation d'électricité (en MW)")
    plt.show()

#-----------------TEST-----------------#

# Y = [1,5,4,6,7,5,3,6]

# g = visibility_graph(Y)
# print(Sij(g, 0, 1, 1))
# plot_visibility_graph(Y,g.graph)
# print(y_(g, Y))
# plot_visibility_graph_pred(Y,g.graph,predict(Y,1))
# g = visibility_graph(Y)
# y_s(g, Y)
# plot_visibility_graph_pred(Time_series[60:120], visibility_graph(Time_series[60:120]).graph, predict(Time_series[60:120], 1))
# plot_visibility_graph_pred_seq(Time_series[60:120], 30, pred_seq(Time_series[60:120], 30))
# pred_30 = pred_seq(Time_series[60:120], 30)
# plot_visibility_graph_pred(Time_series[330:], visibility_graph(Time_series[330:]).graph, predict(Time_series[330:], 1))
plot_visibility_graph_pred_seq(Time_series, 30, pred_seq(Time_series, 30))
# plot_visibility_graph_pred(Time_series[100:115], visibility_graph(Time_series[100:115]).graph, predict(Time_series[100:115], 1))
# plot_visibility_graph_pred_seq(Time_series[100:115], 10, pred_seq(Time_series[100:115], 10))