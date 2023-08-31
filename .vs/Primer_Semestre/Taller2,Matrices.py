#####Punto 1 (Se tiene una matriz con datos numericos, determinar los datos que mas se repiten)
matriz = []
contador = []
datos_no_repetidos = []
filas = int(input("Número de filas: "))
columnas = int(input("Número de columnas: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f'Dato ({i},{j})= ')))
    matriz.append(fila)

# Encontrar datos no repetidos y contar repeticiones
for i in range(filas):
    for j in range(columnas):
        dato_actual = matriz[i][j]
        if dato_actual not in datos_no_repetidos:
            datos_no_repetidos.append(dato_actual)
            contador.append(1)
        else:
            contador[datos_no_repetidos.index(dato_actual)] += 1

# Ordenar los resultados según la cantidad de repeticiones
for i in range(len(contador)):
    for j in range(i + 1, len(contador)):
        if contador[j] > contador[i]:
            contador[i], contador[j] = contador[j], contador[i]
            datos_no_repetidos[i], datos_no_repetidos[j] = datos_no_repetidos[j], datos_no_repetidos[i]

# Imprimir los datos ordenados por cantidad de repeticiones
for i in range(len(contador)):
    print("Dato:", datos_no_repetidos[i], "veces:", contador[i])

print("Datos que más veces se repiten:")
print(datos_no_repetidos[0], ",", contador[0], "veces")
aux = datos_no_repetidos[0]

i = 0
j = 0
while i < filas and j < columnas:
    if matriz[i][j] == aux:
        print(datos_no_repetidos[i], ",", contador[j], "veces")
    i += 1
    j += 1

##### Punto 2 (Determinar el mayor, el menor y el promedio de cada columna)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
for j in range(columnas):
    mayor=matriz[0][j]
    menor=matriz[0][j]
    suma=0
    for i in range(filas):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
        elif matriz[i][j]<menor:
            menor=matriz[i][j]

        suma+=matriz[i][j]

    promedio=suma/columnas
    print("columna ",j)
    print("Promedio: ",promedio)
    print("Mayor: ",mayor)
    print("Menor: ",menor) 

##### Punto 3 (intercambiar las filas donde se encuentre el mayor y el menor de la matriz)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
mayor=matriz[0][0]
fila_mayor=0
columna_mayor=0
menor=matriz[0][0]
fila_menor=0
columna_menor=0
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
            fila_mayor=i
            columna_mayor=j
        elif matriz[i][j]<menor:
            menor=matriz[i][j]
            fila_menor=i
            columna_menor=j

print("Mayor de la matriz: ",mayor," Ubicado en la fila: ",fila_mayor," Columna: ",columna_mayor)
print("Menor de la matriz: ",menor," Ubicado en la fila: ",fila_menor," Columna: ",columna_menor)
for j in range(columnas):
    aux=matriz[fila_mayor][j]
    matriz[fila_mayor][j]=matriz[fila_menor][j]
    matriz[fila_menor][j]=aux
    
print("Filas intercambiadas con sus respectivos datos: ")
for i in range(filas):
    for j in range(columnas):
        print(f'Dato {i},{j}=',matriz[i][j])    

#### Punto 4 (Intercambiar las columnas donde se encuentre el primo mayor y menor de la matriz)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
mayor=matriz[0][0]
columna_mayor=0
fila_mayor=0
menor=matriz[0][0]
columna_menor=0
fila_menor=0
for i in range(filas):
    for j in range(columnas):
        c=1
        div=0
        while c <= matriz[i][j]:
            if matriz[i][j]%c==0:
                div+=1
            c+=1

        if div==2:
            if matriz[i][j]>mayor:
                mayor=matriz[i][j]
                columna_mayor=j
                fila_mayor=i
            elif matriz[i][j]<menor:
                menor=matriz[i][j]
                columna_menor=j
                fila_menor=i

print("Primo mayor de la matriz: ",mayor," Ubicado en la columna: ",columna_mayor," Fila: ",fila_mayor)
print("Primo menor de la matriz: ",menor," Ubicado en la columna: ",columna_menor," Fila: ",fila_menor)
for i in range(filas):
    aux=matriz[i][columna_mayor]
    matriz[i][columna_mayor]=matriz[i][columna_menor]
    matriz[i][columna_menor]=aux

print("Columnas intercambiadas con sus respectivos datos: ")
for i in range(filas):
    for j in range(columnas):
        print(f'Dato {i},{j}=',matriz[i][j]) 

#### Punto 5 (Se tienen 2 matrices, formar un vector con los fibonaccis comunes sin repetir)
matriz1=[]
matriz2=[]
v_resultante=[]
filas1=int(input("Numero de filas matriz 1= "))
columnas1=int(input("Numero de columnas matriz 1= "))
print("Datos en matriz 1:")
for i in range(filas1):
    fila=[]
    for j in range(columnas1):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz1.append(fila)

filas2=int(input("Numero de filas matriz 2= "))
columnas2=int(input("Numero de columnas= "))
print("Datos en matriz 2:")
for i in range(filas2):
    fila=[]
    for j in range(columnas2):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz2.append(fila)  

na=0
for i in range(filas1):
    for j in range(columnas1):
        a=0
        b=1
        t=0
        while t < matriz1[i][j]:
            t=a+b
            a=b
            b=t
            
        if matriz1[i][j]==t:
            b1=0
            p=0
            while p<filas2 and b1==0:
                q=0
                while q<columnas2 and b1==0:
                    if matriz1[i][j]==matriz2[p][q]:
                        b1=1
                    else:
                        q+=1
                p+=1

            if b1==1:
                b2=0
                x=0
                while x<na and b2==0:
                    if matriz1[i][j]==v_resultante[x]:
                        b2=1
                    else:
                        x+=1

                if b2==0:
                    print(matriz1[i][j]," Fibonacci comun")
                    v_resultante.append(matriz1[i][j])
                    na+=1

print("Vector resultante con numeros fibonaccis comunes sin repetir: ",v_resultante)

##### Punto 6 (Se tienen dos matrices, crear un vector con los numeros primos de la matriz 1 y 2 sin repetir)
matriz1=[]
matriz2=[]
v_resultante=[]
filas1=int(input("Numero de filas matriz 1= "))
columnas1=int(input("Numero de columnas matriz 1= "))
print("Datos en matriz 1:")
for i in range(filas1):
    fila=[]
    for j in range(columnas1):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz1.append(fila)

filas2=int(input("Numero de filas matriz 2= "))
columnas2=int(input("Numero de columnas= "))
print("Datos en matriz 2:")
for i in range(filas2):
    fila=[]
    for j in range(columnas2):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz2.append(fila)    

na=0
for i in range(filas1):
    for j in range(columnas1):
        c=1
        div=0
        while c <= matriz1[i][j]:
            if matriz1[i][j] % c==0:
                div+=1
            c+=1

        if div==2:
            b2=0
            x=0
            while x<na and b2==0:
                if matriz1[i][j]==v_resultante[x]:
                    b2=1
                else:
                    x+=1

            if b2==0:
                v_resultante.append(matriz1[i][j])
                na+=1

for i in range(filas2):
    for j in range(columnas2):
        c=1
        div=0
        while c <= matriz2[i][j]:
            if matriz2[i][j] % c==0:
                div+=1
            c+=1

        if div==2:
            b2=0
            x=0
            while x<na and b2==0:
                if matriz2[i][j]==v_resultante[x]:
                    b2=1
                else:
                    x+=1

            if b2==0:
                v_resultante.append(matriz2[i][j])
                na+=1        


print("Vector resultante con numeros primos de la matriz 1 y 2 sin repetir: ",v_resultante)

##### Punto 7 (Se tiene una matriz cuadrada, formar un vector con los primos de la diagonal principal y los primos de la diagonal secundaria)
dimension=int(input("Numero de filas y columnas: "))
matriz=[]
for i in range(dimension):
    fila=[]
    for j in range(dimension):
        fila.append(int((input(f'Dato({i},{j})= '))))

    matriz.append(fila)    

v_primos_dprincipal=[]
v_primos_dsecundaria=[]
for i in range(dimension):
    for j in range(dimension):
        if i==j:
            c=1
            div=0
            while c<= matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1

            if div==2:
                print("Primo de diagonal principal: ",matriz[i][j])
                v_primos_dprincipal.append(matriz[i][j])

for i in range(dimension):
    for j in range(dimension):
        if i+j==dimension-1:
            c=1
            div=0
            while c<= matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1

            if div==2:
                print("Primo de diagonal secundaria: ",matriz[i][j])
                v_primos_dsecundaria.append(matriz[i][j])

print("Vector con los primos de la diagonal principal: ",v_primos_dprincipal)
print("Vector con los primos de la diagonal secundaria: ",v_primos_dsecundaria)

#### Punto 8


#### punto 9 (Determinar si el segundo primo es consecutivo con el cuarto primo al recorrer la matriz por COLUMNAS)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
si_primo=0
print("Primos encontrados al recorrer matriz por COLUMNAS: ")
for j in range(columnas):
    for i in range(filas):
        c=1
        div=0
        while c<=matriz[i][j]:
            if matriz[i][j] % c==0:
                div+=1
            c+=1

        if div==2:
            si_primo+=1
            if si_primo==2:
                segundo_primo=matriz[i][j]
                print("Segundo primo: ",matriz[i][j])
                print("Ubicado en la columna: ",j)
                print("Fila: ",i) 
            elif si_primo==4:
                cuarto_primo=matriz[i][j]
                print("Cuarto primo: ",matriz[i][j])
                print("Ubicado en la columna: ",j)
                print("Fila: ",i)

if cuarto_primo<segundo_primo:
    aux=segundo_primo
    segundo_primo=cuarto_primo
    cuarto_primo=aux

c_remplazo=segundo_primo+1
b=0
while c_remplazo < cuarto_primo and b==0:
    c_2=1
    div=0
    while c_2<=c_remplazo:
        if c_remplazo % c_2==0:
            div+=1
        c_2+=1

    if div==2:
        b+=1
    else:
        c_remplazo+=1            

if b==0:
    print("El segundo y cuarto primo son consecutivos ya que no hay ningun primo entre estos")
else:
    print("El segundo primo y el cuarto primo No son consecutivos ya que en estos hay numeros primos")  

#### Punto 10 (Ordenar las columas pares de forma ascendente y las impares de forma descendente)
matriz = []
filas = int(input("Numero de filas: "))
columnas = int(input("Numero de columnas: "))

for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))
    matriz.append(fila)

