import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


M = nx.MultiDiGraph()

M.add_nodes_from(['SE','AL','BA','PE','PB','RN','CE','PI','MA'])

M.add_edges_from([('SE', 'AL'), ('AL', 'SE')])
M.add_edges_from([('SE', 'BA'), ('BA', 'SE')])
M.add_edges_from([('AL', 'BA'), ('BA', 'AL')])
M.add_edges_from([('AL', 'PE'), ('PE', 'AL')])
M.add_edges_from([('BA', 'PE'), ('PE', 'BA')])
M.add_edges_from([('BA', 'PI'), ('PI', 'BA')])
M.add_edges_from([('PE', 'PI'), ('PI', 'PE')])
M.add_edges_from([('PE', 'CE'), ('CE', 'PE')])
M.add_edges_from([('PE', 'PB'), ('PB', 'PE')])
M.add_edges_from([('PI', 'CE'), ('CE', 'PI')])
M.add_edges_from([('PI', 'MA'), ('MA', 'PI')])
M.add_edges_from([('PB', 'CE'), ('CE', 'PB')])
M.add_edges_from([('PB', 'RN'), ('RN', 'PB')])
M.add_edges_from([('CE', 'RN'), ('RN', 'CE')])

for v in M.nodes:
  print(f">Vértice {v}:<")
  print(f'Grau de Entrada: {M.in_degree(v)}', end=' / ')
  print(f'Grau de Saída: {M.out_degree(v)}')
  print(f'Arcos entrada: {M.in_edges(v)}', end=' / ')
  print(f'Arcos saída: {M.out_edges(v)}')
  print(f'Vizinhos de entrada: {list(M.predecessors(v))}', end=' / ')
  print(f'Vizinhos de saída: {list(M.successors(v))}')


# Grafo base = to_undirected
draw_graph(M.to_undirected(as_view=True))
