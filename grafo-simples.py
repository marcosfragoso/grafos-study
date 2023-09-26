import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph

# Grafo simples - não possui arestas paralelas e nem loops.

S = nx.Graph()
S.add_nodes_from(['x','y','z','w'])
S.add_edges_from([('x','y'),('x','w'),('x','z'),('y','z')])

draw_graph(S)