#Multiplicar el contador de pares por el contador de impares con suma
print("Multiplicar el contador de pares por el contador de impares con suma")

cantidad_numeros=int(input("Cantidad de numeros= "))
c=0
cpar=0
cimpar=0
while c<cantidad_numeros:
    numero=int(input("Numero= "))
    if numero%2==0:
        cpar+=1
    else:
        cimpar+=1
    c+=1

multiplicacion=0
cmultiplicacion=0    
if cpar>0 and cimpar>0:
    while cmultiplicacion<cimpar:
        multiplicacion+=cpar
        cmultiplicacion+=1
else:
    print("No hay pares o impares")    

print("contador de pares: ",cpar," * ","Contador de impares ",cimpar," = ",multiplicacion)

#Determinar la suma de los pares multiplos de 3,4,5. sacar menor y mayor y multiplicarlos
print("Determinar la suma de los pares multiplos de 3,4,5. sacar menor y mayor y multiplicarlos")

cantidad_numeros = int(input("Cantidad de números: "))
c = 1
ctotal = 0

while c <= cantidad_numeros:
    numero = int(input("Número: "))
    if c==1:
        menor=numero
        mayor=numero
    else:
        if numero>mayor:
            mayor=numero
        elif numero<menor:
            menor=numero        
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0:
        if numero%2==0:
            ctotal += numero
    c += 1

mult=menor*mayor

print("Suma =", ctotal)
print("Numero menor: ",menor, "*" "Numero mayor: ",mayor," = ",mult)
           
#Determinar si un numero dado es primo
print("Determinar si un numero es primo")

numer_dado=int(input("Numero= "))
c=1
div=0
while c<=numer_dado:
    if numer_dado%c==0:
        div+=1
    c+=1

if div==2:
    print("El numero es primo")
else:
    print("El numero no es primo")    

#Promedio de numeros primos
print("Pormedio de numeros primos")

cantidad_numeros=int(input("Cantidad de datos: "))
c=1
cpri=0
suma=0
while c<=cantidad_numeros:
    numero=int(input("Numero= "))
    c2=1
    div=0
    while c2<=numero:
        if numero%c2==0:
            div+=1
        c2+=1
        
    if div==2:
        suma+=numero
        cpri+=1
    c+=1        

if cpri>0:
    promedio=suma/cpri
    print("Promedio de numeros primos= ",promedio)
else:
    print("No hay numeros primos ")

#Primo mayor, primo menor, suma de numeros pares
cantidad_numeros = int(input("Cantidad de datos: "))
c = 1
sipri = 0
sumapares = 0

while c <= cantidad_numeros:
    numero = int(input("Número: "))
    if numero % 2 == 0:
        sumapares += numero

    c2 = 1
    div = 0

    while c2 <= numero:
        if numero % c2 == 0:
            div += 1
        c2 += 1

    if div == 2:
        sipri += 1

        if sipri == 1:
            menor = numero
            mayor = numero
        else:
            if numero > mayor:
                mayor = numero
            elif numero < menor:
                menor = numero

    c += 1        

print("Suma de números pares:", sumapares)
print("Primo menor:", menor)
print("Primo mayor:", mayor)

#Primo menor,mayor y averiguar si su resta es primo
print("Primo menor,mayor y averiguar si su resta es primo")

cantidad_numeros = int(input("Cantidad de datos: "))
c = 1
sipri = 0

while c <= cantidad_numeros:
    numero = int(input("Número: "))
    c2 = 1
    div = 0

    while c2 <= numero:
        if numero % c2 == 0:
            div += 1
        c2 += 1

    if div == 2:
        sipri += 1

        if sipri == 1:
            menor = numero
            mayor = numero
        else:
            if numero > mayor:
                mayor = numero
            elif numero < menor:
                menor = numero

    c += 1    

print("Primo menor:", menor)
print("Primo mayor:", mayor)

resta=mayor-menor
c2=1
div2=0
while c2<=resta:
    if resta%c2==0:
        div2+=1
    c2+=1

if div2==2:
    print("la resta", resta,"Es numero primo")
else:
    print("La resta",resta,"No es numero primo")

