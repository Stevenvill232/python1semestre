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

#11.	Se tienen dos vectores con datos numéricos, en el primer vector hay números múltiplos de tres
#que determinan la cantidad de datos de rangos correspondientes al vector dos
#encontrar el mayor, el menor y el promedio de cada rango.
print("Ejercicio 11 (Se tienen dos vectores, el primero determina el rango de datos que tendra el segundo vector)")
datos = []
rango = []
cantidad_datos_rango = int(input("Cantidad de datos de la lista de rango: "))
cantidad_datos_lista = int(input("Cantidad de elementos de la lista datos: "))

for i in range(cantidad_datos_rango):
    rango.append(int(input("Digitar valor rango({})=".format(i))))

for j in range(cantidad_datos_lista):
    datos.append(int(input("Digitar valor dato({})=".format(j))))

i = 0
c = 0

while i < cantidad_datos_rango:
    if rango[i] % 3 == 0:
        limite_final = c + rango[i]  # Usamos c como inicio del rango
        mayor = datos[c]
        menor = datos[c]
        promedio = 0
        contador = 0
        sumador = 0
        while c < limite_final:  # Usamos c para iterar sobre los datos del rango
            contador += 1
            sumador += datos[c]
            promedio = sumador / contador
            if datos[c] > mayor:
                mayor = datos[c]
            elif datos[c] < menor:
                menor = datos[c]
            c += 1  # Incrementamos c

        print("Rango", i, "Mayor:", mayor, "Menor:", menor, "Promedio del rango:", promedio)
        i += 1

print("Fin algoritmo")
#Ejercicio 12 (Se tienen dos vectores, forman un tercero con los primos comunes sin repetirse)
print("Ejercicio 12 (Se tienen dos vectores, forman un tercero con los primos comunes sin repetirse)")
a=[]
v=[]
p=[]
cantidad_datosA=int(input("Cantidad de datos en vector a="))
for i in range(cantidad_datosA):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datosB=int(input("Cantidad de datos en vector b="))
for j in range(cantidad_datosB):
    v.append(int(input("Dato({})=".format(j))))

for i in range(cantidad_datosA):
    c=1
    div=0
    while c<=a[i]:
        if a[i]%c==0:
            div+=1
        c+=1

    if div==2:
        dato= a[i] in v
        if dato== True:
            print(a[i],"Es primo comun")
            dato_2= a[i] in p
            if dato_2==False:
                p.append(a[i])

print("Vector con primos comunes sin repetirse:",p)
print("Fin algoritmo")
#Ejercicio 13 (Se tienen dos vectores, formar un tercero con la union de los fibonaccis sin repetirse)
print("Ejercicio 13 (Se tienen dos vectores, formar un tercero con la union de los fibonaccis sin repetirse)")
a=[]
v=[]
p=[]
cantidad_datosA=int(input("Cantidad de datos en vector a="))
for i in range(cantidad_datosA):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datosB=int(input("Cantidad de datos en vector b="))
for j in range(cantidad_datosB):
    v.append(int(input("Dato({})=".format(j))))

contador=0
for i in range(cantidad_datosA):
    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t
        
    if a[i]==t:
        print(a[i],"Es fibonacci")
        dato= a[i] in p
        if dato== False:
            p.append(a[i])

for j in range(cantidad_datosB):
    a_1=0
    b=1
    t=0
    while t<v[j]:
        t=a_1+b
        a_1=b
        b=t

    if v[j]==t:
        print(v[j],"Es fibonacci")
        dato_2= v[j] in p
        if dato_2== False:
            p.append(v[j])    

print("Vector con la union de fibonaccis sin repetirse:",p)
print("Fin algoritmo")
#Ejercicio 14 (Se tienen dos vectores, crear un tercer vecotor de forma descendente organizado por mezcla)
print("Ejercicio 14 (Se tienen dos vectores, crear un tercer vecotor de forma descendente organizado por mezcla)")
cantidad_datosA = int(input("Cantidad de datos en vector a= "))
print("Vector ordenado ascendentemente")
a = []
for i in range(cantidad_datosA):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datosB = int(input("Cantidad de datos en vector b= "))
print("Vector ordenado descendentemente")
v = []
for j in range(cantidad_datosB):
    v.append(int(input("Dato({})=".format(j))))

p = []
i = 0
j = cantidad_datosB-1

while i < cantidad_datosA and j >= 0:
    if v[j] < a[i]:
        p.append(v[j])
        j -= 1
    else:
        p.append(a[i])
        i += 1

while j>=0:
    p.append(v[j])
    j-=1

while i<cantidad_datosA:
    p.append(a[i])
    i+=1
#ordenar el vector "p" de mayor a menor
for x in range(len(p)-1):
    c=x+1
    mayor=p[x]
    pos=x
    while c<len(p):
        if p[c]>mayor:
            mayor=p[c]
            pos=c
        c+=1

    aux=p[x]
    p[x]=p[pos]
    p[pos]=aux

print(p)
print("Fin algoritmo")
#Ejercicio 15 (lo mismo que el anterior, unicamente que el vector nuevo solo llevara numeros pares)
print("Ejercicio 14 (Se tienen dos vectores, crear un tercer vecotor de forma descendente organizado por mezcla)")
cantidad_datosA = int(input("Cantidad de datos en vector a= "))
print("Vector ordenado ascendentemente")
a = []
for i in range(cantidad_datosA):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datosB = int(input("Cantidad de datos en vector b= "))
print("Vector ordenado descendentemente")
v = []
for j in range(cantidad_datosB):
    v.append(int(input("Dato({})=".format(j))))

