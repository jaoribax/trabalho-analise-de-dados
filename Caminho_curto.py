# Defina o grafo do mundo encantado com 20 fases
grafo = {
    "Torre": [("Fase 1", 10), ("Fase 2", 5)],
    "Fase 1": [("Fase 3", 3), ("Fase 4", 7)],
    "Fase 2": [("Fase 3", 2)],
    "Fase 3": [("Fase 5", 4)],
    "Fase 4": [("Fase 6", 6)],
    "Fase 5": [("Fase 7", 8)],
    "Fase 6": [("Fase 7", 3)],
    "Fase 7": [("Fase 8", 5)],
    "Fase 8": [("Fase 9", 4)],
    "Fase 9": [("Fase 10", 7)],
    "Fase 10": [("Fase 11", 6)],
    "Fase 11": [("Fase 12", 4)],
    "Fase 12": [("Fase 13", 9)],
    "Fase 13": [("Fase 14", 5)],
    "Fase 14": [("Fase 15", 8)],
    "Fase 15": [("Fase 16", 7)],
    "Fase 16": [("Fase 17", 3)],
    "Fase 17": [("Fase 18", 2)],
    "Fase 18": [("Fase 19", 4)],
    "Fase 19": [("Fase 20", 10)],
    "Fase 20": []
}

def calcular_menor_caminho(grafo, ponto_inicial, ponto_destino):
    fila_de_prioridade = [(0, ponto_inicial)]  # Inicializa a fila de prioridade com o ponto de partida
    visitados = set()  # Conjunto de nós visitados
    distancia = {ponto: float('inf') for ponto in grafo}  # Inicializa a distância com infinito para todos os pontos
    distancia[ponto_inicial] = 0  # A distância até o ponto de partida é 0
    predecessor = {}  # Dicionário para armazenar os predecessores de cada ponto

    while fila_de_prioridade:
        (dist, ponto_atual) = heapq.heappop(fila_de_prioridade)

        if ponto_atual in visitados:
            continue

        visitados.add(ponto_atual)

        for (vizinho, custo) in grafo[ponto_atual]:
            if distancia[ponto_atual] + custo < distancia[vizinho]:
                distancia[vizinho] = distancia[ponto_atual] + custo
                predecessor[vizinho] = ponto_atual
                heapq.heappush(fila_de_prioridade, (distancia[vizinho], vizinho))

    caminho = []
    ponto = ponto_destino
    while ponto:
        caminho.insert(0, ponto)
        ponto = predecessor.get(ponto, None)

    return caminho, distancia[ponto_destino]

# Exemplo de uso:
ponto_partida = "Torre"
ponto_destino = "Fase 20"
caminho, distancia = calcular_menor_caminho(grafo, ponto_partida, ponto_destino)

print(f"Menor caminho de {ponto_partida} até {ponto_destino}:")
print(" -> ".join(caminho))
print(f"Distância total: {distancia}")