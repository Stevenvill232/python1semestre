cantidad_numeros = int(input("Digite la cantidad de números: "))
c = 1
c5 = 0
c3 = 0
suma_5 = 0
suma_3 = 0

while c <= cantidad_numeros:
    numero = int(input("Digite un número: "))
    
    if numero % 5 == 0:
        suma_5 += numero
        c5 += 1
        
    if numero % 3 == 0:
        suma_3 += numero
        c3 += 1
        
    c += 1

if c5 > 0:
    promedio_5 = suma_5 / c5
    print("El promedio de los múltiplos de 5 es:", promedio_5)
else:
    print("No hay múltiplos de 5")

if c3 > 0:
    promedio_3 = suma_3 / c3
    print("El promedio de los múltiplos de 3 es:", promedio_3)
else:
    print("No hay múltiplos de 3")

if promedio_5 > promedio_3:
    print("El promedio de los múltiplos de 5 es mayor que el promedio de los múltiplos de 3")
elif promedio_5 < promedio_3:
    print("El promedio de los múltiplos de 3 es mayor que el promedio de los múltiplos de 5")
else:
    print("El promedio de los múltiplos de 5 es igual al promedio de los múltiplos de 3")

