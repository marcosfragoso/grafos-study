import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph

M = nx.MultiGraph()
M.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'),
                   ('y','w'),('z','w'),('w','z')])
edges = M.edges()

draw_graph(M)

