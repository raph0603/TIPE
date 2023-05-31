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

def ki(g : graph, i):
    return sum(g.graph[i])

def E(g : graph):
    g.E = sum([ki(g, i) for i in range(len(g))]) / 2

def Pij(g : graph, i, j):
    return g[i][j] / ki(g, i)

def P(g : graph):
    g.P = [[Pij(g, i, j) for j in range(len(g))] for i in range(len(g))]

def produit_mat_vect(Pt, v):
    res = []
    for i in range(len(Pt)):
        res.append(sum([Pt[i][j] * v[j] for j in range(len(Pt))]))
    return res

def pi(Pt, i, t):
    if t == 0:
        return [1 if i == j else 0 for j in range(len(Pt))]
    else:
        return produit_mat_vect(Pt, pi(Pt, i, t-1))
    
def Sij(g : graph, i, j , t):
    E(g)
    P(g)
    return ((ki(g,i)/(2*g.E)) * (pi(g.P, i, t)[j])) + ((ki(g,j)/(2*g.E)) * (pi(g.P, j, t)[i]))

def Sij_better(g : graph, i, j , t):
    return sum([Sij(g, i, j, l) for l in range(t)])

def distance(i,j):
    return abs(i-j)

def y_(g : graph, Y):
    S = [Sij(g, i, len(g)-1, abs(i - len(g)-1)) for i in range(len(g)-1)]
    print("S:", S)
    ind = 0
    max = 0
    for i in range(len(S)):
        if S[i] > max:
            ind = i
            max = S[i]
    ytp1 = ((Y[-1]-Y[ind])/(len(g)-1-ind)) + Y[-1]
    w1 = 1/ distance(ind, len(g))
    w2 = distance(ind, len(g)-1) / distance(ind, len(g))
    yntp1 = w1 * Y[-1] + w2 * ytp1
    return yntp1

def predict(Y, T):
    PTS = [y for y in Y]
    res = []
    for t in range(T):
        g = visibility_graph(PTS)
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

def plot_visibility_graph_pred_seq(Y,nb_nodes, pred):
    plt.plot(range(len(Y)), Y , 'r',color='red')
    plt.plot(range(nb_nodes,len(Y)), pred , 'r',color='blue')
    plt.show()

#-----------------TEST-----------------#

Y = [1,5,4,6,7,2,3,9]

g = visibility_graph(Y)
print(Sij(g, 0, 1, 1))
plot_visibility_graph(Y,g.graph)
print(y_(g, Y))
plot_visibility_graph_pred(Y,g.graph,predict(Y,1))
# plot_visibility_graph_pred(Time_series[60:120], visibility_graph(Time_series[60:120]).graph, predict(Time_series[60:120], 1))
# plot_visibility_graph_pred_seq(Time_series[60:120], 30, pred_seq(Time_series[60:120], 30))
# pred_30 = pred_seq(Time_series[60:120], 30)
# plot_visibility_graph_pred(Time_series[330:], visibility_graph(Time_series[330:]).graph, predict(Time_series[330:], 1))
# plot_visibility_graph_pred_seq(Time_series, 30, pred_seq(Time_series, 30))
# plot_visibility_graph_pred(Time_series[100:115], visibility_graph(Time_series[100:115]).graph, predict(Time_series[100:115], 1))
# plot_visibility_graph_pred_seq(Time_series[100:115], 10, pred_seq(Time_series[100:115], 10))