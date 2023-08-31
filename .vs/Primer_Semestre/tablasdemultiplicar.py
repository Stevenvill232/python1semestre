c = 1
while c <= 10:
    c2 = 1
    while c2 <= 10:
        multiplicacion = c * c2
        print(c, "*", c2, "=", multiplicacion)
        c2 += 1
    c += 1   

#Tabla de multiplicar de un numero dado
print("Tabla de multiplicar de un numero dado")
numero_dado=int(input("Tabla de multiplicar del numero= "))
c=numero_dado
multiplicacion=0
c2=1
while c<=numero_dado:
    while c2<=10:
        multiplicacion=c*c2
        print(c,"*",c2,"=",multiplicacion)
        c2+=1
    c+=1   