from busca_largura import bfs

def connected_components_bfs(g):

  if g is None:
    return None

  vertices = list(g.nodes()) # Lista de todos os vértices de G
  componentes = [] # Lista que armazena todos os componentes de G

  while vertices:
    arvore = bfs(g, vertices[0]) # Árvore resultante sendo a raíz o primeiro vértice da lista de vértices
    vertices_arvore = [] # Lista que armazena os vértices da árvore resultante que formarão um componente
    for key in arvore[2]:
      vertices_arvore.append(key)
    componentes.append(vertices_arvore)

    for node in vertices_arvore:
      vertices.remove(node) # Removendo os vértices que já estão em um componente

  return componentes