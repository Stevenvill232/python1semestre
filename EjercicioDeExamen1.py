#Cantidad de primos y multiplos de 3 y hallar las tablas de multiplicar de numeros pares entre estos 2

cantidad_numeros=int(input("Cantidad de datos= "))
c=1
contador3=0
contadorpri=0
while c<=cantidad_numeros:
    numero=int(input("Numero= "))
    if numero%3==0:
        contador3+=1

    c2=1
    div=0
    while c2<=numero:
        if numero%c2==0:
            div+=1
        c2+=1
    if div==2:
        contadorpri+=1
    c+=1

print("Cantidad de primos= ",contadorpri)
print("Contidad de multiplos de 3= ",contador3)

if contadorpri<contador3:
    aux=contador3
    contador3=contadorpri
    contadorpri=aux

c2=contador3
sipar=0
while c2<=contadorpri:
    if c2%2==0:
        ctabla=1
        while ctabla<=10:
            tabla=c2*ctabla
            print(c2,"*",ctabla,"=",tabla)
            ctabla+=1
    c2+=1
