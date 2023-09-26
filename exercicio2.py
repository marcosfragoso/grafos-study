import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


# Pontes de Konigsberg
P = nx.MultiGraph()

P.add_nodes_from(['Ilha B', 'Ilha A', 'Margem C', 'Margem D'])
P.add_edges_from([('Ilha B', 'Ilha A'),('Ilha B', 'Margem D'),('Ilha B', 'Margem C'),
                  ('Margem C','Ilha A'),('Ilha A', 'Margem C'), ('Ilha A', 'Margem D'),
                  ('Margem D','Ilha A')])


draw_graph(P)