import networkx as nx
import matplotlib.pyplot as plt
from utils.networkx_util import draw_graph


def max_income(G):

    # Parâmetro None retorna None
    if G is None:
        return None
    
    # Grafo não ponderado retorna None
    if not is_ponderado(G):
        return None
    
    # Amount inválido retorna None
    if amount_invalid(G):
        return None

    # Grafo nulo = amount zero
    if G.number_of_nodes() == 0 and G.number_of_edges() == 0:
        return 0, []

    # Lista para armazenar os amounts de cada vértice
    amounts = []
    # Lista de todos os vértices
    vertices = list(G.nodes())

    # Iterando em cada vértice para determinar os arcos de entrada e seus amounts
    for vertice in G.nodes():
        amount = 0
        # Lista com todos os arcos de entrada do vértice
        arcos = G.in_edges(vertice, data=True)

        # Iterando sobre cada arco dos arcos de entrada do vértice
        for arco in arcos:
            # Somando os amounts de todos os arcos do vértice
            amount += float(arco[2]['amount'])
        # Adicionando o amount total do vértice na lista de amounts
        amounts.append(amount)

    # Pegando o maior amount do grafo
    max_amount = max(amounts)
    # Lista que armazena as pessoas que tiveram o maior amount
    pessoas = []

    # Iterando sobre os amounts
    for i in range(len(amounts)):
        if amounts[i] == max_amount:
            # Adicionando as pessoas que têm o maior amount
            pessoas.append(vertices[i])

    return max_amount, pessoas


# Função auxiliar para verificar se um grafo é ponderado.
def is_ponderado(G):
    if G.number_of_edges() == 0:
        return True
    arcos = G.edges(data=True)
    for cauda, cabeca, amount in arcos:
        if len(amount) > 0:
            return True
    return False


# Função auxiliar para verificar se um grafo possui amount inválido (amount negativo)
def amount_invalid(G):
    arcos = G.edges(data=True)
    for cauda, cabeca, amount in arcos:
        if amount['amount'] < 0:
            return True
    return False


