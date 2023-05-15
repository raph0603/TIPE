import matplotlib.pyplot as plt

class graph:

    def __init__(self, vertices):
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
    
def is_between(Y, i, k, j):
    if Y[k] >= Y[i] + (Y[j] - Y[i]) * (k - i) / (j - i):
        return False

def visibility_graph(Y):
    g = graph(len(Y))
    for i in range(len(Y)):
        for j in range(len(Y)):
            if i != j:
                visible = True
                for k in range(len(Y)):
                    if k != i and k != j:
                        if is_between(Y, i, k, j):
                            visible = False
                if visible:
                    g[i][j] = 1
    return g

def afficher_graphique(X, Y):
    plt.scatter(X, Y)
    plt.show()
