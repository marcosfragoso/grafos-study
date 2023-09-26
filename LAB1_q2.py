# Considere um grafo onde os vértices são nomes de pessoas e as arestas relacionam 
# nomes de pessoas que são amigas.
# Implemente a função **candidates** que retorna uma lista com os nomes 
# de *candidatos a amigos* que uma certa *pessoa* pode conhecer, 
# em ordem alfabética. Os candidatos a amigos são amigos diretos de amigos 
# de *pessoa* que ainda não são amigos de *pessoa*. O nome da pessoa está 
# definido na variável **p**.
# Exemplo:
# Para o grafo:
#    ['Joao', 'Maria', 'Eduardo', 'Cristina', 'Otavio', 'Jose']
#    [('Joao', 'Maria'), ('Joao', 'Otavio'), ('Maria', 'Cristina'), 
#     ('Maria', 'Eduardo'), ('Eduardo', 'Cristina'), ('Cristina', 'Otavio'), 
#      ('Cristina', 'Jose'), ('Otavio', 'Jose')]
# Se pessoa = "Maria", a função deve retornar: ['Jose','Otávio']


def candidates (G,p):
  
  if G is None or p is None:
    return None

  candidatos = []

  for vertice in G.nodes:
    if not G.has_edge(p, vertice) and vertice != p:
      candidatos.append(vertice)
  
  candidatos_order = sorted(candidatos, key=str.lower)
  return candidatos_order