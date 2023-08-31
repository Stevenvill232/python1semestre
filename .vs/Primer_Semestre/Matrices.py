##### Llenar una matriz con un numero dado forma 1
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("numero de columnas= "))
numero=int(input("Numero dentro de matriz= "))
for i in range(filas):
    matriz.append([numero]*columnas)

print(matriz)

#### Llenar una matriz con un numero dado forma 2
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))
numero=int(input("Numero a llenar en matriz= "))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(numero)

    matriz.append(fila)

print(matriz)

####### Filas pares con 0 filas impares con 1
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))
for i in range(filas):
    if i % 2==0:
        matriz.append([0]*columnas)
    else:
        matriz.append([1]*columnas)

print(matriz)

##### Leer datos numericos desde un teclado para una matriz
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'dato {i},{j}=')))

    matriz.append(fila)

print(matriz)

##### Llenar DIAGONAL PRINCIPAL con 0 (Las filas son iguales que las columnas (i==j))
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        if i==j:
            fila.append(0)
        else:
            fila.append(1)

    matriz.append(fila)            

print(matriz)

##### Llenar DIAGONAL SECUNDARIA con 0 (i+j==columnas-1)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        if i+j==columnas-1:
            fila.append(0)
        else:
            fila.append(1)

    matriz.append(fila)
                
print(matriz)

#### Hallar el promedio de los numeros pares de una matriz
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'dato {i},{j}=')))

    matriz.append(fila)

print(matriz)
#sumar y contar pares de la matriz
suma_pares=0
contador_pares=0
for i in range(filas):
    for j in range(columnas):
        if matriz[i][j] % 2==0:
            print(matriz[i][j],"es par")
            suma_pares+=matriz[i][j]
            contador_pares+=1

#Hallar promedio de pares
if contador_pares>0:
    promedio_pares=suma_pares/contador_pares
    print("Promedio de pares de la matriz= ",promedio_pares)
else:
    print("No hay pares en la matriz")

##### Hallar promedio de fibonaccis y primos
matriz=[]
filas=int(input("Cantidad de filas= "))
columnas=int(input("Cantidad de columnas= "))
for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato {i},{j} =')))
    matriz.append(fila)

print(matriz)
suma_fibo=0
contador_fibo=0
suma_primos=0
contador_primos=0
for i in range(filas):
    for j in range(columnas):
        c=1
        div=0
        while c <= matriz[i][j]:
            if matriz[i][j] % c==0:
                div+=1
            c+=1

        if div==2:
            suma_primos+=matriz[i][j]
            contador_primos+=1

        a=0
        b=1
        t=0
        while t < matriz[i][j]:
            t=a+b
            a=b
            b=t

        if matriz[i][j]==t:
            suma_fibo+=matriz[i][j]
            contador_fibo+=1

if contador_primos>0:
    promedio_primos=suma_primos/contador_primos
    print("Promedio de primos de la matriz= ",promedio_primos)
else:
    print("No hay primos en la matriz")

if contador_fibo>0:
    promedio_fibonaccis=suma_fibo/contador_fibo
    print("Promedio de fibonaccis= ",promedio_fibonaccis)
else:
    print("No hay fibonaccis en la matriz")    

#### Intercambias la primera fila de la matriz con la ultima
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
    aux=matriz[0][j]
    matriz[0][j]=matriz[-1][j]
    matriz[-1][j]=aux

print(matriz)

#### Intercambias la primera columna con la ultima de cada fila
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
for i in range(filas):
    aux=matriz[i][0]
    matriz[i][0]=matriz[i][-1]
    matriz[i][-1]=aux

print(matriz)

#### Ordenar la diagonal principal de la matriz
matriz=[]
orden=int(input("Orden de la matriz= "))
for i in range(orden):
    fila=[]
    for j in range(orden):
        fila.append(int(input(f'Dato ({i},{j})=')))

    matriz.append(fila)

print(matriz)
#intercambiar filas
for i in range(orden-1):
    for j in range(i+1,orden):
        if matriz[j][j]<matriz[i][i]:
            aux=matriz[i][i]
            matriz[i][i]=matriz[j][j]
            matriz[j][j]=aux

