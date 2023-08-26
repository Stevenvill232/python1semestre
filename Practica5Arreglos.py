#Llenar datos en un vector
print("Llenar datos en un vector")
A = []
cd = int(input("Cantidad de datos: "))
i = 0

while i <= cd - 1:
    A.append(int(input("Dato({})=".format(i))))
    i += 1

print(A)
print("Fin algoritmo")
#Llenar un vector con 1
print("Llenar un vector con 1")
cd = int(input("Cantidad de datos: "))
a=[]
i=0
while i<cd:
    a.append(1)
    i+=1
    
print(a)
print("Fin algoritmo")
#Llenar la posicion par con 1 y la impar con 0
print("Llenar la posicion par con 1 y la impar con 0")
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
i=0
while i<cantidad_datos:
    if i % 2==0:
        v.append(1)
    else:
        v.append(0)
    i+=1        

print(v)
print("Fin algoritmo")
#Llenar la posicion par con 1 y la impar con 0, ahora con ciclo para
print("Llenar la posicion par con 1 y la impar con 0")
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
i=0
while i<cantidad_datos:
    if i % 2==0:
        v.append(1)
    else:
        v.append(0)
    i+=1        

for i in v:
    print(i)
    
print("Fin algoritmo")
#Sacar el mayor y menor de los datos en un vector
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato ({}) =".format(i))))

menor=v[0]
mayor=v[0]
i=1
for i in range(cantidad_datos):
    if v[i]<menor:
        menor=v[i]
    elif v[i]>mayor:
        mayor=v[i]

print(v)
print("Mayor de los datos= ",mayor)
print("Menor de los datos= ",menor)
print("Fin algoritmo")
#Encontrar un dato en un vector y su pisicion
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})=".format(i))))

dato_buscar=int(input("Dato a buscar en vector= "))
i=0
b=0
while i<cantidad_datos and b==0:
    if dato_buscar==v[i]:
        posicion=i
        b=1
    i+=1

if b==0:
    print("Dato a buscar: ",dato_buscar,"No se encuentra en el vector")
else:
    print("Dato a buscar: ",dato_buscar,"Esta en la posicion ",posicion) 

#Determinar cuantas veces se repite un dato en un vector
cantidad=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad):
    v.append(int(input("datos({})=".format(i))))

dato_buscar=int(input("Dato a contar= "))
contador=0
for i in range(cantidad):
    if v[i]==dato_buscar:
        contador+=1

if contador>0:
    print("Dato a buscar",dato_buscar,"Se repite",contador,"Veces")
else:
    print("Dato a buscar no se encuentra en vector")    

#Determinar el promedio de los numeros impares de un vector
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato ({})= ".format(i))))

contador_impares=0
sumador_impares=0
for i in range(cantidad_datos):
    if a[i] % 2>0:
        print("Numeros impares: ")
        print(a[i])
        sumador_impares+=a[i]
        contador_impares+=1

if contador_impares>0:
    promedio=sumador_impares/contador_impares
    print("Promedio de los numeros impares= ",promedio)
else:
    print("No hay impares")

#Determinar el promedio de los numeros primos de un vector
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

suma_primos=0
contador_primos=0    

for i in range(cantidad_datos):
    c2=1
    div=0
    while c2 <= a[i]:
        if a[i] % c2==0:
            div+=1
        c2+=1

    if div==2:
        suma_primos+=a[i]
        contador_primos+=1
        print("Primos del vector:")
        print(a[i])

if contador_primos>0:
    promedio=suma_primos/contador_primos
    print("Promedio de los numeros primos= ",promedio)
else:
    print("No hay numeros primos")

#Determinar el promedio de los fibonacci de un vector
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

suma_fibonacci=0
contador_fibonacci=0

for i in range(cantidad_datos):
    a_1=0
    b_1=1
    t_1=0
    while t_1 < a[i]:
        t_1=a_1+b_1
        a_1=b_1
        b_1=t_1

    if a[i]==t_1:
        suma_fibonacci+=a[i]
        contador_fibonacci+=1
        print("Numero fibonacci: ",a[i])

if contador_fibonacci>0:
    promedio=suma_fibonacci/contador_fibonacci
    print("Promedio de fibonacci= ",promedio)
else:
    print("No hay fibonaccis")

#Determinar primo mayor y fibonacci menor
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

sifibo=0
siprimo=0

for i in range(cantidad_datos):
    a_1=0
    b_1=1
    t_1=0
    while t_1 < a[i]:
        t_1=a_1+b_1
        a_1=b_1
        b_1=t_1

    if a[i]==t_1:
        print("Fibonacci: ",a[i])
        sifibo+=1

        if sifibo==1:
            fibonacci_menor=a[i]
        elif a[i]<fibonacci_menor:
            fibonacci_menor=a[i]

    c2=1
    div=0
    while c2<=a[i]:
        if a[i] % c2==0:
            div+=1
        c2+=1
    if div==2:
        print("Primo: ",a[i])
        siprimo+=1
        if siprimo==1:
            primo_mayor=a[i]
        elif a[i]>primo_mayor:
            primo_mayor=a[i]

