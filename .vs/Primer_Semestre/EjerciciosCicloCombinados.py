#sumar los numeros desde el 0 hasta un numero dado
numero_dado=int(input("numero limite = "))
c=1
suma=0
while c<=numero_dado:
    suma+=c
    c+=1
print ("Suma= ",suma)

#Sumar los numeros pares hasta un numero dado
numero_dado=int(input("numero limite para sumar pares= "))
c=1
suma=0
while c<=numero_dado:
    if c%2==0:
        suma+=c
    c+=1
if suma>0:
    print("Suma de pares= ",suma)
else:
    print("No hay pares")                    
