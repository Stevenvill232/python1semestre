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

#Otra forma
numero_dado = int(input("Número: "))
div = 0

for c in range(1, numero_dado + 1):
    if numero_dado % c == 0:
        div += 1

if div == 2:
    print("El número es primo")
else:
    print("El número no es primo")

#otra forma
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")
     