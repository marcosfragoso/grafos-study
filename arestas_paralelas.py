import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


def has_parallel_edges (G):
  for u in G.nodes:
    for v in G.nodes:
      if G.number_of_edges(u,v) > 1:
        return True
  return False


M = nx.MultiGraph()
M.add_edges_from([('x','y'),('x','y'),('y','x'),('x','w'),
                   ('y','w'),('z','w'),('w','z')])
edges = M.edges()

S = nx.Graph()
S.add_nodes_from(['x','y','z','w'])
S.add_edges_from([('x','y'),('x','w'),('x','z'),('y','z')])

P = nx.MultiGraph()
P.add_edges_from([('x','y'),('x','y'),('x','w'),
                   ('y','w'),('z','w'),('w','w')])

print(f"S possui arestas paralelas? {'Sim' if has_parallel_edges(S) else 'Não'}")
print(f"M possui arestas paralelas? {'Sim' if has_parallel_edges(M) else 'Não'}")
print(f"P possui arestas paralelas? {'Sim' if has_parallel_edges(P) else 'Não'}")

