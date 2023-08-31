#Ejercicio 1 centinela Taller 2
print("Ejercicio 1 Centinela Taller 2")
numero=int(input("Numero: "))
sipri=0
contador_primo=0
sumador_primo=0
sifibo=0
while numero>=0:
    c1=1
    div=0
    while c1<=numero:
        if numero%c1==0:
            div+=1
        c1+=1

    if div==2:
        print("Primo: ",numero)
        contador_primo+=1
        sumador_primo+=numero
        sipri+=1
        if sipri==1:
            primo_menor=numero
            primo_mayor=numero
        else:
            if numero<primo_menor:
                primo_menor=numero
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
        print("Fibonacci: ",numero)
        sifibo+=1
        if sifibo==1:
            fibo_menor=numero
        elif numero<fibo_menor:
            fibo_menor=numero

    numero=int(input("Numero: "))                            

if contador_primo>0:
    print("Primo mayor= ",primo_mayor," Primo menor= ",primo_menor)
    promedio_primos=sumador_primo/contador_primo
    print("Promedio de los numeros primos= ",promedio_primos)
else:
    print("No hay primos")
    
if sifibo>0:
    print("Fibonacci menor= ",fibo_menor)
    numero_factorial=fibo_menor
    factorial=1
    while numero_factorial>=1:
        factorial=factorial*numero_factorial
        numero_factorial-=1

    print("Factorial del fibonacci menor= ",factorial)
else:
    print("No hay fibonaccis")

print("Fin algoritmo")
#Ejercicio 2 centinela Taller 2
print("Ejercicio 2 centinela Taller 2")
respuesta=input("Desea procesar triangulo (si/no):")
perimetro_equilatero=0
contador_equilateros=0
contador_isosceles=0
perimetro_escaleno=0
contador_escalenos=0
while respuesta.lower()=="si":
    lado1=int(input("Lado 1= "))
    lado2=int(input("Lado 2= "))
    lado3=int(input("Lado 3= "))
    if lado1>0 and lado2>0 and lado3>0:
        if lado1==lado2:
            if lado2==lado3:
                print("Triangulo equilatero")
                perimetro_equilatero=lado1*3
                print("Su Perimetro=",perimetro_equilatero)
                contador_equilateros+=1
            else:
                print("Triangulo isosceles")
                contador_isosceles+=1
        else:
            if lado1==lado3:
                print("Triangulo isosceles")
                contador_isosceles+=1
            else:
                if lado2==lado3:
                    print("Triangulo isosceles")
                    contador_isosceles+=1
                else:
                    print("Triangulo escaleno")
                    perimetro_escaleno= lado1+lado2+lado3
                    print("Su perimetro= ",perimetro_escaleno)
                    contador_escalenos+=1                               
    else:
        print("Triangulo no valido")

    respuesta=input("Desea procesar mas triangulos (si/no):")

if contador_isosceles>0:
    c1=1
    div=0
    while c1<=contador_isosceles:
        if contador_isosceles%c1==0:
           div+=1
        c1+=1

    if div==2:
       print("El contador de triangulos isosceles=",contador_isosceles,"El cual es primo")
    else:
       print("El contador de triangulos isosceles=",contador_isosceles,"El cual no es primo")    
else:
    print("No hay triangulos isosceles")

if contador_equilateros>0:
    promedio_equilatero=perimetro_equilatero/contador_equilateros
    print("Promedio del perimetro de los triangulos equilateros= ",promedio_equilatero)
else:
    print("No hay triangulos equilateros")

if contador_equilateros>0:
    print("Contador de triangulos equilateros= ",contador_equilateros)
    factorial=1
    while contador_equilateros>=1:
        factorial=factorial*contador_equilateros
        contador_equilateros-=1

    print("Su factorial es= ",factorial)    
else:
    print("No hay triangulos equilateros")

promedio_escalenos=0
if contador_escalenos>0:
    promedio_escalenos=perimetro_escaleno/contador_escalenos
    print("Promedio del perimetro de los triangulos escalenos= ",promedio_escalenos)
else:
    print("No hay triangulos escalenos")

if promedio_equilatero>promedio_escalenos:
    print("El promedio del perimetro de los equilateros es mayor")
elif promedio_equilatero==promedio_escalenos:
    print("Los promedios de los perimetros son iguales")
else:
    print("El promedio del perimetro de los escalenos es mayor")

print("Fin algoritmo")
#Ejercicio 3 Rompimiento de control taller 2
print("Ejercicio 3 Rompimiento de control taller 2")
numero=int(input("Numero: "))
suma_contador_pares=0
si_fibonacci=0
suma_contadores_fibonaccis=0
si_primo=0
suma_contador_primos=0
c_0=0
while numero!=-5:
    aux=numero
    suma_numeros=0
    contador_grupo=0
    while numero==aux:
        suma_numeros+=numero
        contador_grupo+=1
        numero=int(input("Numero: "))

    c_0+=1
    promedio=suma_numeros/contador_grupo    
    print("Grupo de numeros: ",aux," Su contador= ",contador_grupo,"Promedio de datos= ",promedio)

    if contador_grupo % 2==0:
        print("Su contador es numero par y su suma es= ",suma_numeros)
        suma_contador_pares+=contador_grupo

    a=0
    b=1
    t=0
    while t<contador_grupo:
        t=a+b
        a=b
        b=t

    if contador_grupo==t:
        print("Su contador es numero fibonacci")
        suma_contadores_fibonaccis+=contador_grupo
        si_fibonacci+=1

    c=1
    div=0
    while c<=contador_grupo:
        if contador_grupo % c==0:
            div+=1
        c+=1

    if div==2:
        print("Su contador es numero primo")
        suma_contador_primos+=contador_grupo
        si_primo+=1

    if c_0==1:
        grupo_mayor=contador_grupo
        representante_Gmayor=aux
        grupo_menor=contador_grupo
        representante_Gmenor=aux
    else:
        if contador_grupo>grupo_mayor:
            grupo_mayor=contador_grupo
            representante_Gmayor=aux
        elif contador_grupo<grupo_menor:
            grupo_menor=contador_grupo
            representante_Gmenor=aux

if si_fibonacci>0:
    promedio_fibonaccis=suma_contadores_fibonaccis/si_fibonacci
    print("Promedio de los contadores que fueron numeros fibonaccis= ",promedio_fibonaccis)
else:
    print("No hubo contadores fibonaccis")

if si_primo>0:
    promedio_primos=suma_contador_primos/si_primo
    print("Promedio de los contadores que fueron numeros primos= ",promedio_primos)
else:
    print("No hubo contadores primos")

if contador_grupo>0:
    print("Grupo que mas se reptio: ",representante_Gmayor," Con ",grupo_mayor," Veces")
    c_2=1
    div_2=0
    while c_2<=grupo_menor:
        if grupo_menor % c_2==0:
            div_2+=1
        c_2+=1

    if div_2==2:
        print("Grupo que menos se repitio: ",representante_Gmenor," Con: ",grupo_menor," Veces y su contador es numero primo")
    else:
        print("Grupo que menos se repitio: ",representante_Gmenor," Con: ",grupo_menor," Veces y su contador No es numero primo")            
else:
    print("No hubieron grupos de numeros")

print("Fin algoritmo")