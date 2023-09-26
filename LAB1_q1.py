# Escreva uma função, **non_neighbor**, que recebe um grafo *G* como entrada, 
# um identificador *v* de um vértice deste grafo e retorna uma lista com os 
# vértices que não são vizinhos de *v*. Se *v* não pertence ao grafo ou 
# *G* é nulo ou *None*, a função deve retornar *None*.

def non_neighbor (G,v):

  if G is None or v not in G.nodes:
    return None
  
  if len(G.edges) == 0:
    return [0]

  naoVizinhos = []
  
  for vertice in G.nodes:
    if G.has_edge(v, vertice) == False:
      naoVizinhos.append(vertice)

  return naoVizinhos