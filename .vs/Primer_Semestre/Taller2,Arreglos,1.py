#Ejercicio 1 (determinar cual es el primo que mas se repite)
print("Ejercicio 1 (determinar cual es el primo que mas se repite)")
cantidad_datos=int(input("Cantidad de datos= "))
vector=[]
datos_no_repetidos=[]
contador=[]
for i in range(cantidad_datos):
    vector.append(int(input("Dato({})=".format(i))))

x=0
hay_primos=0
for i in range(cantidad_datos):
    j=0
    b=0
    while j<x and b==0:
        if vector[i]==datos_no_repetidos[j]:
            b=1
        else:
            j+=1

    if b==0:
        c=1
        div=0
        while c<=vector[i]:
            if vector[i]%c==0:
                div+=1
            c+=1

        if div==2:
            hay_primos+=1
            datos_no_repetidos.append(vector[i])
            x+=1
            contador.append(1)
    else:
        contador[j]+=1

if hay_primos>0:
    print("Primos del vector: ",datos_no_repetidos)
    primo_mas_repetido=contador[0]
    posicion=0
    j=1
    for j in range(len(contador)):
        if contador[j]>primo_mas_repetido:
            primo_mas_repetido=contador[j]
            posicion=j

    print("primo mas repetido del vector",datos_no_repetidos[posicion],"con",contador[posicion],"veces")        
else:
    print("No hay primos en el vector")

print("Fin algoritmo")

#Ejercicio 2 (eliminar los numeros pares)
print("Ejercicio 2 (eliminar los numeros pares)")
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

i=0
while i<len(l1):
    if l1[i] % 2==0:
        l1.remove(l1[i]) 
    else:
        i+=1       

print("Lista resultane sin numeros pares:",l1)
print("Fin algoritmo")
#Ejercicio 3(eliminar los datos que sean primos y fibonaccis)
print("Ejercicio 3(eliminar los datos que sean primos y fibonaccis)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
nuevo_vector=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))
    nuevo_vector.append(a[i])

for i in range(cantidad_datos):
    c=1
    div=0
    while c<=a[i]:
        if a[i] % c == 0:
            div+=1
        c+=1

    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t

    if a[i]==t or div==2:
        if a[i]==t and div==2:
            print(a[i],"Es primo y fibonacci")
        elif a[i]==t:
           print(a[i],"Es fibonacci")
        elif div==2:
           print(a[i],"Es primo")

        dato=a[i] in nuevo_vector
        if dato==True:
            nuevo_vector.remove(a[i])

print("Vector sin primos y fibonaccis:",nuevo_vector)
print("Fin algoritmo")

#Ejercicio 4 (Insertar varios datos numericos en la posicion que corresponda)
print("Ejercicio 4 (Insertar varios datos numericos en la posicion que corresponda)")
a=[]
cantidad_datos=int(input("Cantidad de datos en vector 1= "))
for j in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(j))))
    

cantidad_datos_insertar=int(input("Cantidad de datos a insertar= "))
for i in range(cantidad_datos_insertar):
    a.append(int(input("Numero: ")))

for i in range(len(a)-1):
    menor=a[i]
    posicion=i
    j=i+1
    while j<len(a):
        if a[j]<menor:
            menor=a[j]
            posicion=j
        j+=1

    aux=a[i]
    a[i]=a[posicion]
    a[posicion]=aux

for x in range(len(a)):
    print("Posicion ",x," Dato ",a[x])

print("Fin algoritmo")
#Ejercicio 5 (leer una serie de numeros y llenarlos en un vector de tal forma que queden ordenados de forma ascendente)
print("Ejercicio 5 (leer una serie de numeros y llenarlos en un vector de tal forma que queden ordenados de forma ascendente)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Numero=")))

i=0
while i< cantidad_datos-1:
    menor=a[i]
    pos=i
    j=i+1
    while j< cantidad_datos:
        if a[j]<menor:
            menor=a[j]
            pos=j
        j+=1    

    aux=a[i]
    a[i]=a[pos]
    a[pos]=aux
    i+=1

for i in range(cantidad_datos):
    print("posicion: ",i,"dato= ",a[i])

