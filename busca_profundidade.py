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
        else:
            S.popleft()  # Remove o vértice do topo se não houver vizinhos não pintados

    return p, f, t


G2 = nx.read_graphml(filename2)
r = 'n0'
p2,f2,t2 = dfs(G2,r)
print(f"Função predecessor: {p2}")
print(f"Função tempo de adição na árvore: {f2}")
print(f"Função tempo de remoção da pilha: {t2}")