p = []
i = 0
j = cantidad_datosB-1

while i < cantidad_datosA and j >= 0:
    if v[j] < a[i]:
        if v[j]%2==0:
            p.append(v[j])
        j -= 1
    else:
        if a[i]%2==0:
            p.append(a[i])
        i += 1

while j>=0:
    if v[j]%2==0:
        p.append(v[j])
    j-=1

while i<cantidad_datosA:
    if a[i]%2==0:
        p.append(a[i])
    i+=1
#ordenar el vector "p" de mayor a menor
for x in range(len(p)-1):
    c=x+1
    mayor=p[x]
    pos=x
    while c<len(p):
        if p[c]>mayor:
            mayor=p[c]
            pos=c
        c+=1

    aux=p[x]
    p[x]=p[pos]
    p[pos]=aux

print(p)
print("Fin algoritmo")
#Ejercicio 16 (Se tiene un vector con datos fibonaccis, formar un tercer vector con los primos entre el fibonacci menor y mayor)
print("Ejercicio 16 (Se tiene un vector con datos fibonaccis, formar un tercer vector con los primos entre el fibonacci menor y mayor)")
cantidad_datos=int(input("cantidad de datos= "))
a=[]
v=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

sifibo=0
for i in range(cantidad_datos):
    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t

    if a[i]==t:
        sifibo+=1 
        if sifibo==1:
            fibo_menor=a[i]
            fibo_mayor=a[i]
        else:
            if a[i]<fibo_menor:
                fibo_menor=a[i]
            elif a[i]>fibo_mayor:
                fibo_mayor=a[i]

print("Fibonacci menor:",fibo_menor)
print("Fibonacci mayor:",fibo_mayor)
print("Numeros primos entre estos fibonaccis:")
c=fibo_menor+1
while c<fibo_mayor:
    c_2=1
    div=0
    while c_2<=c:
        if c%c_2==0:
            div+=1
        c_2+=1

    if div==2:
        print(c)
        dato=c in v
        if dato==False:
            v.append(c)

    c+=1            

print("Vector con numeros primos entre fibpnacci mayor y menor:",v)
print("Fin algoritmo")
#Ejercicio 17 (Se tiene un vector con fibonaccis, hallar el promedio de los multiplos de tres entre el segundo y tercer fibonacci)
print("Ejercicio 17 (Se tiene un vector con fibonaccis, hallar el promedio de los multiplos de tres entre el segundo y tercer fibonacci)")
cantidad_datos=int(input("cantidad de datos= "))
a=[]
v=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

sifibo=0
for i in range(cantidad_datos):
    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t

    if a[i]==t:
        sifibo+=1 
        if sifibo==2:
            fibo_segundo=a[i]
        else:
            if sifibo==3:
                fibo_tercero=a[i]
                
print("Segundo fibonacci:",fibo_segundo)
print("Tercer fibonacci:",fibo_tercero)
if fibo_tercero<fibo_segundo:
    aux=fibo_segundo
    fibo_segundo=fibo_tercero
    fibo_tercero=aux

c=fibo_segundo+1
contador=0
sumador=0
print("Multiplos de tres entre estos dos:")
while c<fibo_tercero:
    if c%3==0:
        print(c)
        contador+=1
        sumador+=c
    c+=1

if contador>0:
    promedio=sumador/contador
    print("El promedio de estos numeros es: ",promedio)
else:
    print("No hay mulriplos de tres entre los dos fibonaccis") 

print("Fin algoritmo")
#Ejercicio 18 (Encontrar el segundo y tercer fibonacci,sus posiciones, reemplazzar las posiciones comprendidad entre estos dos por el factorial del fibonacci menor de los 2)
cantidad_datos=int(input("cantidad de datos= "))
a=[]
v=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

sifibo=0
for i in range(cantidad_datos):
    a_1=0
    b=1
    t=0
    while t<a[i]:
        t=a_1+b
        a_1=b
        b=t

    if a[i]==t:
        sifibo+=1 
        if sifibo==2:
            pos_segundo=i
            fibo_segundo=a[i]
        else:
            if sifibo==3:
                pos_tercero=i
                fibo_tercero=a[i]
                
print("Segundo fibonacci:",fibo_segundo,"Su posicion es:",pos_segundo)
print("Tercer fibonacci:",fibo_tercero,"Su posicion es:",pos_tercero)
if fibo_segundo<fibo_tercero:
    fibo_menor=fibo_segundo
elif fibo_segundo>fibo_tercero:
    fibo_menor=fibo_tercero
elif fibo_segundo==fibo_tercero:
    fibo_menor=fibo_segundo

c=fibo_menor
factorial=1
while c>=1:
    factorial=factorial*c
    c-=1

print("El fibonacci menor es:",fibo_menor,"su factorial es:",factorial)
print("Posiciones entre el segundo y terces fibonaccis reemplazados por el factorial:")
i=pos_segundo
while i<=pos_tercero:
    print("Posicion:",i,"Dato:",factorial)
    i+=1

print("Fin algoritmo")
