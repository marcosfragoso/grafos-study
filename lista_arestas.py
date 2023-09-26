import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


l_edges = ["b a", "a c", "c d", "c e", "d b", "d f", "f e", "b e"]
G_edge_list = nx.parse_edgelist(l_edges)
draw_graph(G_edge_list)