if sifibo>0:
    print("Fibonacci menor del vector= ",fibonacci_menor)
else:
    print("No hay fibonaccis")

if siprimo>0:
    print("Primo mayor del vector= ",primo_mayor)
else:
    print("No hay primos") 

#Determinar el promedio de los fibonaccis y primos de un vector
cantidad_datos=int(input("Cantidad de datos en el vector= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})=".format(i))))

contador_primos=0
sumador_primos=0
sumador_fibonaccis=0
contador_fibonaccis=0
for i in range(cantidad_datos):
    c=1
    div=0
    while c<=v[i]:
        if v[i]%c==0:
            div+=1
        c+=1

    if div==2:
        print(v[i],"Es primo")
        contador_primos+=1
        sumador_primos+=v[i]

    a=0
    b=1
    t=0
    while t<v[i]:
        t=a+b
        a=b
        b=t

    if v[i]==t:
        print(v[i],"Es fibonacci")
        contador_fibonaccis+=1
        sumador_fibonaccis+=v[i]

if contador_primos>0:
    promedio_primos=sumador_primos/contador_primos
    print("Promedio de los numeros primos= ",promedio_primos)
else:
    print("No hay primos en el vector")

if contador_fibonaccis>0:
    promedio_fibonaccis=sumador_fibonaccis/contador_fibonaccis
    print("Promedio de los numeros fibonaccis= ",promedio_fibonaccis)
else:
    print("No hay fibonaccis en el vector")

#Determinar si los dos primeros primos son consecutivos
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

siprimo=0

for i in range(cantidad_datos):
    c2=1
    div=0
    while c2<=a[i]:
        if a[i] % c2==0:
            div+=1
        c2+=1
    if div==2:
        siprimo+=1
        if siprimo==1:
            primo_1=a[i]
        else:
            if siprimo==2:
                primo_2=a[i]

if siprimo>0:
    print("Primo 1= ",primo_1)
    print("Primo 2= ",primo_2)
    if primo_2<primo_1:
        aux=primo_1
        primo_1=primo_2
        primo_2=aux

    c3=primo_1+1
    b=0
    while c3<primo_2:
        c4=1
        div2=0
        while c4<=c3:
            if c3 % c4==0:
                div2+=1
            c4+=1
        if div2==2:
            print("Entre medio esta: ",c3)
            b+=1    
        c3+=1 

    if b==0:
        print("Son consecutivos")
    else:
        print("No son consecutivos")        
else:
    print("No hay numeros primos")

#Determinar el menor del vector e intercambiarlo en la posicion 0
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

menor=a[0]
pos=0
i=1
for i in range(cantidad_datos):
    if a[i]<menor:
        menor=a[i]
        pos=i

aux=a[0]
a[0]=a[pos]
a[pos]=aux
print(a)

#Ordenar en el vector intercambiando datos 
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})=".format(i))))

j=0
while j<=cantidad_datos-2:
    menor=v[j]
    pos=j
    i=j+1
    while i<=cantidad_datos-1:
        if v[i]<menor:
            menor=v[i]
            pos=i
        i+=1
    aux=v[j]
    v[j]=v[pos]
    v[pos]=aux
    j+=1

print(v)

#Buscar un dato en una lista con funciones
cantidad_datos=int(input("cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

dato_buscar=int(input("Dato a buscar= "))
b=dato_buscar in a
if b==True:
    pos=a.index(dato_buscar)

if b==True:
    print("Dato a buscar:",dato_buscar,"Se encuentra en la posicion",pos)
else:
    print("Dato a buscar: ",dato_buscar,"No se encuentra en lista")

#obtener mayor y menor, y llenar entre el menor y el mayor con la multiplicacion de los dos
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})= ".format(i))))

mayor=v[0]
menor=v[0]
i=1
pos_mayor=0
pos_menor=0
for i in range(cantidad_datos):
    if v[i]>mayor:
        mayor=v[i]
        pos_mayor=i
    elif v[i]<menor:
        menor=v[i]
        pos_menor=i

multiplicacion=mayor*menor
print("Mayor: ",mayor,"(*) Menor: ",menor," = ",multiplicacion)
if pos_mayor<pos_menor:
    aux=pos_menor
    pos_menor=pos_mayor
    pos_mayor=aux

i=pos_menor+1
while i<=pos_mayor-1:
    print("Posicion",i,"Remplazada por la multiplicacion anterior= ",multiplicacion)
    i+=1  