print("Matriz original:")
for i in range(filas):
    for j in range(columnas):
        print("Fila: ",i," Columna: ",j," Dato= ",matriz[i][j])

for j in range(columnas):
    if j % 2 == 0:  # Columnas pares
        for i in range(filas - 1):
            for k in range(i + 1, filas):
                if matriz[k][j] < matriz[i][j]:
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[k][j]
                    matriz[k][j] = aux
    else:  # Columnas impares
        for i in range(filas - 1):
            for k in range(i + 1, filas):
                if matriz[k][j] > matriz[i][j]:
                    aux = matriz[i][j]
                    matriz[i][j] = matriz[k][j]
                    matriz[k][j] = aux

print("Matriz ordenada en columnas pares ascendentes y columnas impares descendentes:")
for i in range(filas):
    for j in range(columnas):
        print("Fila: ",i," Columna: ",j," Dato= ",matriz[i][j])

#### Punto 11 (dos matrices ordenadas ascendentemente, obtener un vector ordenado ascendentemente por mezcla )
matriz_1 = []
matriz_2 = []
vector = []

filas_1 = int(input("Filas en matriz 1: "))
columnas_1 = int(input("Columnas en matriz : "))
print("Digite los datos de la matriz 1 en orden ascendente: ")
for i in range(filas_1):
    fila_1 = []
    for j in range(columnas_1):
        fila_1.append(int(input(f'Dato({i},{j})= ')))
    matriz_1.append(fila_1)

