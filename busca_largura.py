import networkx as nx
from utils.networkx_util import draw_graph
from collections import deque

filename1 = "s-u-cy-sc-p-06.graphml"

def bfs(g, r):
    i = 0
    Q = deque()
    i += 1
    painted = [r]
    l = {r: 0}
    t = {r: i}
    Q.append(r)  # Fila: adiciona a direita
    p = []
    new_p = []
    ## Edite o trecho a seguir para completar a implementação
    while Q:
        x = Q[0]  # Fila: elemento da frente
        not_painted = [v for v in g.neighbors(x) if v not in painted]
        if not_painted:
            v = not_painted[0]
            i += 1
            painted.append(v)
            l[v] = l[x] + 1
            t[v] = i
            p.append(v)
            Q.append(v)
            new_p.append((x, v))
        else:
            Q.popleft()

    return new_p, l, t

G1 = nx.read_graphml(filename1)
r = 'n0'
#p1,l1,t1 = bfs(G1,r)
#print(f"Função predecessor: {p1}")
#print(f"Função nível: {l1}")
#print(f"Função tempo: {t1}")
#not_edges_p1 = [e for e in G1.edges if (e[0],e[1]) not in p1 and (e[1],e[0]) not in p1]

'''draw_graph(G1,title=f"Árvore BFS com raiz {r}",
           eset=[p1,not_edges_p1],
           esetcolor=["red","lightgray"],
           esetlabel=["Arestas da árvore","Arestas da co-árvore"])
           '''

#print(G1.nodes())
#bfs(G1, r)