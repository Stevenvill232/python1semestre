####Punto 13 
def leer_matriz():
    matriz=[]
    cantidad=int(input("Numero de filas * columnas: "))
    for i in range(cantidad):
        fila=[]
        for j in range(cantidad):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)
    print("Matriz original:")    
    for fila in matriz:
        print(fila)
    return matriz

def promedio_diagonal_principal_secundaria(valor_1):
    suma=0
    contador=0
    print("Datos de la diagonal principal: ")
    for i in range(len(valor_1)):
        for j in range(len(valor_1[i])):
            if i == j:
                print(valor_1[i][j])
                suma+=valor_1[i][j]
                contador+=1

    promedio_1=suma/contador
    print("Promedio de la diagonal principal: ",promedio_1)

    suma=0
    contador=0
    print("Datos de la diagonal secundaria: ")
    for i in range(len(valor_1)):
        for j in range(len(valor_1[i])):
            if i+j==len(valor_1)-1:
                print(valor_1[i][j])
                suma+=valor_1[i][j]
                contador+=1

    promedio_2=suma/contador
    print("Promedio de la diagonal secundaria: ",promedio_2)           

def orden_diagonal_principal(valor_2):
    for i in range(len(valor_2)-1):
        for j in range(i+1,len(valor_2)):
            if valor_2[j][j]<valor_2[i][i]:
                aux=valor_2[i][i]
                valor_2[i][i]=valor_2[j][j]
                valor_2[j][j]=aux
    print("Orden de la diagonal principal: ")
    for fila in valor_2:
        print(fila)   

def promedio_encima_diagonales(matriz):
    suma_pares = 0
    contador_pares = 0
    suma_impares = 0
    contador_impares = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > i:  # Por encima de la diagonal principal
                if matriz[i][j] % 2 == 0:  # Número par
                    suma_pares += matriz[i][j]
                    contador_pares += 1
            if i + j < len(matriz) - 1:  # Por encima de la diagonal secundaria
                if matriz[i][j] % 2 != 0:  # Número impar
                    suma_impares += matriz[i][j]
                    contador_impares += 1
    
    if contador_pares > 0:
        promedio_pares = suma_pares / contador_pares
        print("Promedio de los pares encima de la diagonal principal:", promedio_pares)
    else:
        print("No hay números pares encima de la diagonal principal.")
    
    if contador_impares > 0:
        promedio_impares = suma_impares / contador_impares
        print("Promedio de los impares encima de la diagonal secundaria:", promedio_impares)
    else:
        print("No hay números impares encima de la diagonal secundaria.")

def relllenar_diagonales(matriz):
    si_primo=0
    si_fibonacci=0
    si_par=0
    si_impar=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            div=0
            c=1
            while c<=matriz[i][j]:
                if matriz[i][j]%c==0:
                    div+=1
                c+=1
            if div==2:
                si_primo+=1
                if si_primo==1:
                    primo_menor=matriz[i][j]
                elif matriz[i][j]<primo_menor:
                    primo_menor=matriz[i][j]
            a=0
            b=1
            t=0
            while t<matriz[i][j]:
                t=a+b
                a=b
                b=t
            if matriz[i][j]==t:
                si_fibonacci+=1
                if si_fibonacci==1:
                    fibonacci_mayor=matriz[i][j]
                elif matriz[i][j]>fibonacci_mayor:
                    fibonacci_mayor=matriz[i][j]

            if matriz[i][j] % 2==0:
                si_par+=1
                if si_par==1:
                    par_mayor=matriz[i][j]
                elif matriz[i][j]>par_mayor:
                    par_mayor=matriz[i][j]
            else:
                si_impar+=1
                if si_impar==1:
                    impar_menor=matriz[i][j]
                elif matriz[i][j]<impar_menor:
                    impar_menor=matriz[i][j]

    print("Primo menor de la matriz: ",primo_menor," Fibonacci mayor de la matriz: ",fibonacci_mayor)
    print("Diagonales reemplazadas por los anteriores datos: ")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i==j:
                matriz[i][j]=primo_menor
            elif i+j==len(matriz)-1:
                matriz[i][j]=fibonacci_mayor
    for fila in matriz:
        print(fila)
    return par_mayor,impar_menor                

def llenar_contorno_interior(matriz, par_mayor, impar_menor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0 or i == len(matriz) - 1 or j == 0 or j == len(matriz[i]) - 1:
                matriz[i][j] = par_mayor
            else:
                matriz[i][j] = impar_menor

    print("Matriz con contorno de par_mayor y parte interna de impar_menor:")
    for fila in matriz:
        print(fila)

matriz= leer_matriz() #obligatorio
#promedio_diagonal_principal_secundaria(matriz)
#orden_diagonal_principal(matriz)
#promedio_encima_diagonales(matriz)
#par_mayor, impar_menor = relllenar_diagonales(matriz) #obligatoria para que funcione la siguiente, se hizo asi para comprobar si servia algo(return)
#llenar_contorno_interior(matriz, par_mayor, impar_menor)


####punto 14
def leer_dos_matrices():
    matriz_1 = []
    matriz_2 = []

    filas_1 = int(input("Filas en matriz 1: "))
    columnas_1 = int(input("Columnas en matriz 1: "))
    print("Digite los datos de la matriz 1 en orden ascendente: ")
    for i in range(filas_1):
        fila_1 = []
        for j in range(columnas_1):
            fila_1.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila_1)

    print("Matriz 1: ")
    for fila in matriz_1:
        print(fila)  

    filas_2 = int(input("Filas en matriz 2: "))
    columnas_2 = int(input("Columnas en matriz 2: "))
    print("Digite los datos de la matriz 2 en orden ascendente: ")
    for i in range(filas_2):
        fila_2 = []
        for j in range(columnas_2):
            fila_2.append(int(input(f'Dato({i},{j})= ')))
        matriz_2.append(fila_2)
    
    print("Matriz 2: ")
    for fila in matriz_2:
        print(fila)

    return matriz_1, matriz_2

