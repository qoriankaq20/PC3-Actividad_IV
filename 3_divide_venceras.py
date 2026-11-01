# -----------------------------------------
# 3. Implementacion del algoritmo divide y venceras: MAXIMO Y MINIMO EN UNA LISTA
# -----------------------------------------

# Enfoque iterativo: recorre toda la lista comparando cada elemento

def max_min_iterativo(lista):
    maximo = minimo = lista[0]
    comparaciones = 0
    for x in lista[1:]:
        # Cada elemento se compara dos veces: contra el maximo y contra el minimo
        comparaciones += 2
        if x > maximo:
            maximo = x
        if x < minimo:
            minimo = x
    return maximo, minimo, comparaciones

# Enfoque divide y venceras: divide la lista en mitades y combina los resultados

def max_min_dyv(lista):
    # Caso base: un solo elemento es maximo y minimo a la vez
    if len(lista) == 1:
        return lista[0], lista[0], 0
    # Caso base: dos elementos, una sola comparacion
    if len(lista) == 2:
        if lista[0] > lista[1]:
            return lista[0], lista[1], 1
        return lista[1], lista[0], 1

    # Dividir: se separa la lista en dos mitades y se resuelve cada una
    medio = len(lista) // 2
    max_izq, min_izq, comp_izq = max_min_dyv(lista[:medio])
    max_der, min_der, comp_der = max_min_dyv(lista[medio:])

    # Combinar: se comparan los resultados de ambas mitades (2 comparaciones)
    maximo = max_izq if max_izq > max_der else max_der
    minimo = min_izq if min_izq < min_der else min_der
    return maximo, minimo, comp_izq + comp_der + 2

lista = [3, 5, 1, 2, 8, 9, 4]

print("-" * 40)
print("3. Maximo y minimo en una lista")
print("-" * 40)

print("Entrada:", lista)

maximo, minimo, comp = max_min_iterativo(lista)
print("\nEnfoque iterativo")
print(f"Maximo: {maximo}, Minimo: {minimo}")
print("Comparaciones:", comp)

maximo, minimo, comp = max_min_dyv(lista)
print("\nEnfoque divide y venceras")
print(f"Maximo: {maximo}, Minimo: {minimo}")
print("Comparaciones:", comp)
