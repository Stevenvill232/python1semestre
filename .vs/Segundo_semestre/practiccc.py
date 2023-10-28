def es_primo(valor):
    valor_entero = int(valor)
    contador = 1
    divisores = 0
    while contador <= valor_entero:
        if valor_entero % contador == 0:
            divisores += 1
        contador += 1
    if divisores == 2:
        return True
    else:
        return False


def fibonaccis(valor):
    a = 0
    b = 1
    temp = 0
    while temp < valor:
        temp = a + b
        a = b
        b = temp
    if valor == temp:
        return True
    else:
        return False

def leer_lista():
    lista = []
    cantidad_datos = int(input("Cantidad de datos en la lista: "))
    for i in range(cantidad_datos):
        lista.append(int(input(f'Dato({i})= ')))
    print("Lista generada según los anteriores datos: ", lista)
    return lista

def leer_matriz():
    matriz = []
    filas = int(input("Cantidad de filas: "))
    columnas = int(input("Cantidad de columnas: "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)
    print("Matriz generada según los anteriores datos: ")
    for fila in matriz:
        print(fila)
    return matriz

def punto_3():
    diccionario_datos = {3: [4, 4, 19], 4: [13, 4, 4], 9: [4, 5, 11], 13: [2, 4, 4, 8]}
    # Encontrar claves que son primos y claves que son Fibonacci
    claves_primos = []
    claves_fibonacci = []
    for clave in diccionario_datos:
        if es_primo(clave):
            claves_primos.append(clave)
        if fibonaccis(clave):
            claves_fibonacci.append(clave)
    # Crear Conjunto 1 con los números pares de las listas valor de claves primos
    conjunto_pares_primos = set()
    for clave in claves_primos:
        valores = diccionario_datos[clave]
        for valor in valores:
            if valor % 2 == 0:
                conjunto_pares_primos.add(valor)
    # Crear Conjunto 2 con los números pares de las listas valor de claves Fibonacci
    conjunto_pares_fibonacci = set()
    for clave in claves_fibonacci:
        valores = diccionario_datos[clave]
        for valor in valores:
            if valor % 2 == 0:
                conjunto_pares_fibonacci.add(valor)
    # Crear Cadena 1 con los pares comunes
    cadena_pares_comunes = ", ".join(str(valor) for valor in conjunto_pares_primos.intersection(conjunto_pares_fibonacci)) #utilizamos str para convertir un valor a una cadena 
    # Crear Cadena 2 con la unión de los pares sin elementos comunes
    cadena_union_pares = ", ".join(str(valor) for valor in conjunto_pares_primos.union(conjunto_pares_fibonacci))
    print("Conjunto 1 (Pares de claves primos):", conjunto_pares_primos)
    print("Conjunto 2 (Pares de claves Fibonacci):", conjunto_pares_fibonacci)
    print("Cadena 1 (Pares comunes):", cadena_pares_comunes)
    print("Cadena 2 (Unión de pares sin elementos comunes):", cadena_union_pares)

punto_3()
