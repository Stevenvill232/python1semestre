cantidadatos=int(input("Cantidad de datos= "))
cantidadpares=0
cantidadimpares=0
c=1
while c<=cantidadatos:
    numero=int(input("Digite numero: "))
    if numero%2==0:
        cantidadpares+=1
    else:
        cantidadimpares+=1
    c+=1
print("cantidad de pares ",cantidadpares)
print("Cantidad de impares ",cantidadimpares)            