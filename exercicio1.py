import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


# V(G) = {a,b,c,d,e,f} E(G) = {ab, bc, cd, ce, de, ef}
V = nx.Graph()
V.add_nodes_from(['a','b','c','d','e','f'])
V.add_edges_from([('a','b'),('b','c'),('c','d'),('c','e'),('d','e'),('e','f')])

draw_graph(V)