print("Fin algoritmo")
#Ejercicio 6 (leer una serie de numeros y llenar los primos y fibonaccis en un vector el cual quede ordenado ascendentemente)
print("Ejercicio 6 (leer una serie de numeros y llenar los primos y fibonaccis en un vector el cual quede ordenado ascendentemente)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
vector_total=[]
for i in range(cantidad_datos):
    a.append(int(input("Numero=")))

for i in range(cantidad_datos):
    c=1
    div=0
    while c<= a[i]:
        if a[i] % c==0:
            div+=1
        c+=1

    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t

    if a[i]==t or div==2:
        if a[i]==t and div==2:
            print(a[i],"es fibonacci y primo")
        elif div==2:
            print(a[i],"Es primo")
        elif a[i]==t:
            print(a[i],"Es fibonacci")

        dato=a[i] in vector_total
        if dato== False:
            vector_total.append(a[i])        

for i in range(len(vector_total)-1):
    menor=vector_total[i]
    pos=i
    j=i+1
    while j< len(vector_total):
        if vector_total[j]<menor:
            menor=vector_total[j]
            pos=j
        j+=1    

    aux=vector_total[i]
    vector_total[i]=vector_total[pos]
    vector_total[pos]=aux
    i+=1

print("Vector ordenado con numeros primos y fibonaccis:")
for i in range(len(vector_total)):
    print("posicion: ",i,"dato= ",vector_total[i])

print("Fin algoritmo")
#Ejercicio 7 (ordenar las posiciones pares en orden ascendente y las impares en orden descendente)
print("Ejercicio 7 (ordenar las posiciones pares en orden ascendente y las impares en orden descendente)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

for i in range(len(a)-1):
    if i % 2==0:
        menor=a[i]
        pos_menor=i
        j=i+1
        while j< len(a):
            if a[j]<menor:
                menor=a[j]
                pos_menor=j  
            j+=1

        aux=a[i]
        a[i]=a[pos_menor]
        a[pos_menor]=aux
    else:
        mayor=a[i]
        pos_mayor=i
        j=i+1
        while j<len(a):
            if a[j]>mayor:
                mayor=a[j]
                pos_mayor=j
            j+=1

        aux=a[i]
        a[i]=a[pos_mayor]
        a[pos_mayor]=aux

for i in range(len(a)):
    print("Posicion: ",i,"dato= ",a[i])

print("Fin algotimo")
#Ejercicio 8 (ordenar la mitad del vector en forma ascendente y la otra mitad de forma descendente)
print("Ejercicio 8 (ordenar la mitad del vector en forma ascendente y la otra mitad de forma descendente)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

i=0
while i< (len(a)//2):
    Menor=a[i]
    pos_menor=i
    j=i+1
    while j< len(a)//2:
        if a[j]<Menor:
            Menor=a[j]
            pos_menor=j
        j+=1

    aux_0=a[i]
    a[i]=a[pos_menor]
    a[pos_menor]=aux_0
    i+=1

i=len(a)//2
while i < len(a)-1:
    mayor=a[i]
    pos_mayor=i
    j=i+1
    while j< len(a):
        if a[j]>mayor:
            mayor=a[j]
            pos_mayor=j
        j+=1

    aux_1=a[i]
    a[i]=a[pos_mayor]
    a[pos_mayor]=aux_1
    i+=1        

for i in range(len(a)):
    print("Posicion: ",i,"Dato= ",a[i])

print("Fin algoritmo")
#Ejercicio 9 (apartir de un vector formar otros dos, uno con los datos pares y otro con los primos, ordenarlos ascendente y descendente respectivamente)
print("Ejercicio 9 (apartir de un vector formar otros dos, uno con los datos pares y otro con los primos, ordenarlos ascendente y descendente respectivamente)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
v_pares=[]
v_primos=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],"es par")
        dato_par= a[i] in v_pares
        if dato_par==False:
            v_pares.append(a[i])

for i in range(len(a)):
    c=1
    div=0
    while c<=a[i]:
        if a[i]%c==0:
            div+=1
        c+=1

    if div==2:
        print(a[i],"Es primo")
        dato_primo= a[i] in v_primos
        if dato_primo== False:
            v_primos.append(a[i])

for i in range(len(v_pares)-1):
    menor=v_pares[i]
    pos_menor=i
    j=i+1
    while j< len(v_pares):
        if v_pares[j]<menor:
            menor=v_pares[j]
            pos_menor=j
        j+=1

    aux_0=v_pares[i]
    v_pares[i]=v_pares[pos_menor]
    v_pares[pos_menor]=aux_0

print("Vector con pares ordenado ascendentemente:",v_pares)
for i in range(len(v_primos)-1):
    mayor=v_primos[i]
    pos_mayor=i
    j=i+1
    while j< len(v_primos):
        if v_primos[j]>mayor:
            mayor=v_primos[j]
            pos_mayor=j
        j+=1

    aux_1=v_primos[i]
    v_primos[i]=v_primos[pos_mayor]
    v_primos[pos_mayor]=aux_1

print("Vector con primos ordenados descendentemente:",v_primos)
print("Fin algoritmo")
#Ejercicio 10 (Se tiene vector con datos numericos ordenados y repetidos, mostrar los numeros y veces que se repiten, utilizar rompimiento de control)
print("Ejercicio 10(Se tiene vector con datos numericos ordenados y repetidos, mostrar los numeros y veces que se repiten, utilizar rompimiento de control)")
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

aux=a[0]
i=0
while i < cantidad_datos:
    contador=0
    while i < cantidad_datos and a[i]==aux:
        contador+=1
        i+=1    

    if contador==1:
        print("Dato: ",aux,"Se repite= ",contador,"vez")
    else:
        print("Dato: ",aux,"Se repite= ",contador,"veces")
            
    if i < cantidad_datos:
        aux=a[i] 

print("Fin algoritmo")



#######EXAMEBN
def leer_matriz():
    matriz=[]
    filas=int(input("Filas: "))
    columnas=int(input("Columnas: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)

    print("matriz:")
    for fila in matriz:
        print(fila)

    return matriz 


def primo(matriz):
    si_primo=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c=1
            div=0
            while c<=matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                si_primo+=1
                if si_primo==1:
                    primo_mayor=matriz[i][j]
                    columna_primo=j
                else:
                    if matriz[i][j]>primo_mayor:
                        primo_mayor=matriz[i][j]
                        columna_primo=j

    print("Primo mayor: ",primo_mayor,"Columna: ",columna_primo)
    return primo_mayor,columna_primo

def fibonacci(matriz):
    si_fibonacci=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a=0
            b=1
            t=0
            while t< matriz[i][j]:
                t=a+b
                a=b
                b=t
            if matriz[i][j]==t:
                si_fibonacci+=1
                if si_fibonacci==1:
                    fibonacci_menor=matriz[i][j]
                    columna_fibonacci=j
                elif matriz[i][j]<fibonacci_menor:
                    fibonacci_menor=matriz[i][j]
                    columna_fibonacci=j

    print("Fibonacci menor: ",fibonacci_menor,"Columna: ",columna_fibonacci)
    return fibonacci_menor,columna_fibonacci

def orden_columnas(matriz,columna_primo,columna_fibonacci):
    nf= len(matriz)
    #columna primo
    for i in range(nf):
        for j in range(i+1,nf):
            if matriz[j][columna_primo]<matriz[i][columna_primo]:
                matriz[j][columna_primo],matriz[i][columna_primo] = matriz[i][columna_primo],matriz[j][columna_primo]

    #columna fibonacci
    for i in range(nf):
        for j in range(i+1,nf):
            if matriz[j][columna_fibonacci]>matriz[i][columna_fibonacci]:
                matriz[j][columna_fibonacci],matriz[i][columna_fibonacci] = matriz[i][columna_fibonacci],matriz[j][columna_fibonacci]

    print("Matriz resultante con columnas de primo menor ordenada ascendentemente y columna fibonacci descendentemente")
    for fila in matriz:
        print(fila)                     


matriz=leer_matriz()
primo_mayor,columna_primo=primo(matriz)
fibonacci_menor,columna_fibonacci=fibonacci(matriz)
orden_columnas(matriz,columna_primo,columna_fibonacci)


def leer_matriz():
    matriz = []
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)

    print("Matriz:")
    for fila in matriz:
        print(fila)

    return matriz

def vector_fibonaccis(matriz):
    vector = []
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            a = 0
            b = 1
            t = 0
            while t < matriz[i][j]:
                t = a + b
                a = b
                b = t
                
            if matriz[i][j] == t:
                b1 = 0
                p = 0
                while p < filas and b1 == 0:
                    q = 0
                    while q < columnas and b1 == 0:
                        if matriz[i][j] == matriz[p][q]:
                            b1 = 1
                        else:
                            q += 1
                    p += 1

                if b1 == 1:
                    b2 = 0
                    x = 0
                    while x < len(vector) and b2 == 0:
                        if matriz[i][j] == vector[x]:
                            b2 = 1
                        else:
                            x += 1

                    if b2 == 0:
                        print(matriz[i][j], " Fibonacci comun")
                        vector.append(matriz[i][j])

    print("Vector resultante con numeros fibonaccis comunes sin repetir: ", vector)
    return vector


def contar_fibonaccis(matriz, vector_fibonaccis):
    contador_fibonaccis = [0] * len(vector_fibonaccis)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = matriz[i][j]
            if numero in vector_fibonaccis:
                index = vector_fibonaccis.index(numero)
                contador_fibonaccis[index] += 1
                
    print("Vector de conteo de números Fibonacci en la matriz:")
    for i in range(len(vector_fibonaccis)):
        print(f"Número {vector_fibonaccis[i]}: {contador_fibonaccis[i]} veces")
    
    return contador_fibonaccis

matriz = leer_matriz()
vector = vector_fibonaccis(matriz)
contar_fibonaccis(matriz,vector)
