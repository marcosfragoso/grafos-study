import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


def minimum_cost(coordinates):
    if coordinates is None: return None
    if not isinstance(coordinates, list): return None
    if coord_repetidas(coordinates): return None
    if not_tuplas(coordinates): return None

    grafo = cria_grafo(coordinates)
    if grafo is None: return None
    
    arvore_geradora = nx.minimum_spanning_tree(grafo, weight='dist')
    custo_min = 0
    for edge in arvore_geradora.edges(data=True):
        custo_min += edge[2]['dist']
    return grafo, custo_min

#
def cria_grafo(c):
    G = nx.MultiGraph()
    for node in c:
        G.add_node(node)
    
    for c1 in c:
        for c2 in c:
            if c1 == c2:
                continue
            if not isinstance(c1[0], int) or not isinstance(c1[1], int) or not isinstance(c2[0], int) or not isinstance(c2[1], int):
                return None
            if not G.has_edge(c1, c2):
                G.add_edge(c1, c2, dist=distancia(c1, c2))
    return G


def distancia(c1, c2):
    xa = c1[0]
    xb = c2[0]
    ya = c1[1]
    yb = c2[1]

    dist = ((xb - xa) ** 2 + (yb - ya) ** 2) ** (0.5)

    return int(dist)


def coord_repetidas(C):
    for c1 in C:
        contador = 0
        for c2 in C:
            if c1 == c2:
                contador += 1
        if contador > 1:
            return True
    return False


def not_tuplas(C):
    for c1 in C:
        if not isinstance(c1, tuple):
            return True
    return False



