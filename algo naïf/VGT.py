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
    
def is_between(Y, i, k, j):
    print(Y[k], "<", Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i))
    if Y[k] < Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i):
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

# Test random
Y = [1,3,2,4]

def is_visible(Y, i, j):
    if i>j: 
        return is_visible(Y, j, i)
    for k in range(i,j,1):
        if k != i and k != j:
            print(Y[k], "<", Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i))
            if Y[k] < Y[j] + (Y[i] - Y[j]) * (j - k) / (j - i):
                return False
    return True

print(is_visible(Y, 0, 2))
print(visibility_graph(Y))