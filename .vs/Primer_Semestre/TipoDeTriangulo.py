respuesta = input("Desea procesar triangulo (si/no)")
perimetro_equilatero = 0
contador_equilateros = 0
contador_isosceles = 0
perimetro_escaleno = 0
contador_escalenos = 0

while respuesta.lower() == "si":
    lado1 = int(input("Lado 1= "))
    lado2 = int(input("Lado 2= "))
    lado3 = int(input("Lado 3= "))
    
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if lado1 == lado2 == lado3:
            print("Triangulo equilatero")
            perimetro_equilatero = lado1 * 3
            contador_equilateros += 1
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triangulo isosceles")
            contador_isosceles += 1
        else:
            print("Triangulo escaleno")
            perimetro_escaleno = lado1 + lado2 + lado3
            contador_escalenos += 1
    else:
        print("Triangulo no valido")

    respuesta = input("Desea procesar mas triangulos (si/no)")

print("Cantidad de triangulos equilateros:", contador_equilateros)
print("Cantidad de triangulos isosceles:", contador_isosceles)
print("Cantidad de triangulos escalenos:", contador_escalenos)
print("Perimetro total de triangulos equilateros:", perimetro_equilatero)
print("Perimetro total de triangulos escalenos:", perimetro_escaleno)




