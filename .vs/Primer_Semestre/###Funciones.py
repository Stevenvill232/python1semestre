#####Llenar una lista con datos repetidos, formar una nueva sin datos repetidos y ordenar de forma ascendente y descendente
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
l2=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

#Recorrer lista 1 y por cada dato llenarlo en l2 si no esta
for i in range(len(l1)):
    dato= l1[i] in l2
    if dato==False:
        l2.append(l1[i])

print("Lista sin repetidos:",l2)
l2.sort()
print("Lista anterior ordenada ascendentemente:",l2)
l2.sort(reverse=True)
print("Lista anterior ordenada descendentemente:",l2)


##### Otra forma de hacerlo
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
l2=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

#Creamos una nueva lista con estas dos funciones
l2=list(set(l1))
print("Lista sin repetidos:",l2)
l2.sort()
print("Lista anterior ordenada ascendentemente:",l2)
l2.sort(reverse=True)
print("Lista anterior ordenada descendentemente:",l2)


#####Contar las veces que se repiten los numeros de un vector
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
l2=[] #Esta lista va a contar las veces que se van contando
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

for i in range(len(l1)):
    dato= l1[i] in l2
    if dato==False:
        c= l1.count(l1[i]) #Se cuenta las veces que aparecen los datos 

    print("dato:",l1[i],"Esta:",c,"veces")
    l2.append(l1[i])


#####Eliminar los numeros pares de la lista
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

i=0
while i<len(l1):
    if l1[i] % 2==0:
        l1.remove(l1[i]) #Tambien se puede usar   del(l1[i])
    else:
        i+=1       

print("Lista resultane:",l1)


#####Insertar un numero en donde le corresponda
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})=".format(i))))

dato=int(input("Dato a insertar:"))
i=0
while i<len(l1):
    if dato>l1[i]:
        i+=1
    else:
        break
    #La posicion donde se inserta el valor sera en I es hasta donde llego ell bucle
    # brak hace que termine el bucle hasta donde uno le diga

l1.insert(i,dato)
print("Lista:",l1) 


#####LLenar los datos en una lista de tal forma que al entrar vayan quedando ordenados (ordenamiento POR INSERCION)
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
i=1
while i<=cantidad_datos:
    dato=int(input("Digitar dato="))
    #buscamos posicion en la lista
    j=0
    while j<len(l1):
        if dato>l1[j]:
            j+=1
        else:
            break

    l1.insert(j,dato)
    i+=1

print("Lista ordenada:",l1)


####Buscar un dato en la lista y su posicion
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})".format(i))))

dato=int(input("Dato a buscar= "))
b= dato in l1   #Aseguramos si el dato esta en la lista
if b==True:
    i=l1.index(dato)
    print(l1)
    print(dato,"Se encuentra en la posicion",i,"de la lista")
else:
    print(l1)
    print(dato,"No se encuentra en la lista")


#####Se tiene una lista, determinar cual dato se repite mas
cantidad_datos=int(input("Cantidad de datos= "))
l1=[]
contados=[]
for i in range(cantidad_datos):
    l1.append(int(input("Dato({})".format(i))))

b1=0
for i in range(len(l1)):
    b= l1[i] in contados
    if b==False:
        c = l1.count(l1[i])
        if b1==0:
            mayor=c
            dato_mayor=l1[i]
            b1=1
        else:
            if c>mayor:
                mayor=c
                dato_mayor=l1[i]
        #determinamos l1 como contado
        contados.append(l1[i])

print("Dato que mas se repite= ",dato_mayor,"con",mayor,"veces")

#######Se tienen dos vectores, llenar los numeros pares no comunes sin repetir en un tercer vector
l1=[]
l2=[]
l3=[]
cantidad_datos_l1=int(input("Cantidad de datos en lista 1:"))
print("Ingrese los datos de la lista 1:")
for i in range(cantidad_datos_l1):
    l1.append(int(input("Dato({})=".format(i))))

cantidad_datos_l2=int(input("Cantidad de datos en lista 2:"))
print("Ingrese los datos de la lista 1:")
for j in range(cantidad_datos_l2):
    l2.append(int(input("Dato({})=".format(i))))

for i in range(len(l1)):
    if l1[i] % 2==0:
        dato1= l1[i] in l2
        if dato1==False:
            dato_agregar_1= l1[i] in l3
            if dato_agregar_1==False:
                l3.append(l1[i])

for j in range(len(l2)):
    if l2[j] % 2==0:
        dato2= l2[j] in l1
        if dato2==False:
            dato_agregar_2= l2[j] in l3
            if dato_agregar_2==False:
                l3.append(l2[j])

print("Lista 3 con pares no comunes si repetir: ",l3)

#######Generar 10 numeros pares aleatorios entre 0 y 100
import random
list2=[]
for _ in range(10):
    numero= random.randrange(0,100,2)
    list2.append(numero)

print(list2)

#######Generar una cantidad de numeros aleatorios multiplos de 5
import random
list2=[]
cantidad_datos=int(input("Cantidad de datos a generar:"))
for _ in range(cantidad_datos):
    numero= random.randrange(0,100,5)
    list2.append(numero)   #tambien se puede hacer asi: list2.append(random.randrange(0,100,5))

print(list2)

###### Generar los numeros del 1 hasta un numero dado, de forma desordenada
import random
list2=[]
cantidad_datos=int(input("Hasta que numero generar la lista:"))
i=0
for i in range(i+1,cantidad_datos+1):
    list2.append(i)

random.shuffle(list2)
print(list2)

##### Se tienen 2 listas con numeros aleatorios, formar una lista con la  union de las dos por estension
import random
list1=[]
lista2=[]
cantidad_datos1=int(input("Cantidad de datos en lista 1= "))
cantidad_datos2=int(input("Cantidad de datos en lista 2= "))
v1=int(input("Valor entero limite aleatorio= "))
for _ in range(cantidad_datos1):
    list1.append(random.randint(0,v1))

for _ in range(cantidad_datos2):
    lista2.append(random.randint(0,v1))

print("Lista 1=",list1)
print("Lista 2=",lista2)

#### funcion para que nos diga la posicion de cada elemento
tienda=['agua','huevos','aceite','sal']
for i,producto in  enumerate(tienda):
    print(i,producto)

#### para relacionar dos listas
tienda=['agua','aceite','arroz','sal']
mineral=['mineral natural','de oliva virgen','basmati']
for producto,mine in  zip(tienda,mineral):
    print(producto,mine)    