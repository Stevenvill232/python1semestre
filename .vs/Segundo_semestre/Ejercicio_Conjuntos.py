# Función para leer un vector
def leer_vector():
    vector = []
    cantidad_datos = int(input("Cantidad de datos en el vector: "))
    for i in range(cantidad_datos):
        vector.append(int(input(f'Dato({i})= ')))
    return vector

# Función para leer una matriz
def leer_matriz():
    matriz = []
    filas = int(input("Cantidad de filas de la matriz: "))
    columnas = int(input("Cantidad de columnas de la matriz: "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)
    return matriz

# Función para verificar si un número es primo
def es_primo(valor):
    if valor <= 1:
        return False
    if valor <= 3:
        return True
    if valor % 2 == 0 or valor % 3 == 0:
        return False
    i = 5
    while i * i <= valor:
        if valor % i == 0 or valor % (i + 2) == 0:
            return False
        i += 6
    return True

# Función para obtener los números primos de una lista (vector o matriz)
def obtener_primos(lista):
    primos = set()  # Usamos un conjunto para evitar duplicados
    for elemento in lista:
        if es_primo(elemento):
            primos.add(elemento)
    return primos

# Función para realizar las operaciones de conjuntos
def operaciones_conjuntos(vector_primos, matriz_primos):
    # Unión de conjuntos
    union = vector_primos.union(matriz_primos)

    # Intersección de conjuntos
    interseccion = vector_primos.intersection(matriz_primos)

    # Diferencia entre el vector y la matriz
    diferencia_vector = vector_primos.difference(matriz_primos)

    # Diferencia entre la matriz y el vector
    diferencia_matriz = matriz_primos.difference(vector_primos)

    # Diferencia simétrica entre el vector y la matriz
    dif_simetrica = vector_primos.symmetric_difference(matriz_primos)

    return union, interseccion, diferencia_vector, diferencia_matriz, dif_simetrica

# Función para imprimir un conjunto
def imprimir_conjunto(nombre, conjunto):
    print(f"{nombre}: {conjunto}")

# Main
def main():
    vector = leer_vector()
    matriz = leer_matriz()
    primos_vector = obtener_primos(vector)
    primos_matriz = obtener_primos([numero for fila in matriz for numero in fila])
    
    union, interseccion, diferencia_vector, diferencia_matriz, dif_simetrica = operaciones_conjuntos(primos_vector, primos_matriz)
    
    imprimir_conjunto("Números primos en el vector", primos_vector)
    imprimir_conjunto("Números primos en la matriz", primos_matriz)
    imprimir_conjunto("Unión", union)
    imprimir_conjunto("Intersección", interseccion)
    imprimir_conjunto("Diferencia Vector-Matriz", diferencia_vector)
    imprimir_conjunto("Diferencia Matriz-Vector", diferencia_matriz)
    imprimir_conjunto("Diferencia Simétrica", dif_simetrica)

main()
