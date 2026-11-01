
# -----------------------------------------
# 4. Implementacion del algoritmo backtracking: STRINGS DE LARGO 3 CON "a", "b" Y "c"
# -----------------------------------------

def generar_strings(letras, largo, actual, resultado):
    # Caso base: el string ya tiene el largo pedido, por lo q se guarda
    if len(actual) == largo:
        resultado.append(actual)
        return

    for letra in letras:
        # se elegi una letra y avanza a la siguiente posicion
        generar_strings(letras, largo, actual + letra, resultado)
        # Al volver de la llamada, se prueba la siguiente letra (backtracking)

print("-" * 40)
print("4. Strings de largo 3 con a, b y c")
print("-" * 40)

letras = ["a", "b", "c"]
resultado = []
generar_strings(letras, 3, "", resultado)

for s in resultado:
    print(s)
print("Total de strings:", len(resultado))