filas_2 = int(input("Filas en matriz 2: "))
columnas_2 = int(input("Columnas en matriz 2: "))
print("Digite los datos de la matriz 2 en orden ascendente: ")
for i in range(filas_2):
    fila_2 = []
    for j in range(columnas_2):
        fila_2.append(int(input(f'Dato({i},{j})= ')))
    matriz_2.append(fila_2)

print("Matriz 1: ", matriz_1, " Matriz 2: ", matriz_2)

i = 0  # filas matriz 1
j = 0  # columnas matriz 1
z = 0  # filas matriz 2
x = 0  # columnas matriz 2

while i < filas_1 or z < filas_2:
    if i == filas_1:
        vector += matriz_2[z][x:]
        break
    elif z == filas_2:
        vector += matriz_1[i][j:]
        break
    elif matriz_1[i][j] < matriz_2[z][x]:
        vector.append(matriz_1[i][j])
        j += 1
        if j == columnas_1:
            j = 0
            i += 1
    else:
        vector.append(matriz_2[z][x])
        x += 1
        if x == columnas_2:
            x = 0
            z += 1

print("Vector ordenado por mezcla: ", vector)

#Punto 12(Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila)
matriz_1 = []
filas_1 = int(input("Filas en matriz 1: "))
columnas_1 = int(input("Columnas en matriz : "))
print("Digite los datos de la matriz 1 en orden ascendente: ")
for i in range(filas_1):
    fila_1 = []
    for j in range(columnas_1):
        fila_1.append(int(input(f'Dato({i},{j})= ')))
    matriz_1.append(fila_1)

