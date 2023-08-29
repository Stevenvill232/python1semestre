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

#### Punto 8 (Se tiene una matriz cuadrada con datos numéricos, Comparar el promedio de los números pares que están sobre la diagonal principal)
#con el promedio de los impares de los datos que están bajo la diagonal principal.

dimension=int(input("Numero de filas y columnas: "))
matriz=[]
for i in range(dimension):
    fila=[]
    for j in range(dimension):
        fila.append(int((input(f'Dato({i},{j})= '))))

    matriz.append(fila) 

sum_pares = 0
count_pares = 0
sum_impares = 0
count_impares = 0
# Calcular promedio de pares sobre la diagonal principal
for i in range(dimension):
    for j in range(dimension):
        if i < j and matriz[i][j] % 2 == 0:
            sum_pares += matriz[i][j]
            count_pares += 1

# Calcular promedio de impares bajo la diagonal principal
for i in range(dimension):
    for j in range(dimension):
        if i > j and matriz[i][j] % 2 != 0:
            sum_impares += matriz[i][j]
            count_impares += 1

if count_pares > 0:
    promedio_pares = sum_pares / count_pares
else:
    promedio_pares = 0
    print("No hay números pares sobre la diagonal principal.")

if count_impares > 0:
    promedio_impares = sum_impares / count_impares
else:
    promedio_impares = 0
    print("No hay números impares bajo la diagonal principal.")

if promedio_pares > 0 and promedio_impares > 0:
    if promedio_pares > promedio_impares:
        print(f"El promedio de los números pares sobre la diagonal principal ({promedio_pares}) es mayor que el promedio de los números impares bajo la diagonal principal ({promedio_impares}).")
    elif promedio_impares > promedio_pares:
        print(f"El promedio de los números impares bajo la diagonal principal ({promedio_impares}) es mayor que el promedio de los números pares sobre la diagonal principal ({promedio_pares}).")
    else:
        print("Los promedios son iguales.")

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


##### Punto 10 (Ordenar las columas pares de forma ascendente y las impares de forma descendente)
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

#### Punto 12(Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila)
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

#######  Punto 13 
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

#¡¡¡¡ QUITAS LOS "#" DE LO SIGUIENTE Y ASI FUNCIONAN LOS SUBPROGRAMAS ¡¡¡¡
matriz= leer_matriz() #obligatorio(Siempre lo debes dejar activo para que funcione lo demas)
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
                                     

#¡¡¡¡ QUITAS LOS "#" DE LO SIGUIENTE Y ASI FUNCIONAN LOS SUBPROGRAMAS ¡¡¡¡
matriz_1, matriz_2 = leer_dos_matrices()  #obligatorio(Siempre lo debes dejar activo para que funcione lo demas)
#vector_datos_comunes = vector_elementos_comunes(matriz_1, matriz_2)
#vector_datos_primos_comunes = vector_primos_comunes(matriz_1,matriz_2)


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

def intercambiar_filas_mayor_menor(matriz):
    mayor = matriz[0][0]
    menor = matriz[0][0]
    fila_mayor = 0
    fila_menor = 0
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if suma_fila > mayor:
            mayor = suma_fila
            fila_mayor = i
        
        if suma_fila < menor:
            menor = suma_fila
            fila_menor = i
    
    matriz[fila_mayor], matriz[fila_menor] = matriz[fila_menor], matriz[fila_mayor]
    
    print("Matriz con filas intercambiadas según el mayor y el menor de cada fila: ")
    for fila in matriz:
        print(fila)

def encontrar_fibonacci(numero):
    a = 0
    b = 1
    t = 0
    
    while t < numero:
        t = a + b
        a = b
        b = t
    
    return t == numero

def intercambiar_filas_fibonacci_2_4(matriz):
    fila_fibonacci_2 = None
    fila_fibonacci_4 = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if encontrar_fibonacci(suma_fila):
            if fila_fibonacci_2 is None:
                fila_fibonacci_2 = i
            elif fila_fibonacci_4 is None:
                fila_fibonacci_4 = i
    
    if fila_fibonacci_2 is not None and fila_fibonacci_4 is not None:
        matriz[fila_fibonacci_2], matriz[fila_fibonacci_4] = matriz[fila_fibonacci_4], matriz[fila_fibonacci_2]
        print("Matriz con filas intercambiadas entre Fibonacci 2 y Fibonacci 4: ")
        for fila in matriz:
            print(fila)
    else:
        print("No se encontraron filas con Fibonacci 2 y Fibonacci 4.")

def intercambiar_filas_primo_fibonacci_menor(matriz):
    primo_mayor = None
    fibonacci_menor = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        
        if suma_fila > primo_mayor and encontrar_primo(suma_fila):
            primo_mayor = suma_fila
        
        if suma_fila < fibonacci_menor and encontrar_fibonacci(suma_fila):
            fibonacci_menor = suma_fila
    
    if primo_mayor is not None and fibonacci_menor is not None:
        fila_primo_mayor = None
        fila_fibonacci_menor = None
        
        for i in range(len(matriz)):
            suma_fila = sum(matriz[i])
            if suma_fila == primo_mayor:
                fila_primo_mayor = i
            if suma_fila == fibonacci_menor:
                fila_fibonacci_menor = i
        
        if fila_primo_mayor is not None and fila_fibonacci_menor is not None:
            matriz[fila_primo_mayor], matriz[fila_fibonacci_menor] = matriz[fila_fibonacci_menor], matriz[fila_primo_mayor]
            print("Matriz con filas intercambiadas entre primo mayor y Fibonacci menor: ")
            for fila in matriz:
                print(fila)
        else:
            print("No se encontraron filas con los valores adecuados.")
    else:
        print("No se encontraron filas con primo mayor y Fibonacci menor.")

def encontrar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def consecutivos_primo_2_4(matriz):
    posicion_primo_2 = None
    posicion_primo_4 = None
    
    for i in range(len(matriz)):
        suma_fila = sum(matriz[i])
        if suma_fila == 2 and encontrar_primo(suma_fila):
            posicion_primo_2 = i
        if suma_fila == 4 and encontrar_primo(suma_fila):
            posicion_primo_4 = i
    
    if posicion_primo_2 is not None and posicion_primo_4 is not None:
        if abs(posicion_primo_2 - posicion_primo_4) == 1:
            print("Los primos 2 y 4 son consecutivos.")
        else:
            print("Los primos 2 y 4 no son consecutivos.")
    else:
        print("No se encontraron filas con primos 2 y 4.")

#¡¡¡¡ QUITAS LOS "#" DE LO SIGUIENTE Y ASI FUNCIONAN LOS SUBPROGRAMAS ¡¡¡¡
matriz_intercambio_columnas = intercambio_columnas(matriz) #obligatorio(Siempre lo debes dejar activo para que funcione lo demas)
#mayor_menor_promedio_columnas(matriz)
#ordenar_filas_pares_impares(matriz)
#matriz_ordenada_descendentemente = orden_matriz_descendente(matriz)
#intercambiar_filas_promedio_ascendente(matriz)       
#intercambiar_filas_mayor_menor(matriz)
#intercambiar_filas_fibonacci_2_4(matriz)
#intercambiar_filas_primo_fibonacci_menor(matriz)
#consecutivos_primo_2_4(matriz)