#otra forma con vector ordenado (No es lo que realmente pide el ejercicio)
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})= ".format(i))))

v.sort()
mayor=v[-1]
print("Mayor del vector= ",mayor)
posicion_mayor=v.index(mayor)
menor=v[0]
print("Menor del vector= ",menor)
posicion_menor=v.index(menor)
multiplicacion=mayor*menor
print("Multiplicacion entre estos= ",multiplicacion)
print("Reemplazo:")
print(posicion_menor,"=",menor)
i=posicion_menor+1
while i<posicion_mayor:
    print(i,"=",multiplicacion)
    i+=1

print(posicion_mayor,"=",mayor)
#Sacar fibo mayor y menor y llenar entre estos con el fibo menor
cantidad_datos=int(input("Cantidad de datos= "))
v=[]
for i in range(cantidad_datos):
    v.append(int(input("Dato({})=".format(i))))

fibo_menor=0
fibo_mayor=0
pos_fibomayor=0
pos_fibomenor=0
sifibo=0
for i in range(cantidad_datos):
    a=0
    b=1
    t=0
    while t<v[i]:
        t=a+b
        a=b
        b=t

    if v[i]==t:
        sifibo+=1
        if sifibo==1:
            fibo_mayor=v[i]
            pos_fibomayor=i
            fibo_menor=v[i]
            pos_fibomenor=i
        else:
            if v[i]<fibo_menor:
                fibo_menor=v[i]
                pos_fibomenor=i
            elif v[i]>fibo_mayor:
                fibo_mayor=v[i]
                pos_fibomayor=i

print("Fibonacci mayor= ",fibo_mayor,"Su posicion es: ",pos_fibomayor)
print("Fibonacci menor= ",fibo_menor,"Su posicion es: ",pos_fibomenor)
if pos_fibomayor<pos_fibomenor:
    aux=pos_fibomenor
    pos_fibomenor=pos_fibomayor
    pos_fibomayor=aux

i=pos_fibomenor+1
while i<pos_fibomayor:
    print("Posicion",i,"Reemplazada pos fibonacci menor= ",fibo_menor)
    i+=1

#Crear un nuevo vector con datos sin repetir a partir de otro(Con funciones)
n = int(input("Cantidad de datos: "))
arreglo = []

for i in range(n):
    arreglo.append(int(input("Dato({})=".format(i))))

nuevo_arreglo = list(set(arreglo))

print("Arreglo original:", arreglo)
print("Nuevo arreglo sin datos repetidos:", nuevo_arreglo)

#Crear un nuevo vector con datos sin repetir a partir de otro(Sin funciones)
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
b=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

nb=0
for i in range(cantidad_datos):
    encontro=0
    x=0
    while x<nb and encontro==0:
        if a[i]==b[x]:
            encontro=1
        x+=1
    if encontro==0:
        b.append(a[i])
        nb+=1

print(b)
#Otra forma mejor
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
b=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

for i in range(cantidad_datos):
    encontro=a[i] in b
    if encontro==False:
        b.append(a[i])

print(b)
#Se tienen dos vectores formar uno nuevo con los datos comunes entre los 2 vectores sin repetirce
cantidad_datosA=int(input("Cantidad de datos vector A= "))
a=[]
print("Datos en vector A:")
for i in range(cantidad_datosA):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datosB=int(input("Cantidad de datos vector B= "))
b=[]
print("Datos en vector B:")
for j in range(cantidad_datosB):
    b.append(int(input("Dato({})=".format(i))))

c=[]

for i in range(cantidad_datosA):
    for j in range(cantidad_datosB):
        encontro=a[i] in b
        if encontro==True:
            encontro2=a[i] in c
            if encontro2==False:
                c.append(a[i])

print(c)

#Contar las veces que se repite cada dato en el vector(forma 1)
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
contados=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

x=0
nc=0
for i in range(cantidad_datos):
    b=0
    z=0
    #z es el indice que recorre vector "Contados"
    while z<x and b==0:
        if a[i]==contados[z]:
            b=1
        z+=1    
#el dato del vector a no estaria en el vector "Contados" por lo cual lo que hace es meterlo a este vector y a su vez 
#en el mismo vector "a" ir vienco cuantas veces se repitio, para eso es el indice j
    if b==0:
        con=1
        j=i+1
        while j<cantidad_datos:
            if a[i]==a[j]:
                con+=1
            j+=1

        contados.append(a[i])
        x+=1
        print("Dato: ",a[i],"",con,"Veces")

#Contar las veces que se repite cada dato en el vector(forma 2)Funciones se pueden utilizar
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
contados=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))
    
for i in range(len(a)):
    b=a[i] in contados
    if b==False:
        con=a.count(a[i])
        print("Dato: ",a[i],"esta ",con,"veces")
        contados.append(a[i])

