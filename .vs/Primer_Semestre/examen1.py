#Se tiene una cantidad de números dada, determinar el primo mayor, el Fibonacci menor, el par menor y realizar la multiplicación de ellos con sumas.25%
cantidad_datos=int(input("Cantidad de datos= "))
c=1
sipri=0
sifibo=0
sipar=0
primo_mayor=0
fibo_menor=0
par_menor=0
while c<=cantidad_datos:
    c+=1;
    numero=int(input("Numero= "))

    if numero%2==0:
        sipar+=1

        if sipar==1:
            par_menor=numero
        else:
            if numero<par_menor:
                par_menor=numero

    c2=1
    div=0
    while c2<=numero:
        if numero%c2==0:
            div+=1
        c2+=1

    if div==2:
        sipri+=1

        if sipri==2:
            primo_mayor=numero
        else:
            if numero>primo_mayor:
                primo_mayor=numero

    t=0
    a=0
    b=1
    while t<numero:
        t=a+b
        a=b
        b=t

    if numero==t:
        sifibo+=1

        if sifibo==1:
            fibo_menor=numero
        else:
            if numero<fibo_menor:
                fibo_menor=numero

print("Par menor= ",par_menor)
print("Primo mayor= ",primo_mayor)
print("Fibonacci menor= ",fibo_menor)

c3=0
multiplicacion1=0
while c3<primo_mayor:
    multiplicacion1+=par_menor
    c3+=1

print(multiplicacion1)
c4=0
multiplicacion_total=0
while c4<multiplicacion1:
    multiplicacion_total+=fibo_menor
    c4+=1

print("Multiplicacion total= ",multiplicacion_total)
#Se tiene una cantidad de números dada donde hay varios números que se repiten. Encontrar el número de veces que se repite el segundo Fibonacci (en orden de entrada) y determinar si este contador es un número primo
cantidad_datos = int(input("Cantidad de datos: "))
c = 1
c2 = 0
sifibo = 0
numero_2 = 0

while c <= cantidad_datos:
    c += 1
    numero = int(input("Número: "))
    a = 0
    b = 1
    t = 0

    while t < numero:
        t = a + b
        a = b
        b = t

        if numero == t:
            sifibo += 1

            if sifibo == 2:
                c2 += 1
                numero_2 = numero
            else:
                if numero == numero_2:
                    c2 += 1

print("Segundo fibonacci:", numero_2, "Contador:", c2)
c3 = 1
div = 0

if c2 > 0:
    while c3 <= c2:
        if c2 % c3 == 0:
            div += 1
        c3 += 1

    if div == 2:
        print("El contador del segundo fibonacci:", c2, "es primo")
    else:
        print("El contador del segundo fibonacci:", c2, "no es primo")
else:
    print("No hay fibonacci")
#Se tiene una cantidad de ternas,decir si es triangulo equilatero,escaleno o isosceles, y saber si el perimetro de los equilateros es fibonacci
cantidad_ternas = int(input("Cantidad de ternas: "))
c = 1
perimetro = 0
contador_equilatero = 0
contador_isosceles = 0
contador_escaleno = 0

while c <= cantidad_ternas:
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))

    if lado1 == lado2 and lado1 == lado3:
        perimetro += (lado1+lado2+lado3)
        contador_equilatero += 1
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        contador_isosceles += 1
    else:
        contador_escaleno += 1

    c += 1

print("Hay", contador_equilatero, "triángulos equiláteros")
print("Hay", contador_escaleno, "triángulos escalenos")
print("Hay", contador_isosceles, "triángulos isósceles")

a = 0
b = 1
t = 0

while t < perimetro:
    t = a + b
    a = b
    b = t

if perimetro == t:
    print("El perímetro de los triángulos equiláteros =", perimetro, "es un número de Fibonacci")
else:
    print("El perímetro de los triángulos equiláteros =", perimetro, "no es un número de Fibonacci")
