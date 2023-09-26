# Escreva uma função, graph_types, que classifica um grafo não-direcionado, 
# considerando as seguintes categorias: 
#     Simples, Multigrafo, Pseudografo, Trivial, Nulo, Vazio, Bipartido. 
# Um mesmo grafo pode possuir mais de uma destas características. 
# Por exemplo, o grafo Trivial é também um grafo Simples, Vazio e Bipartido. 
# A função deve retornar uma lista com todas as classificações que podem ser 
# dadas ao grafo recebido como parâmetro, em qualquer ordem.
# Dicas:
#    Use o método number_of_edges da classe Graph para determinar a quantidade de arestas 
#    entre dois vértices (ver exercícios resolvidos Aula 02)
#    Use a função number_of_selfloops da seção Functions de NetworkX para determinar 
#    se o grafo possui loops
#    Use a função is_bipartite para testar se o grafo é bipartido

import networkx as nx

def tem_arestas_paralelas(G):
  for x in G.nodes:
    for y in G.nodes:
      if G.number_of_edges(x, y) > 1:
        return True
  return False


def graph_types (G):
  
  graph_types = []

  if not tem_arestas_paralelas(G) and nx.number_of_selfloops(G) < 1:
    graph_types.append("Simples")
  if tem_arestas_paralelas(G) and nx.number_of_selfloops(G) < 1:
    graph_types.append("Multigrafo")
  if nx.number_of_selfloops(G) >= 1:
    graph_types.append("Pseudografo")
  if nx.number_of_nodes(G) == 1 and nx.number_of_edges(G) == 0:
    graph_types.append("Trivial")
  if nx.number_of_nodes(G) == 0:
    graph_types.append("Nulo")
  if nx.number_of_edges(G) == 0:
    graph_types.append("Vazio")
  if nx.bipartite.is_bipartite(G):
    graph_types.append("Bipartido")

  return graph_types