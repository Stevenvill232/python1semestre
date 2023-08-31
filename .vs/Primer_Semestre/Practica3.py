#Generar la serie de fibonacci

print("Generar la serie de fibonacci")

numero_dado=int(input("cantidad de fibonaccis= "))
a=0
b=1
print(a)
print(b)
t=0
c=3
while c<=numero_dado:
    t=a+b
    print(t)
    a=b
    b=t
    c+=1

print("Fin algoritmo")
#Determinar si un numero dado pertenece a la serie de fibonacci

print("Determinar si un numero dado pertenece a la serie de fibonacci")

numero_dado=int(input("numero= "))
a=0
b=1
t=0
while t<numero_dado:
    t=a+b
    a=b
    b=t

if numero_dado==t:
    print("El numero",numero_dado,"Pertenece a la serie fibonacci")
else:
    print("El numero",numero_dado,"No pertenece a la serie fibonacci") 

print("Fin algoritmo")     

#Determinar el fibonacci mayor y menor de una cantidad de numeros

print("Determinar el fibonacci mayor y menor de una cantidad de numeros")

cantidad_numeros=int(input("Cantidad de numeros= "))
c=1
sifibo=0
while c<=cantidad_numeros:
    numero=int(input("numero= "))
    t=0
    a=0
    b=1
    while t<numero:
        t=a+b
        a=b
        b=t

        if numero==t:
            sifibo+=1

            if sifibo==1:
                menor=numero
                mayor=numero
            else:
                if numero>mayor:
                    mayor=numero
                elif numero<menor:
                    menor=numero
    c+=1

print("Fibonacci menor= ",menor)
print("Fibonacci mayor= ",mayor)   
print("Fin algoritmo")

#Determinar el promedio de los fibonaccis de una cantidad de numeros
print("Determinar el promedio de los fibonaccis de una cantidad de numeros")

cantidad_numeros=int(input("Cantidad de numeros= "))
c=1
suma=0
contador=0
while c<=cantidad_numeros:
    numero=int(input("numero= "))
    t=0
    a=0
    b=1
    while t<numero:
        t=a+b
        a=b
        b=t

        if numero==t:
            suma+=numero
            contador+=1
    c+=1

if contador>0:
    promedio=suma/contador
    print("Promedio de fibonaccis hallados= ",promedio)
else:
    print("No hay fibonaccis")

print("Fin algoritmo")

#Determinar si la diferencia del primo mayor con el fibonacci menor es un numero fibonacci

print("#Determinar si la diferencia del primo mayor con el fibonacci menor es un numero fibonacci")

cantidad_datos = int(input("Cantidad de datos: "))
c = 1
siprimo = 0
sifibo = 0

while c <= cantidad_datos:
    numero = int(input("Número: "))
    c2 = 1
    divisores = 0

    while c2 <= numero:
        if numero % c2 == 0:
            divisores += 1
        c2 += 1

    if divisores == 2:
        siprimo += 1

        if siprimo == 1:
            primo_mayor = numero
        else:
            if numero > primo_mayor:
                primo_mayor = numero

    a = 0
    b = 1
    t = 0

    while t < numero:
        t = a + b
        a = b
        b = t

        if numero == t:
            sifibo += 1

            if sifibo == 1:
                fibo_menor = numero
            else:
                if numero < fibo_menor:
                    fibo_menor = numero

    c += 1

print("Fibonacci menor: ",fibo_menor)
print("Primo mayor: ",primo_mayor)

if primo_mayor<fibo_menor:
    aux=fibo_menor
    fibo_menor=primo_mayor
    primo_mayor=aux

c3=fibo_menor+1
diferencia=0
while c3<=primo_mayor:
    diferencia+=1
    c3+=1

print("Diferencia= ",diferencia)

a=0
b=1
t=0
while t<diferencia:
    t=a+b
    a=b
    b=t

if diferencia==t:
    print("Es fibonacci ")  
else:
    print("No es fibonacci")

print("Fin algoritmo")    