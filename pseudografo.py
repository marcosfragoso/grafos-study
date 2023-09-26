import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph

# Todo pseudografo possui loop, e também podem possuir arestas paralelas

P = nx.MultiGraph()
P.add_edges_from([('x','y'),('x','y'),('x','w'),
                   ('y','w'),('z','w'),('w','w')])

draw_graph(P)