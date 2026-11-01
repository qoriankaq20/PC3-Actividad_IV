
# -----------------------------------------
# 1a. Implementacion del algoritmo voraz: CAMBIO DE MONEDA
# -----------------------------------------


def cambio_moneda(monto, monedas):
    # se ordena las monedas de mayor a menor (criterio voraz)
    monedas = sorted(monedas, reverse=True)
    resultado = {}

    for moneda in monedas:
        # Cuantas veces cabe esta moneda en el monto que falta
        cantidad = monto // moneda
        if cantidad > 0:
            resultado[moneda] = cantidad
            # se resta lo que ya se ha cubierto
            monto = monto - cantidad * moneda

    return resultado

# Programa principal
print("-" * 40)
print("1a. Cambio de moneda")
print("-" * 40)

monto = 68
monedas = [25, 10, 5, 1]

cambio = cambio_moneda(monto, monedas)

print("Monto:", monto)
for moneda, cantidad in cambio.items():
    print(f"{cantidad} moneda(s) de {moneda}")
print("Total de monedas usadas:", sum(cambio.values()))


# -----------------------------------------
# 1b. Implementacion del algoritmo voraz: DIJKSTRA
# -----------------------------------------


import heapq

def dijkstra(grafo, inicio):
    # Al inicio todas las distancias son infinito, menos la del nodo de partida
    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0
    # Guarda desde que nodo se llego a cada uno (para reconstruir el camino)
    previo = {nodo: None for nodo in grafo}
    # Cola de prioridad: siempre sale el nodo con menor distancia
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo = heapq.heappop(cola)
        # Si ya hay una distancia mejor registrada, se ignora esta entrada
        if distancia_actual > distancias[nodo]:
            continue
        # se revisan los vecinos del nodo actual
        for vecino, peso in grafo[nodo].items():
            nueva = distancia_actual + peso
            # Si pasar por este nodo da un camino mas corto, se actualiza
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                previo[vecino] = nodo
                heapq.heappush(cola, (nueva, vecino))

    return distancias, previo

def reconstruir_camino(previo, destino):
    camino = []
    while destino is not None:
        camino.append(destino)
        destino = previo[destino]
    # Se invierte para que vaya de inicio a destino
    return camino[::-1]

# Programa principal
print()
print("-" * 40)
print("1b. Dijkstra")
print("-" * 40)

grafo = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "C": 1, "D": 5},
    "C": {"A": 2, "B": 1, "D": 8, "E": 10},
    "D": {"B": 5, "C": 8, "E": 2},
    "E": {"C": 10, "D": 2},
}

distancias, previo = dijkstra(grafo, "A")

print("Distancias minimas desde A:")
for nodo in grafo:
    camino = " -> ".join(reconstruir_camino(previo, nodo))
    print(f"A a {nodo}: distancia {distancias[nodo]}, camino: {camino}")