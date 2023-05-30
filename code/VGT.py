import matplotlib.pyplot as plt
import igraph as ig
import matrice as mat

class graph:

    def __init__(self, vertices):
        """Initialise le graphe avec le nombre de sommets donné"""
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

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

Time_series = [int(item["Consommation"]) for item in dico] # extraction de la consommation

def is_visible(Y, i, j):
    if i>j: 
        return is_visible(Y, j, i)
    for k in range(i,j):
        if k != i and k != j:
            print(Y[k], "<", Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i))
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

def plot_visibility_graph_pred(Y,graph, pred):
    for i in range(len(Y)):
        for j in range(len(Y)):
            if graph[i][j] == 1:
                plt.plot([i, j], [Y[i], Y[j]], 'r',color='red')
    plt.stem(range(len(Y)), Y)
    plt.stem(len(Y), pred, "g")
    plt.plot([len(Y)-1, len(Y)], [Y[len(Y)-1], pred], 'r',color='green', linestyle='dashed')
    plt.show()

def vg(graph):
    g = ig.Graph()
    g.add_vertices(len(graph))
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                g.add_edges([(i,j)])
    return g

def plot_igraph(Y,graph):
    g = vg(graph)
    g.vs["label"] = range(len(Y))
    g.vs["name"] = range(len(Y))
    g.vs["name"] = [str(i) for i in g.vs["name"]]
    g.vs["label"] = [str(i) for i in g.vs["label"]]
    ig.plot(g, bbox=(300,300))
    return g

def Pxy(g, x, y):
    return g[x][y] / sum(g[x])

def P_matrix(g):
    P = [[0 for column in range(len(g))] for row in range(len(g))]
    for i in range(len(g)):
        for j in range(len(g)):
            P[i][j] = Pxy(g, i, j)
    return P

def produit_mat_vect(P, v):
    """P already transposed"""
    res = []
    for i in range(len(P)):
        res.append(sum([P[i][j] * v[j] for j in range(len(P))]))
    return res

def Pi_x(P, x, t):
    """P already transposed"""
    if t == 0:
        return [1 if i == x else 0 for i in range(len(P))]
    else:
        pixt_1 = Pi_x(P, x, t-1)
        print("pixt_1 :", pixt_1)
        print("P :", P)
        print("produit :", produit_mat_vect(P, pixt_1))
        return produit_mat_vect(P, pixt_1)
    
def k_x(g, x):
    return sum(g[x])

def nb_E_2(g):
    return sum([sum(g[i]) for i in range(len(g))])

def S_LRW_xy(g, Pt, x, y, t):
    print("Pt :", Pt)
    pi_xyt = Pi_x(Pt, x, t)
    pi_yxt = Pi_x(Pt, y, t)
    print("pi_xyt :", pi_xyt)
    print("pi_yxt :", pi_yxt)
    return (k_x(g,x)/nb_E_2(g)) * pi_xyt[y] + (k_x(g,y)/nb_E_2(g)) * pi_yxt[x]

def S_SRW_xy(g, x, y, t):
    Pt = mat.transposee_matrice(P_matrix(g))
    S_xy = 0
    for i in range(t+1):
        S_xy += S_LRW_xy(g, Pt, x, y, i)
        print("S_xy :", S_xy)
    return S_xy

def node_dist(x,y):
    return abs(x-y)

def y_n1(S, Y):
    ind = -1
    y_max = 0
    for i in range(len(S)):
        if S[i] > y_max:
            y_max = S[i]
            ind = i
    print("ind :", ind)
    print("y_max :", y_max)
    print("Y[-1] :", Y[-1])
    print("Y[ind] :", Y[ind])
    print("len(Y) :", len(Y))
    print("len(Y)-1-ind :", len(Y)-1-ind)
    print(Y[-1], "+", (((Y[-1]-Y[ind])/(len(Y)-1-ind))), "*" , len(Y)-len(Y)-1, ":", Y[-1] + (((Y[-1]-Y[ind])/(len(Y)-1-ind))) * (len(Y)-(len(Y)-1)))
    return Y[-1] + (((Y[-1]-Y[ind])/(len(Y)-1-ind))) * (len(Y)-(len(Y)-1))

def predict(Y, N):
    """N is the number of points to predict"""
    pred = []
    PTS = [i for i in Y]
    for i in range(N):
        g = visibility_graph(PTS).graph
        S_SRW = [S_SRW_xy(g,j,len(PTS)-1, node_dist(j,len(PTS)-1)) for j in range(len(PTS)-1)]
        yn__1 = y_n1(S_SRW, PTS)
        pred.append(yn__1)
        PTS.append(yn__1)
    return pred
    

# Test random
Y = [10,5,4,15,3,8]


print(is_visible(Y, 0, 2))
g = visibility_graph(Y).graph
print(g)
plot_visibility_graph(Y,g)
graphn = plot_igraph(Y,g)
graphn.write_svg("test.svg")

S = S_SRW_xy(g, 1, 3, 5)

S_SRW = [S_SRW_xy(g,i,len(Y)-1, node_dist(i,len(Y)-1)) for i in range(len(Y)-1)]

yn__1 = y_n1(S_SRW, Y)

plot_visibility_graph_pred(Y,g, yn__1)

pred = predict(Y, 5)

# Test on Time_series

# gts = visibility_graph(Time_series).graph
# print(gts)
# plot_visibility_graph(Time_series,gts)
# graphn = plot_igraph(Time_series,gts)
# ig.plot(graphn, bbox=(300,300))