print("Matriz original:")
for fila in matriz_1: #me saca la matriz de una forma mas lejible, como uma matriz en papel
    print(fila)

promedios = []
for i in range(filas_1):
    suma = sum(matriz_1[i])
    promedio = suma / columnas_1
    print("promedio fila ",i," = ",promedio)
    promedios.append(promedio)

for i in range(filas_1 - 1):
    for j in range(i + 1, filas_1):
        if promedios[i] > promedios[j]:
            matriz_1[i], matriz_1[j] = matriz_1[j], matriz_1[i]
            promedios[i], promedios[j] = promedios[j], promedios[i]

print("Matriz con filas intercambiadas por promedios ascendentes:")
for fila in matriz_1:
    print(fila)

##### Punto 15 (Formar un vector con aquellos contadores de datos que se repiten y que sean numeros fibonaccis, sin repetidos)
matriz=[]
filas=int(input("Numero de filas: "))
columnas=int(input("Numero de columnas: "))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})= ')))
    matriz.append(fila) 

datos_no_repetidos=[]
contador=[]
print(matriz)
for i in range(filas):
    for j in range(columnas):
        aux=matriz[i][j]
        if aux not in datos_no_repetidos:
            datos_no_repetidos.append(aux)
            contador.append(1)
        else:
            contador[datos_no_repetidos.index(aux)]+=1

for i in range(len(contador)):
    print("Dato: ",datos_no_repetidos[i]," Veces: ",contador[i])  

vector_contador=[]
for i in range(len(contador)):
    if contador[i]>1:
        a=0
        b=1
        t=0
        while t<contador[i]:
            t=a+b
            a=b
            b=t

        if contador[i]==t:
            print(contador[i],"es fibonacci")
            dato= contador[i] in vector_contador
            if dato==False:
                vector_contador.append(contador[i])

print("Vector con los contadores fibonaccis de los datos repetidos, (agregados sin repetir): ",vector_contador)


#####"""####"
#matriz = leer_matriz() #La línea (matriz = leer_matriz()) obtiene la matriz ingresada por el usuario y la almacena en la variable matriz.
                       #siempre debem asignarse los valores que se obtuvieron a una variable, esto para segur siendo utilizadas  
#promedio_primos = calculo_primos(matriz) #calcula el promedio de los números primos en la matriz utilizando la función calculo_primos(),
                                         # pasando la matriz como argumento, y almacena este promedio en la variable promedio_primos.
#si_fue_fibo= promedio_fibo(promedio_primos) 
