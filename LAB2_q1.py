# Implemente a função **triangles** que recebe um grafo simples G como entrada e 
# retorna uma lista com grupos de 3 vértices que são mutuamente adjacentes entre si.
# Como exemplo, considere o grafo G, onde:
#
#    V(G) = {0,1,2,3}
#    E(G) = {01,02,12,13,23}
#
# Este grafo possui dois grupos de vértices mutuamente adjacentes. Portanto, a função deverá retornar a seguinte lista:
#
#    [[0,1,2], [1,2,3]]
#
# Os vértices e as listas não precisam estar necessariamente na nesta ordem.

import networkx as nx


def contem(lista, grupos):
  for grupo in grupos:
     if sorted(lista) == sorted(grupo):
        return True
  return False


def triangles (G):
  if G is None:
    return None

  grupos = []

  for vertice in G.nodes():
    adjacentes = set(G.neighbors(vertice))

    for primeiro_adjacente in adjacentes:
      for segundo_adjacente in adjacentes:
        if G.has_edge(primeiro_adjacente, segundo_adjacente) and primeiro_adjacente != segundo_adjacente:
          grupo = [vertice, primeiro_adjacente, segundo_adjacente]
          
          if not contem(grupo, grupos):
            grupos.append(grupo)    
  return grupos