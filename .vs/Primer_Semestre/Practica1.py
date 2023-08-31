#La cantidad de numeros mayores que 10
print("cantidad de numeros mayores que 10")
numero_limite=int(input("Cantidad de datos= "))
c=1
contador=0
while c<=numero_limite:
    num=int(input("Numero= "))
    if num>10:
        contador+=1
    c+=1
print("Cantidad de numeros mayores que 10= ",contador)        
print("fin algoritmo")
#La cantidad de numeros mayores que un numero dado
print("cantidad de numeros mayores que un numero dado")
numero_limite=int(input("cantidad de datos "))
numero_dado=int(input("Sean mayores que= "))
c=1
contador=0
while c<=numero_limite:
    num=int(input("Numero= "))
    if num>numero_dado:
        contador+=1
    c+=1
print("Cantidad de numeros mayores que el numero: ",numero_dado," Son= ",contador)  
print("Fin algoritmo")
#El promedio de los numeros que estan entre los valores 20 y 50
print("promedio de los numeros que estan entre los valores 20 y 50")
numero_limite=int(input("Cantidad de datos= "))
c=1
c2=0
contador=0
while c<=numero_limite:
    num=int(input("Numero= "))
    if num>20 and num<50:
        contador+=num
        c2+=1
    c+=1
if c2>0:
    promedio=contador/c2
    print("promedio de los numeros entre 20 y 50= ",promedio)
else:
    print("No hay numeros entre 20 y 50")    
print("Fin algoritmo")
#El promedio de los numeros que estan entre dos valores dados
print("promedio de los numeros que estan entre dos valores dados") 
numero_limite=int(input("Cantidad de datos= "))
valor1=int(input("valor 1= "))
valor2=int(input ("valor 2= "))
c=1
c2=0
contador=0
while c<=numero_limite:
    num=int(input("Numero= "))
    if valor1<num<valor2:
        contador+=num
        c2+=1
    c+=1
if c2>0:
    promedio=contador/c2
    print("promedio de los numeros entre valor 1= ",valor1," Y valor 2= ",valor2," = ",promedio)
else:
    print("No hay numeros entre valor 1= ",valor1," Y valor 2= ",valor2)
print("Fin algoritmo")              
#El promedio de los numeros pares que estan entre dos valores dados
print("promedio de los numeros pares que estan entre dos valores dados")
numero_limite=int(input("Cantidad de datos= "))
valor1=int(input("valor 1= "))
valor2=int(input ("valor 2= "))
c=1
c2=0
contador=0
while c<=numero_limite:
    num=int(input("Numero= "))
    if num%2==0:
        if valor1<num<valor2:
            contador+=num
            c2+=1
    c+=1    
if c2>0:
    promedio=contador/c2
    print("promedio de los numeros pares entre valor 1= ",valor1," Y valor 2= ",valor2," = ",promedio)
else:
    print("No hay numeros pares entre valor 1= ",valor1," Y valor 2= ",valor2)
print("Fin algoritmo")    
#Numero mayor de una cantidad de datos
print("Numeri mayor de una cantidad de datos")
numero_limite=int(input("Cantidad de datos= "))
mayor=float('-inf')
menor=float('inf')
c=1
while c<=numero_limite:
    num=int(input("Digite numero: "))
    if num>mayor:
        mayor=num
    else:
        if num<menor:
            menor=num
    c+=1
print("El mayor de los datos= ",mayor) 
print("El menor de los datos= ",menor)               