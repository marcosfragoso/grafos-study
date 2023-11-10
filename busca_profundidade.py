import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph
import os
from collections import deque
from random import choice

filename2 = "s-u-cy-sc-p-06.graphml"


def dfs(g, r):
    i = 0
    S = deque()
    i += 1
    painted = [r]
    f = {r: i}
    t = {}
    S.appendleft(r)  # Pilha: adiciona à esquerda
    p = []
    new_p = []
    ## Edite o trecho a seguir para completar a implementação
    while S:
        x = S[0]  # Pilha: elemento no topo
        i += 1
        not_painted = [v for v in g.neighbors(x) if v not in painted]
        if not_painted:
            v = not_painted[0]  # Pega o primeiro vértice não pintado
            i += 1
            painted.append(v)
            f[v] = i
            t[v] = x
            S.appendleft(v)
            p.append(v)
            new_p.append((x, v))
        else:
          t[x] = i
          S.popleft()
    return new_p, f, t
