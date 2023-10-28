def es_primo(valor):
    valor=int(valor)
    c=1
    div=0
    while c<=valor:
        if valor % c == 0:
            div+=1
        c+=1
    if div==2:
        return True
    else:
        return False

def fibonaccis(valor):
    a=0
    b=1
    t=0
    while t<valor:
        t=a+b
        a=b
        b=t

    if valor==t:
        return True
    else:
        return False 

def leer_lista():
    lista=[]
    cantidad_datos=int(input("Cantidad de datos en el la lista: "))
    for i in range(cantidad_datos):
        lista.append(int(input(f'Dato({i})=')))
    print("lista generada segun los anteriores datos: ",lista)
    return lista           

def leer_matriz():
    matriz=[]
    filas=int(input("Cantidad de filas: "))
    columnas=int(input("Cantidad de columnas: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)

    print("Matriz generada segun los anteriores datos: ")
    for fila in matriz:
        print(fila)
    return matriz    

def punto_1():
    vector=leer_lista()
    matriz=leer_matriz()
    # Encontrar el número menor y el número mayor en la matriz
    numero_menor = min(min(fila) for fila in matriz)
    numero_mayor = max(max(fila) for fila in matriz)

    # Encontrar los números primos en el rango de la matriz
    primos_en_rango = [num for num in range(numero_menor, numero_mayor + 1) if es_primo(num)]

    # Encontrar el segundo Fibonacci en el vector que está en el rango de primos
    segundo_fibonacci = None
    posicion = -1
    for i, valor in enumerate(vector):
        if valor in primos_en_rango and fibonaccis(valor):
            if segundo_fibonacci is None:
                segundo_fibonacci = valor
                posicion = i

    print("Dato encontrado: ",segundo_fibonacci," Su posicion: ",posicion)            

def punto_2():
    diccionario={3:[4,4,19],4:[13,4,4],9:[4,5,11],13:[2,4,4,8]}
    print("Diccionario generado: ",diccionario)
    lista_valores=list(diccionario.values())
    lista_claves=list(diccionario.keys())
    si_hay_primo=0
    si_hay_fibonacci=0
    primo_mayor=0
    fibonacci_menor=0
    for i in range(len(lista_valores)):
        for j in range(len(lista_valores[i])):
            if es_primo(lista_valores[i][j]):
                si_hay_primo+=1
                if si_hay_primo==1:
                    primo_mayor=lista_valores[i][j]
                else:
                    if lista_valores[i][j]>primo_mayor:
                        primo_mayor=lista_valores[i][j]
            elif fibonaccis(lista_valores[i][j]):
                si_hay_fibonacci+=1
                if si_hay_fibonacci==1:
                    fibonacci_menor=lista_valores[i][j]
                else:
                    if lista_valores[i][j]<fibonacci_menor:
                        fibonacci_menor=lista_valores[i][j]

    clave_fibonacci_menor = None
    clave_primo_mayor = None

    for clave in lista_claves:
        if diccionario[clave].count(fibonacci_menor) > 0:
            clave_fibonacci_menor = clave
        if diccionario[clave].count(primo_mayor) > 0:
            clave_primo_mayor = clave

    # Escribir los resultados
    print("El primo mayor es:", primo_mayor, "y su clave en el diccionario es:", clave_primo_mayor)
    print("El valor Fibonacci menor es:", fibonacci_menor, "y su clave en el diccionario es:", clave_fibonacci_menor) 
    pares_entre = []
    suma_pares = 0
    contador_pares = 0

    if clave_fibonacci_menor is not None and clave_primo_mayor is not None: #nos aseguramos que hallan las respectivas claves
        valores_fibonacci = diccionario[clave_fibonacci_menor] #extraemos respectivos valores
        valores_primo = diccionario[clave_primo_mayor]
        for valor in valores_fibonacci + valores_primo: #buscamos entre los 2
            if valor % 2 == 0:
                pares_entre.append(valor)
                suma_pares += valor
                contador_pares += 1

    promedio_pares = suma_pares/contador_pares
    print("Pares comprendidos entre el Fibonacci menor y el primo mayor:", pares_entre)
    print("Promedio de los pares:", promedio_pares)

def punto_3():
    diccionario = {3: [4, 4, 19], 4: [13, 4, 4], 9: [4, 5, 11], 13: [2, 4, 4, 8]}
    print("Diccionario generado: ",diccionario)
    # Encontrar claves que son primos y claves que son Fibonacci
    claves_primos = []
    claves_fibonacci = []
    for clave in diccionario:
        if es_primo(clave):
            claves_primos.append(clave)
        if fibonaccis(clave):
            claves_fibonacci.append(clave)
    # Crear Conjunto 1 con los números pares de las listas valor de claves primos
    conjunto_1 = set()
    for clave in claves_primos:
        valores = diccionario[clave]
        for valor in valores:
            if valor % 2 == 0:
                conjunto_1.add(valor)
    # Crear Conjunto 2 con los números pares de las listas valor de claves Fibonacci
    conjunto_2 = set()
    for clave in claves_fibonacci:
        valores = diccionario[clave]
        for valor in valores:
            if valor % 2 == 0:
                conjunto_2.add(valor)
    # Crear Cadena con los pares comunes entre Conjunto 1 y Conjunto 2
    cadena_pares_comunes = ", ".join(str(valor) for valor in conjunto_1.intersection(conjunto_2))

    # Crear Cadena con la unión de los pares de Conjunto 1 y Conjunto 2 (sin elementos comunes)
    cadena_union_pares = ", ".join(str(valor) for valor in conjunto_1.union(conjunto_2))
    print("Conjunto 1 (Pares de claves primos):", conjunto_1)
    print("Conjunto 2 (Pares de claves Fibonacci):", conjunto_2)
    print("Cadena 1 (Pares comunes):", cadena_pares_comunes)
    print("Cadena 2 (Unión de pares sin elementos comunes):", cadena_union_pares)


                                 

                    


        




    



            

