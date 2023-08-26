def Taller1_punto1():
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    si_fibo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
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
        c+=1
    print("Primo mayor: ",primo_mayor,"Fibonacci menor: ",fibo_menor)
    if primo_mayor<fibo_menor:
        aux=fibo_menor
        fibo_menor=primo_mayor
        primo_mayor=aux

    suma_pares=0
    contar_pares=0
    c_3=fibo_menor+1
    print("Numeros pares entre estos dos datos: ")
    while c_3<primo_mayor:
        if c_3 % 2==0:
            print(c_3)
            suma_pares+=c_3
            contar_pares+=1
        c_3+=1

    if contar_pares>0:
        promedio=suma_pares/contar_pares
        print("Promedio de los numeros pares entre el primo mayor y el fibonacci menor: ",promedio)
    else:
        print("No hay numeros pares entre el primo mayor y el fibonacci menor")

def Taller1_punto2():
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    si_fibo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
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
        c+=1
    print("Primo mayor: ",primo_mayor,"Fibonacci menor: ",fibo_menor)
    if primo_mayor<fibo_menor:
        aux=fibo_menor
        fibo_menor=primo_mayor
        primo_mayor=aux

    suma_facrial=0
    contador_factorial=0
    c_2=fibo_menor+1
    while c_2<primo_mayor:
        if c_2 % 2!=0:
            c_1=c_2
            c_factorial=1
            while c_1>0:
                c_factorial*=c_1
                c_1-=1
            print("Numero impar: ",c_2,"Su factorial= ",c_factorial)    
            suma_facrial+=c_factorial
            contador_factorial+=1
        c_2+=1    
    if contador_factorial>0:
        promedio=suma_facrial/contador_factorial
        print("El promedio de estos factoriales= ",promedio)
    else:
        print("No hay impares entre el primo mayor y el fibonacci menor")                

def Taller1_punto3():
    cantidad=int(input("Cantida de edatos: "))
    c=1
    suma=0
    contador=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        c_1=1
        div=0
        while c_1<=numero:
            if numero%c_1==0:
                div+=1
            c_1+=1

        a=0
        b=1
        t=0
        while t<numero:
            t=a+b
            a=b
            b=t
        if numero==t and div==2:
            print(numero,"Es fibonacci y primo a la vez")
            suma+=numero
            contador+=1
        c+=1

    if c>0:
        promedio=suma/contador
        print("Promedio de estos numeros= ",promedio)
    else:
        print("No hay numeros primos y fibonaccis a la vez")            

def Taller1_punto4():
    v=[]
    cantidad=int(input("Cantidad de datos: "))
    c=1
    si_primo=0
    while c<=cantidad:
        numero=int(input("Numero: "))
        v.append(numero)
        c_2=1
        div=0
        while c_2<=numero:
            if numero%c_2==0:
                div+=1
            c_2+=1
        if div==2:
            si_primo+=1
            if si_primo==2:
                segundo_primo=numero   
        c+=1
    if si_primo>0:
        veces_segundo_pri=0    
        for i in range(len(v)):
            if v[i]==segundo_primo:
                veces_segundo_pri+=1
        print("Segundo ptimo encontrado: ",segundo_primo,"Veces que se repite: ",veces_segundo_pri)         
    else:
        print("No se encontro el segundo primo en la cantidad de numeros")           
def Taller1_punto5():
    cantidad = int(input("Cantidad de ternas: "))
    contador_equilateros = 0
    contador_isosceles = 0
    contador_escalenos = 0
    suma_isosceles = 0
    
    for _ in range(cantidad):
        terna = [int(input(f"Lado {i+1}: ")) for i in range(3)]
        
        lados_iguales = len(set(terna))
        
        if lados_iguales == 1:
            contador_equilateros += 1
        elif lados_iguales == 2:
            contador_isosceles += 1
            suma_isosceles += sum(terna)
        else:
            contador_escalenos += 1
    
    print("Cantidad de triángulos equiláteros:", contador_equilateros)
    print("Cantidad de triángulos isósceles:", contador_isosceles)
    print("Cantidad de triángulos escalenos:", contador_escalenos)
    print("Suma de los triángulos isósceles:", suma_isosceles)

#Taller1_punto1()
#Taller1_punto2()
#Taller1_punto3()
#Taller1_punto4()
#Taller1_punto5()
