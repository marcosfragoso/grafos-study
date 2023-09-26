import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph
from networkx.algorithms import isomorphism


G = nx.Graph()
H = nx.Graph()

G.add_nodes_from(['a','b','c','d','e','f','g'])
H.add_nodes_from(['h','i','j','k','l','m','n'])

G.add_edges_from([('a','b'),('b','c'),('c','d'),('c','f'),('f','e'),('g','f'),('g','a'),('g','b')])
H.add_edges_from([('h','n'),('n','j'),('j','k'),('l','k'),('l','m'),('l','i'),('i','j'),('i','n')])

GM = isomorphism.GraphMatcher(G,H)

print(GM.is_isomorphic())