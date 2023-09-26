import networkx as nx
from utils.networkx_util import draw_graph
from collections import deque


filename1 = "s-u-cy-sc-p-06.graphml"

def bfs(g, r):
    i = 0
    Q = deque()
    i += 1
    painted = [r]
    l = {r: 0} # Vértice inicial com nível 0
    t = {r: i} # Vértice inicial com tempo i = 1
    Q.append(r)  # Fila: adiciona a direita
    p = [] # Registro de ordem de visita

    while Q: # Loop enquanto a fila não estiver vazia
        x = Q[0]  # Fila: elemento da frente
        not_painted = [v for v in g.neighbors(x) if v not in painted]
        
        if not_painted: # Verificando se existe vizinhos não visitados
            v = not_painted[0] # Pegando o primeiro vértice não visitado
            i += 1 # Incrementando o tempo da visita
            painted.append(v) # Visitando o vértice não visitado
            l[v] = l[x] + 1 # Definindo o nível do vértice v
            t[v] = i # Definindo o tempo de visita do vértice v
            Q.append(v) # Adicionando v à fila
            p.append(v) # Adicionando v no registro de ordens de visita
        else:
            Q.popleft()  # Removendo o vértice da fila quando não tem mais vizinhos a ser visitado.

    return p, l, t

G1 = nx.read_graphml(filename1)
r = 'n0'
#p1,l1,t1 = bfs(G1,r)
#print(f"Função predecessor: {p1}")
#print(f"Função nível: {l1}")
#print(f"Função tempo: {t1}")
#not_edges_p1 = [e for e in G1.edges if (e[0],e[1]) not in p1 and (e[1],e[0]) not in p1]

'''draw_graph(G1,title=f"Árvore BFS com raiz {r}",
           eset=[p1,not_edges_p1],
           esetcolor=["red","lightgray"],
           esetlabel=["Arestas da árvore","Arestas da co-árvore"])
           '''

#print(G1.nodes())
#bfs(G1, r)