import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph

#Mapa do nordeste

M = nx.MultiGraph()

M.add_nodes_from(['SE','AL','BA','PE','PB','RN','CE','PI','MA'])

M.add_edges_from([('SE', 'AL'),('SE','BA')])
M.add_edges_from([('AL', 'BA'),('AL','PE')])
M.add_edges_from([('BA', 'PE'),('BA','PI')])
M.add_edges_from([('PE', 'PI'),('PE','CE'),('PE','PB')])
M.add_edges_from([('PI', 'CE'),('PI','MA')])
M.add_edges_from([('PB', 'CE'),('PB','RN')])
M.add_edges_from([('CE', 'RN')])


draw_graph(M)
