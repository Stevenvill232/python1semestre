def leer_vector():
    cantidad=int(input("Cantidad de datos en el vector 1: "))
    vecotr_1=[]
    print("Datos en el vector: ")
    for i in range(cantidad):
        vecotr_1.append(int(input("Dato({})= ".format(i))))

    return vecotr_1

def primo(num):
    b=0
    c=2
    while c<num and b==0:
        if num % c==0:
            b=1
        c+=1
    if b==0:
        return True
    else:
        return False

def par(num):
    if num % 2==0:
        return True
    else:
        return False    

a=leer_vector() #vector 1
b=leer_vector() #vector 2          

cantidad_pares=0
for i in range (len(a)):
    if par(a[i]):
        cantidad_pares+=1

print("La cantidad de pares del primer vector es: ",cantidad_pares)  
print("No primos del segundo vector: ")      
for j in range (len(b)):
    if not primo(b[j]):
        print(b[j])
        b[j]=cantidad_pares

print("Vector resultante con los primos reemplazados por la cantidad de pares: ",b)