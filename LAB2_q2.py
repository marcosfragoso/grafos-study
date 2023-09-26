# Implemente a função **walk_type** que recebe um grafo simples **G** e uma lista de vértices **W** 
# e determina o tipo de passeio que a lista representa:
#
#  * não é passeio
#  * passeio aberto
#  * passeio fechado
#  * caminho
#  * ciclo
#  * ciclo simples

# onde *passeio aberto* é todo passeio cuja origem e destino são diferentes e *passeio fechado* é 
# todo passeio cuja origem e destino são iguais.
# Note que todo ciclo é um passeio fechado, mas a função deve retornar a classificação mais 
# específica. As classificações passeio aberto e passeio fechado só devem ser dadas para passeios 
# que não podem ser classificados como caminho, ciclo ou ciclo simples.
#
# Como exemplo, considere o grafo "s-u-cy-sc-p-b-01.graphml" (ver main_Q02.py). 
# A função deve classificar as seguintes sequências de vértices como:
#
#    ['n0','n2','n3','n2','n0']: passeio fechado
#    ['n0', 'n2', 'n3', 'n1', 'n0']: ciclo simples
#    ['n0', 'n2', 'n3', 'n2', 'n3', 'n1', 'n0', 'n2']: passeio aberto
#    ['n0', 'n2', 'n3', 'n1']: caminho
#    ['n3', 'n2', 'n0', 'n1', 'n3', 'n5', 'n6', 'n4', 'n3']: ciclo
#    ['n0', 'n2', 'n3', 'n6', 'n3', 'n1', 'n0', 'n2']: não é passeio
#
# *Dica:*
#* Use a função *repeated_edges* abaixo para determinar se um passeio possui arestas repetidas
# * Consulte o notebook da Aula 03, tópico Passeio e Caminho.
 
import networkx as nx

def repeated_edges(G, W):
  count_edges = {(u,v):0 for (u,v) in G.edges}
  for i in range(len(W)-1):
    u,v = W[i],W[i+1]
    if (u,v) in count_edges.keys():
      count_edges[(u,v)] += 1
    elif (v,u) in count_edges.keys():
      count_edges[(v,u)] += 1
  return any(count_edges[(u,v)] > 1 for (u,v) in count_edges)

# passeio = cada aresta inicia com um vertice, na qual a aresta anterior terminou
# passeio aberto = origem e desino diferentes
# passeio fechado = origem e destino iguais
# ciclo simples = ciclo onde todos os vértices são distintos
# ciclo = passeio sem repetir arestas
# não é passeio
# caminho = todos os vértices distintos


def walk_type (G, W):

  if G is None or W is None:
    return None
  
  for vertice in W:
    if vertice not in G.nodes():
      return None


  if eh_passeio(G, W) and eh_fechado(G, W) and ciclo_simples(W) and not repeated_edges(G, W):
    return "ciclo simples"
  elif eh_passeio(G, W) and eh_fechado(G, W) and not repeated_edges(G, W) and not ciclo_simples(W):
    return "ciclo"
  elif eh_passeio(G, W) and eh_caminho(W) and not eh_fechado(G, W):
    return "caminho"
  elif eh_passeio(G, W) and eh_fechado(G, W):
    return "passeio fechado"
  elif eh_passeio(G, W):
    return "passeio aberto"
  else:
    return "não é passeio"


def eh_passeio(G, W):
  for i in range(len(W) - 1):
    if not G.has_edge(W[i], W[i + 1]):
      return False
  return True


def eh_fechado(G, W):
  if eh_passeio(G, W):
    if W[0] == W[-1] and len(W) > 1:
      return True
  return False


def eh_caminho(W):
  return len(W) == len(set(W))


def ciclo_simples(W):
    if len(W) <= 2 or W[0] != W[-1]:
        return False

    lista_sem_extremos = []
    for k in range(1, len(W) - 1):
      lista_sem_extremos.append(W[k])

    lista_sem_repeticao = set(lista_sem_extremos)
    
    if len(lista_sem_repeticao) != len(lista_sem_extremos):
        return False
    return True