def vector_elementos_comunes(matriz_1, matriz_2):
    vector = []
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            dato = matriz_1[i][j] in matriz_2[i]
            if dato==True:
                print(matriz_1[i][j], "Dato en común en su respectiva fila")
                dato_2 = matriz_1[i][j] in vector
                if not dato_2:
                    vector.append(matriz_1[i][j])

    print("Vector resultante con los datos comunes sin repetir: ", vector)
    return vector

def vector_primos_comunes(matriz_1,matriz_2):
    vector_2=[]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            c=1
            div=0
            while c<=matriz_1[i][j]:
                if matriz_1[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                dato= matriz_1[i][j] in matriz_2[i]
                if dato==False:
                    print(matriz_1[i][j],"Es primo no comun en su respectiva fila")
                    dato_2= matriz_1[i][j] in vector_2
                    if dato_2==False:
                        vector_2.append(matriz_1[i][j]) 

    for i in range(len(matriz_2)):
        for j in range(len(matriz_2[i])):
            c=1
            div=0
            while c<=matriz_2[i][j]:
                if matriz_2[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                dato= matriz_2[i][j] in matriz_1[i]
                if dato==False:
                    print(matriz_2[i][j],"Es primo no comun en su respectiva fila")
                    dato_2= matriz_2[i][j] in vector_2
                    if dato_2==False:
                        vector_2.append(matriz_2[i][j])

    print("Vector resultante con los primos NO comunes sin repetir: ",vector_2)
    return vector_2                                                  

#matriz_1, matriz_2 = leer_dos_matrices()
#vector_datos_comunes = vector_elementos_comunes(matriz_1, matriz_2)
#vector_datos_primos_comunes = vector_primos_comunes(matriz_1,matriz_2) 


####Punto 16
def intercambio_columnas(matriz):
    for i in range(len(matriz)):
        aux=matriz[i][0]
        matriz[i][0]=matriz[i][-1]
        matriz[i][-1]=aux

    print("Matriz con la primera columna intercambiada por la ultima: ")
    for fila in matriz:
        print(fila)

    return matriz

def mayor_menor_promedio_columnas(matriz):
    for j in range(len(matriz[0])):
        mayor = matriz[0][j]
        menor = matriz[0][j]
        suma = 0
        for i in range(len(matriz)):
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
            elif matriz[i][j] < menor:
                menor = matriz[i][j]

            suma += matriz[i][j]
        promedio = suma / len(matriz)
        print("Columna", j, "Mayor:", mayor, "Menor:", menor, "Promedio:", promedio)

def ordenar_filas_pares_impares(matriz):
    for i in range(len(matriz)):
        if i % 2 == 0:  # Fila par
            for j in range(len(matriz[i]) - 1):
                for k in range(j + 1, len(matriz[i])):
                    if matriz[i][k] < matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[i][k]
                        matriz[i][k] = aux
        else:  # Fila impar
            for j in range(len(matriz[i]) - 1):
                for k in range(j + 1, len(matriz[i])):
                    if matriz[i][k] > matriz[i][j]:
                        aux = matriz[i][j]
                        matriz[i][j] = matriz[i][k]
                        matriz[i][k] = aux
    print("Matriz ordenada en columnas pares ascendentes y columnas impares descendentes:")
    for fila in matriz:
        print(fila)

def orden_matriz_descendente(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            p=i
            q=j
            while p<len(matriz):
                while q<len(matriz[i]):
                    if matriz[p][q]>matriz[i][j]:   
                        aux=matriz[i][j]
                        matriz[i][j]=matriz[p][q]
                        matriz[p][q]=aux
                    q+=1
                p+=1
                q=0 #Para garantizar que la siguiente fila inicie en 0
    print("Matriz ordenada descendentemente: ")
    for fila in matriz:
        print(fila)
    return matriz    

def intercambiar_filas_promedio_ascendente(matriz):
    promedios = []
    
    for i in range(len(matriz)):
        suma = sum(matriz[i])
        promedio = suma / len(matriz[i])
        promedios.append((promedio, i))
    
    promedios.sort()  # Ordenar por promedio en orden ascendente
    
    nueva_matriz = []
    for promedio, fila_index in promedios:
        nueva_matriz.append(matriz[fila_index])
    
    print("Matriz ordenada de acuero al promedio de cada fila: ")
    for fila in nueva_matriz:
        print(fila)

# matriz_intercambio_columnas = intercambio_columnas(matriz)
#mayor_menor_promedio_columnas(matriz)
#ordenar_filas_pares_impares(matriz)
#matriz_ordenada_descendentemente = orden_matriz_descendente(matriz)
#intercambiar_filas_promedio_ascendente(matriz)       