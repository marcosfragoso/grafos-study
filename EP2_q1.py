import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


def warning_groups(g, t, m):

    if g is None or t is None or m is None: return None
    if t < 0 or m < 0: return None
    if not g.is_directed(): return None
    if not is_ponderado(g): return None

    componentes = list(nx.weakly_connected_components(g))
    componentes_validos = []
    for componente in componentes:
        if len(list(componente)) >= m:
            componentes_validos.append(list(componente))

    grupos = []
    for componente in componentes_validos:
        subgrafo = g.subgraph(componente)
        for aresta in subgrafo.edges(data=True):
            if aresta[2]['amount'] >= t:
                grupos.append(componente)
                break

    return grupos


def is_ponderado(G):
    if G.number_of_edges() == 0:
        return True
    arcos = G.edges(data=True)
    for cauda, cabeca, amount in arcos:
        if len(amount) > 0:
            return True
    return False