#Contar las veces que se repite cada dato en el vector(forma 3)utilizando 3 vectores
#Este ejercicio es el que determina cual es el dato que mas se repite
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
contador=[]
datos_no_repetidos=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

x=0
nc=0
for i in range(cantidad_datos):
    #buscar a[i] en datos_no_repetidos
    b=0
    j=0
    while j<x and b==0:
        if a[i]==datos_no_repetidos[j]:
            b=1
        else:
            j+=1

    if b==0:
        datos_no_repetidos.append(a[i])
        x+=1
        contador.append(1)
    else:
        contador[j]+=1

dato_mas_repetido=contador[0]
posicion=0
j=1
for j in range(len(contador)):
    if contador[j]>dato_mas_repetido:
        dato_mas_repetido=contador[j]
        posicion=j

print("Dato mas repetido",datos_no_repetidos[posicion],"veces",contador[posicion])

#aqui si se utiliza "LEN" ya que no se sabe que longitud tendra este vector
for i in range(len(contador)):
    print("Dato: ",datos_no_repetidos[i],"veces",contador[i])

#Ordenar las veces que se repite de mayor a menor(Forma 1)
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
contador=[]
datos_no_repetidos=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

x=0
for i in range(cantidad_datos):
    b=0
    j=0
    while j<x and b==0:
        if a[i]==datos_no_repetidos[j]:
            b=1
        else:
            j+=1

    if b==0:
        datos_no_repetidos.append(a[i])
        x+=1
        contador.append(1)
    else:
        contador[j]+=1

for i in range(len(contador)-1):
    j=i+1
    mayor=contador[i]
    posicion=i
    while j<len(contador):
        if contador[j]>mayor:
            mayor=contador[j]
            posicion=j
        j+=1

    aux=contador[i]
    contador[i]=contador[posicion]
    contador[posicion]=aux
    #Para mantener relacion con el otro vector
    aux=datos_no_repetidos[i]
    datos_no_repetidos[i]=datos_no_repetidos[posicion]
    datos_no_repetidos[posicion]=aux

for i in range(len(contador)):
    print("Dato: ",datos_no_repetidos[i]," veces ",contador[i])

#Ordenar las veces que se repite de mayor a menor(Forma 2)(mas facil)
cantidad_datos = int(input("Cantidad de datos= "))
a = []
contador = []
datos_no_repetidos = []

for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

for i in range(cantidad_datos):
    b = 0
    j = 0
    while j < len(datos_no_repetidos) and b == 0:
        if a[i] == datos_no_repetidos[j]:
            b = 1
        else:
            j += 1

    if b == 0:
        datos_no_repetidos.append(a[i])
        contador.append(1)
    else:
        contador[j] += 1

# Ordenar los resultados según la cantidad de repeticiones
for i in range(len(contador)):
    for j in range(i + 1, len(contador)):
        if contador[j] > contador[i]:
            # Intercambiar la cantidad de repeticiones
            contador[i], contador[j] = contador[j], contador[i]
            # Intercambiar los datos no repetidos manteniendo la relación con el otro vector
            datos_no_repetidos[i], datos_no_repetidos[j] = datos_no_repetidos[j], datos_no_repetidos[i]

for i in range(len(contador)):
    print("Dato: ", datos_no_repetidos[i], " veces ", contador[i])

######Ejercicio examen
v_1=[]
cantidad_datos_1=int(input("Cantidad de datos 1= "))
print("Datos del vector 1: (lista rango)")
for i in range(cantidad_datos_1):
    v_1.append(int(input("Dato({})=".format(i))))

primo=0
si_primo=0
v_rango=[]
for i in range(cantidad_datos_1):
    c=1
    div=0
    while c<=v_1[i]:
        if v_1[i] % c==0:
            div+=1
        c+=1

    if div==2:
        si_primo+=1
        if si_primo==2:
            primo_segundo=v_1[i]
            v_rango.append(v_1[i])
            print("Segundo primo= ",v_1[i])
        elif si_primo==3:
            primo_tercero=v_1[i]
            v_rango.append(v_1[i])
            print("Tercer primo= ",v_1[i])

v_2=[]
cantidad_datos_2=primo_segundo+primo_tercero
print("Datos en vector 2: (lista datos) ")
for j in range(cantidad_datos_2):
    v_2.append(int(input("Dato({})=".format(j))))

i=0
j=0
while i< len(v_rango):
    limite_final=j+v_rango[i]-1
    promedio=0
    suma=0
    contador=0
    while j<= limite_final:
        if v_2[j] % 2==0:
            print(v_2[j],"Es par")
            suma+=v_2[j]
            contador+=1
        j+=1
            
    promedio=suma/contador        
    print("Promedio del rango del segundo primo= ",promedio)
    i+=1    
