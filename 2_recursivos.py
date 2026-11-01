
# -----------------------------------------
# 2a. Implementacion del algoritmo recursivo: SUMA DE LOS DIGITOS DE UN NUMERO
# -----------------------------------------


def suma_digitos(n):
    # Caso base: si tiene un solo digito, la suma es el mismo numero
    if n < 10:
        return n
    # Caso recursivo: ultimo digito + suma de los digitos restantes
    return n % 10 + suma_digitos(n // 10)

print("-" * 40)
print("2a. Suma de los digitos de un numero")
print("-" * 40)
numero = 1234
print("Entrada:", numero)
print("Salida:", suma_digitos(numero))

# -----------------------------------------
# 2b. Implementacion del algoritmo recursivo: CONTAR OCURRENCIAS DE UN ELEMENTO EN UNA LISTA
# -----------------------------------------

print()
print("-" * 40)
print("2b. Contar ocurrencias de un elemento en una lista")
print("-" * 40)

def contar_ocurrencias(lista, x):
    # Caso base: lista vacia, no hay nada que contar
    if len(lista) == 0:
        return 0
    # Si el primer elemento coincide, suma 1 y sigue con el resto de la lista
    if lista[0] == x:
        return 1 + contar_ocurrencias(lista[1:], x)
    # Si no coincide, solo sigue con el resto
    return contar_ocurrencias(lista[1:], x)


lista = [1, 2, 3, 2, 2, 4]
x = 2
print("Entrada: lista =", lista, ", x =", x)
print("Salida:", contar_ocurrencias(lista, x))