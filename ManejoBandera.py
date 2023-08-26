#Determinar el primo menor con bandera
print("Determinar el primo menor de una cantidad de datos")
cantidad_datos=int(input("Cantidad dee datos: "))
c=1
b=0
while c<=cantidad_datos:
    c+=1;
    numero=int(input("Numero: "))
    c2=1
    div=0
    while c2<=numero:
        if numero%c2==0:
            div+=1
        c2+=1         
    if div==2:
        if b==0:
            Menor=numero
            b=1
        else:
            if numero<Menor:
                Menor=numero

print("Primo menor= ",Menor)  

#Determinar si un numero dado es primo con bandera
print("Determinar si un numero es primo")
numero=int(input("Numero= "))
c=2
b=0
while c<numero and b==0:
    if numero%2==0:
        b=1
    c+=1

if b==0:
    print("Es primo")
else:
    print("No es primo")

#Generar una serie de numeros
print("Sereie de numeros")
cantidad_numeros=int(input("Cantidad de datos= "))
c=1
b=0
sumador=4
print(sumador)
while c<=cantidad_numeros:
    if b==0:
        sumador+=5
        print(sumador)
        b=1
    else:
        sumador-=2
        print(sumador)
        b=0
    c+=1

#Determinar si un numero dado pertenece a la anterior serie
numero_buscar=int(input("Numero a buscar de la anterior serie: "))
c=1
b=0
b2=0
sumador=4
while c<numero_buscar and b2==0:
    if b==0:
        sumador+=5
        if sumador==numero_buscar:
            b2=1
        b=1
    else:
        sumador-=2
        if sumador==numero_buscar:
            b2=1
        b=0
    c+=1

if b2==1 or numero_buscar==4:
    print("El numero",numero_buscar,"pertenece a la serie")
else:
    print("El numero",numero_buscar,"no pertenece a la serie")

