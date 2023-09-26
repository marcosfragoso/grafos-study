from busca_largura import bfs, G1
import networkx as nx
from utils.networkx_util import draw_graph
from collections import deque


G2 = nx.Graph()

G2.add_nodes_from(['a', 'b', 'c', 'd', 'e'])
G2.add_edges_from([('a', 'b'), ('a', 'c'), ('a', 'd'), ('c', 'b'), ('c', 'd'), ('c', 'e'), ('b', 'e'), ('d', 'e')])


def bfs_odd_cycles(G):
    p, l, t = bfs(G, list(G.nodes())[0])
    for key in l:
        for key2 in l:
            if key != key2 and l[key] == l[key2]:
                if G.has_edge(key, key2):
                    return True
    return False

print(bfs_odd_cycles(G2))
draw_graph(G2)