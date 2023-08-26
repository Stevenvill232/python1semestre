####Punto 1 Parcial 1
cantidad_datos=int(input("Cantidad de datos: "))
c=1
si_primo=0
si_fibo=0
si_par=0
while c<=cantidad_datos:
    numero=int(input("Numero: "))
    c_1=1
    div=0
    while c_1<=numero:
        if numero%c_1==0:
            div+=1
        c_1+=1

    if div==2:
        si_primo+=1
        if si_primo==1:
            primo_mayor=numero
        elif numero>primo_mayor:
            primo_mayor=numero

    a=0
    b=1
    t=0
    while t<numero:
        t=a+b
        a=b
        b=t

    if numero==t:
        si_fibo+=1
        if si_fibo==1:
            fibo_menor=numero
        elif numero<fibo_menor:
            fibo_menor=numero

    if numero%2==0:
        si_par+=1
        if si_par==1:
            par_menor=numero
        elif numero<par_menor:
            par_menor=numero
    c+=1

print("Primo mayor= ",primo_mayor," Fibonacci menor: ",fibo_menor," Par menor: ",par_menor)
multiplicacion_1=fibo_menor
c_3=1
while c_3<primo_mayor:
    multiplicacion_1+=fibo_menor
    c_3+=1

multiplicacion_2=par_menor
c_3=1
while c_3<multiplicacion_1:
    multiplicacion_2+=par_menor
    c_3+=1

print("La multiplicacion entre estos 3= ",multiplicacion_2)
####Punto 2 parcial 1
cantidad_datos = int(input("Cantidad de datos = "))
c = 1
si_fibo = 0
c_fibos = 0
segundo_fibonacci = 0

while c <= cantidad_datos:
    numero = int(input("Numero: "))
    a = 0
    b = 1
    t = 0
    
    while t < numero:
        t = a + b
        a = b
        b = t

    if numero == t:
        si_fibo += 1
        if si_fibo == 2:
            segundo_fibonacci = numero
            c_fibos = 1
        elif numero == segundo_fibonacci:
            c_fibos += 1
    c += 1

print("Segundo fibonacci:", segundo_fibonacci, "Contador de numeros iguales a este:", c_fibos)

c = 1
div = 0

while c <= c_fibos:
    if c_fibos % c == 0:
        div += 1
    c += 1

if div == 2:
    print("Esta contador de datos es un número primo")
else:
    print("Esta contador de datos no es un número primo")

#####Punto 3 parcial 1
Cantidad_datos=int(input("Cantidad de ternas o triangulos: "))
perimetro_equilatero = 0
contador_equilateros = 0
contador_isosceles = 0
contador_escalenos = 0
c=1
c_equilateros=1
while c<=Cantidad_datos:
    lado1 = int(input("Lado 1= "))
    lado2 = int(input("Lado 2= "))
    lado3 = int(input("Lado 3= "))
    
    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        perimetro_equilatero_contado=0
        if lado1 == lado2 == lado3:
            print("Triangulo equilatero")
            perimetro_equilatero+= lado1 * 3
            perimetro_equilatero_contado=lado1*3
            print("Perimetro del triangulo",c_equilateros," = ",perimetro_equilatero_contado)
            c_equilateros+=1
            contador_equilateros += 1
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Triangulo isosceles")
            contador_isosceles += 1
        else:
            print("Triangulo escaleno")
            contador_escalenos += 1
    else:
        print("Triangulo no valido")

    c+=1

print("Cantidad de triangulos equilateros:", contador_equilateros)
print("Cantidad de triangulos isosceles:", contador_isosceles)
print("Cantidad de triangulos escalenos:", contador_escalenos)
a=0
b=1
t=0
while t<perimetro_equilatero:
    t=a+b
    a=b
    b=t

if perimetro_equilatero==t:
    print("Suma de los perimetros equilateros:", perimetro_equilatero," Esta suma es numero fibonacci")
else:
    print("Suma de los perimetros equilateros:", perimetro_equilatero," Esta suma No es numero fibonacci") 

#####Punto 4 parcial 1
cantidad_datos=int(input("Cantidad de datos: "))
c=1
si_fibo=0
while c<=cantidad_datos:
    numero=int(input("Numero: "))
    a=0
    b=1
    t=0
    while t<numero:
        t=a+b
        a=b
        b=t

    if numero==t:
        si_fibo+=1
        if si_fibo==1:
            primer_fibo=numero
        elif si_fibo==2:
            segundo_fibo=numero
        elif si_fibo==3:
            tercer_fibo=numero 
    c+=1

print("Primer fibonacci: ",primer_fibo," Segundo fibonacci: ",segundo_fibo," Tercer fibonaccii: ",tercer_fibo)
if primer_fibo>segundo_fibo and primer_fibo>tercer_fibo:
    fibo_mayor=primer_fibo
elif segundo_fibo>primer_fibo and segundo_fibo>tercer_fibo:
    fibo_mayor=segundo_fibo
elif tercer_fibo>primer_fibo and tercer_fibo>segundo_fibo:
    fibo_mayor=tercer_fibo

if primer_fibo<segundo_fibo and primer_fibo<tercer_fibo:
    fibo_menor=primer_fibo
elif segundo_fibo<primer_fibo and segundo_fibo<tercer_fibo:
    fibo_menor=segundo_fibo
elif tercer_fibo<primer_fibo and tercer_fibo<segundo_fibo:
    fibo_menor=tercer_fibo

print("Fibonacci mayor: ",fibo_mayor," Fibonacci menor: ",fibo_menor)
print("Numeros pares entre estos (Sin tomar los respectivos fibonaccis)")
c=fibo_menor+1
suma_pares=0
c_pares=0
while c<fibo_mayor:
    if c%2==0:
        print(c)
        suma_pares+=c
        c_pares+=1
    c+=1    

if c_pares>0:
    promedio_pares=suma_pares/c_pares
    print("El promedio de estos numeros pares es= ",promedio_pares)
else:
    print("No hay numeros pares entre estos dos fibonaccis") 