import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph

'''
Escreva uma função, best_path, que encontra o menor caminho em um grafo G de um vértice s para um vértice t,
passando por todos os vértices na lista stops, na ordem definida pela lista. 
O vértice s tem que ser diferente de t e estes vértices não podem estar incluídos em stops.
A função deve retornar uma lista de vértices que representa o caminho. Se o caminho não existir, a função deve retornar uma lista vazia.
'''

def best_path(G, s, stops, t):

    parametro_nulo = G is None or s is None or t is None or stops is None

    # Não pode haver parâmetros None, nem s = t, nem s e t inclusos nos stops e nem vértices que não façam parte do grafo
    if (parametro_nulo) or (s == t): return None
    if s in stops or t in stops: return None
    if not (G.has_node(s) and G.has_node(t)): return None
    if (not stops_pertencem(G, stops)): return None
        
    # Se passar stop vazio, retorna o menor caminho possível
    if len(stops) < 1: return list(nx.shortest_path(G, s, t))

    # Lista todos os caminhos possíveis do s até o t
    caminhos = list(nx.all_simple_paths(G, source=s, target=t))
    # Lista com caminhos que passa pelos stops
    caminhos_com_stops = []
    
    for caminho in caminhos:
        # Verifica se o caminho tem stop
        if encontra_stops(caminho=caminho, stops=stops):
            # Adiciona caminho com stop
            caminhos_com_stops.append(caminho)

    # Se não houver caminho, retorna lista vazia        
    if len(caminhos_com_stops) < 1: return caminhos_com_stops
    
    # Encontrando o caminho mais curto
    caminho_mais_curto = caminhos_com_stops[0]
    for caminho in caminhos_com_stops:
        if len(caminho) < len(caminho_mais_curto):
            caminho_mais_curto = caminho

    return caminho_mais_curto


# Função auxiliar para verificar se o caminho passa pelo stop
def encontra_stops(caminho, stops):
    j = 0
    for i in range(len(caminho)):
        if caminho[i] == stops[j]:
            j += 1
        if j == len(stops):
            return True 
    return False


# Função auxiliar para verificar se os vértices dos stops pertencem ao grafo
def stops_pertencem(G, stops):
    for vertice in stops:
        if not G.has_node(vertice):
            return False
    return True