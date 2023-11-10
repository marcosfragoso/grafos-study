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