print(matriz)

#### Ordenar diagonal secundaria de la matriz
matriz=[]
orden=int(input("Orden de la matriz= "))
for i in range(orden):
    fila=[]
    for j in range(orden):
        fila.append(int(input(f'Dato ({i},{j})=')))

    matriz.append(fila)

print(matriz)
#intercambiar filas     (orden-1-j)=diagonal secundaria   (orden-1-i)=diagonal principal3
for i in range(orden-1):
    for j in range(i+1,orden):  
        if matriz[j][orden-1-j]<matriz[i][orden-1-i]:
            aux=matriz[i][orden-1-i]
            matriz[i][orden-1-i]=matriz[j][orden-1-j]
            matriz[j][orden-1-j]=aux

print(matriz)

#### Hallar el mayor, menor y promedio de toda la matriz
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
menor=matriz[0][0]
suma=0
contador=0
for i in range(filas):
    for j in range(columnas):
        suma+=matriz[i][j]
        contador+=1
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
        elif matriz[i][j]<menor:
            menor=matriz[i][j]

promedio=suma/contador
print("Mayor de la matriz: ",mayor," Menor: ",menor,"Promedio= ",promedio)

#### Hallar el primo mayor, menor y el promedio de los primos de la matriz
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)

suma=0
contador=0
sipri=0
for i in range(filas):
    for j in range(columnas):
        c=1
        div=0
        while c<= matriz[i][j]:
            if matriz[i][j] % c==0:
                div+=1
            c+=1

        if div==2:
            print(matriz[i][j],"Es primo")
            suma+=matriz[i][j]
            contador+=1
            sipri+=1
            if sipri==1:
                mayor=matriz[i][j]
                menor=matriz[i][j]
            else:
                if matriz[i][j]>mayor:
                    mayor=matriz[i][j]
                elif matriz[i][j]<menor:
                    menor=matriz[i][j]           

if contador>0:
    promedio=suma/contador
    print("Primo mayor: ",mayor," Primo menor: ",menor," Promedio de primos= ",promedio)
else:
    print("No hay primos en la matriz")

##### Hallar el mayor, menor y promedio de cada fila 
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
for i in range(filas):
    mayor=matriz[i][0]
    menor=matriz[i][0]
    suma=0
    for j in range(columnas):
        if matriz[i][j]>mayor:
            mayor=matriz[i][j]
        elif matriz[i][j]<menor:
            menor=matriz[i][j]

        suma+=matriz[i][j]

    promedio=suma/columnas
    print("Promedio fila ",i," = ",promedio)
    print("Mayor: ",mayor)
    print("Menor: ",menor)     

##### Ordenar las filas de la matriz (con Funcion)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))
        fila.sort()

    matriz.append(fila)

print(matriz)

##### Ordenar toda la matriz de menor a mayor
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))

    matriz.append(fila)

print(matriz)
for i in range(filas):
    for j in range(columnas):
        p=i
        q=j
        while p<filas:
            while q<columnas:
                if matriz[p][q]<matriz[i][j]:   #Cambiamos el "<" a ">" para ordenarla de mayor a menor
                    aux=matriz[i][j]
                    matriz[i][j]=matriz[p][q]
                    matriz[p][q]=aux
                q+=1
            p+=1
            q=0 #Para garantizar que la siguiente fila inicie en 0

print(matriz)

#### Ordenar las filas pares de la matriz (Con funcion)
matriz=[]
filas=int(input("Numero de filas= "))
columnas=int(input("Numero de columnas= "))

for i in range(filas):
    fila=[]
    for j in range(columnas):
        fila.append(int(input(f'Dato({i},{j})=')))
        if i % 2==0:
            fila.sort()

    matriz.append(fila)

print(matriz)

#####Se tienen dos matrices, crear un vector con los numeros primos
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
                    v_resultante.append(matriz1[i][j])
                    na+=1

print("Vector resultante con numeros primos= ",v_resultante)

##### Forma de escribir una matriz de forma cuadrada 
print("Matriz original:")
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j], end="\t")
    print()
