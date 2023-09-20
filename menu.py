def leermatriz(mat, f, c):
    for i in range(f):
        a = []
        for j in range(c):
            a.append(int(input("Ingrese el dato: ")))
        mat.append(a)

def isprime(n):
    m = 0
    for x in range(1, n+1):
        if n % x == 0:
            m += 1
    if m == 2:
        return True
    else:
        return False


def isconsec(n1, n2):
    b = 0
    for i in range(n1, n2):
        if isprime(i):
            b = 1
    if b == 1:
        print("los primos son consecutivos")
    else:
        print("no son consecutivos")


def esfib(n):
    a = 0
    b = 1
    s = 0
    while s < n:
        s = a+b
        a = b
        b = s
    if s == n:
        return True
    else:
        return False


def merge_sort(arr):
    if len(arr) > 1:
        leftarr = arr[:len(arr)//2]
        rightarr = arr[len(arr)//2:]

        merge_sort(leftarr)
        merge_sort(rightarr)

        i = 0
        j = 0
        k = 0

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1

        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1

##EJERCICIO DE SUSTENTACION
def Sustentacions_ejercicio3():
    matriz=[]
    filas=int(input("Numero de filas"))
    columnas=int(input("Numero de columnas"))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)
    print("Matriz original:")    
    for fila in matriz:
        print(fila)

    si_primo=0
    for i in range(filas):
        for j in range(columnas):
            if i+j==columnas-1:
                c=1
                div=0
                while c<= matriz[i][j]:
                    if matriz[i][j] % c==0:
                        div+=1
                    c+=1
                if div==2:
                    si_primo+=1
                    if si_primo==1:
                        primo_menor=matriz[i][j]
                    elif matriz[i][j]<primo_menor:
                        primo_menor=matriz[i][j]

    if si_primo>0:
        print("El primo menor de la diagonal secundaria es: ",primo_menor)
    else:
        print("No hay primos en la diagonal secundaria")

#####
def leer_matriz():
    matriz=[]
    filas=int(input("Filas: "))
    columnas=int(input("Columnas: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)    

    for fila in matriz:
        print(fila)

    return matriz    

def leer_vecotor():
    vector=[]
    cantidad=int(input("Cantidad de datos en el vecctor: "))
    for i in range(cantidad):
        vector.append(int(input(f'Dato({i})= ')))

    print(vector)
    return vector


def ejercicio_planteado():
    matriz=leer_matriz()
    vector=leer_vecotor()
    filas=len(matriz)
    columnas=len(matriz[0])
    cantidad=len(vector)
    vector_nuevo=[]
    for i in range(filas):
        for j in range(columnas):
            c=1
            div=0
            while c<= matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                print(matriz[i][j],"Es primo")
                dato= matriz[i][j] in vector_nuevo
                if dato==False:
                    vector_nuevo.append(matriz[i][j])

    for i in range(cantidad):
        c=1
        div=0
        while c<= vector[i]:
            if vector[i]%c==0:
                div+=1
            c+=1
        if div==2:
            print("es primo",vector[i])
            dato=vector[i] in vector_nuevo
            if dato ==False:
                vector_nuevo.append(vector[i])

    print("vector con datos primos sin repetir", vector_nuevo)

    #ordenar vector nuevo
    # Ordenar vector nuevo
    for i in range(len(vector_nuevo)):
        for j in range(i + 1, len(vector_nuevo)):
            if vector_nuevo[j] < vector_nuevo[i]:
                aux = vector_nuevo[i]
                vector_nuevo[i] = vector_nuevo[j]
                vector_nuevo[j] = aux


    print("vector ordenado: ",vector_nuevo)           


##empieza el menu



import os
while True:
    os.system('cls')
    print("MENU")
    print("")
    print("1. EXAMEN 1")
    print("2. EXAMEN 2")
    print("3. TALLER 1")
    print("4. TALLER 2")
    print("5. TALLER 3")
    print("6. EJERCICIO DE SUSTENTACION")
    print("*************")
    print("0. SALIR")
    print("")
    opcion =int(input('Elija una opción: '))
    match opcion:
        case 1:
            while True:
                os.system('cls')
                print("HAZ ELEGIDO EXAMEN 1")
                print("")
                print(" 1. EXAMEN 1:PUNTO 1")
                print(" 2. EXAMEN 1:PUNTO 2")
                print(" 3. EXAMEN 1:PUNTO 3")
                print(" 4. EXAMEN 1:PUNTO 4")
                print(" 5 agregado")
                print("*************")
                print("0. SALIR")
                print("")
                
                opcion =int(input('Elija una opción: '))
                match opcion:
                    case 1:
                        cprim = 0
                        primomayor = 0
                        parmenor = 0
                        fibonaccimen = 0
                        cparm = 0
                        cf = 0
                        cd = 1

                        cn = int(input('ingresar cantidad de numeros= '))

                        while cd <= cn:
                            n = int(input('ingresar numero= '))
                            c = 2
                            b = 0
                            cd = cd + 1
                            while c * c <= n and b == 0:
                                if n % c == 0:
                                    b = 1
                                c = c + 1
                            if b == 0:
                                cprim = cprim + 1
                                if cprim == 1:
                                    primomayor = n
                                else:
                                    if n > primomayor:
                                        primomayor = n
                            if n % 2 == 0 and (cparm == 0 or n < parmenor):
                                parmenor = n
                                cparm += 1
                            A = 0
                            B = 1
                            T = 0
                            while T < n:
                                T = A + B
                                A = B
                                B = T
                            if T == n:
                                cf = cf + 1
                                if cf == 1:
                                    fibonaccimen = n
                                else:
                                    if n < fibonaccimen:
                                        fibonaccimen = n
                                        
                        print("el fibonacci menor es:", fibonaccimen)
                        print("el par menor es: ", parmenor)
                        print("el primo mayor es:", primomayor)

                        multsumas=0 
                        for i in range(fibonaccimen):
                            multsumas += primomayor

                        multsumas2=0 
                        for i in range(parmenor):
                            multsumas2 += multsumas

                        print("La multiplicación con sumas del primo mayor, el Fibonacci menor y el par menor es:", multsumas2)
                        os.system('pause')
                    case 2:
                            cf=0
                            fb2=0
                            cfr=0
                            cn=int(input("Ingresar cantdad de nuemros= "))
                            cd=0
                            while cd<cn:
                                n=int(input("ingresar numero= "))
                                A=0
                                B=1
                                T=0
                                while T< n:
                                    T=A+B
                                    A=B
                                    B=T
                                if T==n:
                                    cf=cf+1
                                    if cf==2:
                                        fb2=n
                                        cfr=cfr+1
                                    else:
                                        if n==fb2:
                                            cfr=cfr+1
                                cd=cd+1
                            print('numero de veces que se repite el segundo fibonacci= ', cfr)
                            bpr=0
                            cp=2
                            while cp < cfr and bpr==0:
                                if cfr%cp==0:
                                    bpr=1
                                cp=cp+1
                            if  bpr==0:
                                print('contador de fibonacci es primo')
                            else:
                                print('contador fibonacci no es primo')
                                os.system('VEAMOS')
                    case 3:
                            teq=0
                            tes=0
                            tis=0
                            spe=0
                            ct=0
                            cdt=int(input("ingresar cantidad de ternas= "))
                            while ct<cdt:
                                n1=int(input('ingresar n1= '))
                                n2=int(input('ingresar n2= '))
                                n3=int(input('ingresar n3= '))
                                if n1==n2 and n2==n3:
                                    teq=teq+1
                                    spe=spe+n1+n2+n3
                                else:
                                    if n1==n2 or n1==n3 or n2==n3:
                                        tis=tis+1
                                    else:
                                        tes=tes+1
                                ct=ct+1
                            print('numero de triangulos equilateros= ',teq)
                            print('numero de triangulos isoceles= ', tis)
                            print('numero de triangulos escalenos= ',tes)
                            A=0
                            B=1
                            T=0
                            while T<=spe:
                                T=A+B
                                A=B
                                B=T
                            if T==spe:
                                print('la suma es perimetros de los triangulos equilateros es finobacci',spe)
                            else:
                                print('la suma es perimetros de los triangulos equilateros no es  finobacci',spe)           
                            os.system('pause')
                    case 4:
                                cn = int(input('Ingrese la cantidad de números: '))
                                f1 = 0
                                f2 = 0
                                f3 = 0
                                cfibo = 0
                                for i in range(cn):
                                    n = int(input(f'Ingrese el número {i + 1}: '))
                                    a, b = 0, 1
                                    while b < n:
                                        a, b = b, a + b
                                    if b == n and cfibo < 3:
                                        cfibo += 1
                                        if cfibo == 1:
                                            f1 = n
                                        elif cfibo == 2:
                                            f2 = n
                                        else:
                                            f3 = n

                                if cfibo == 3:
                                    min_fib = min(f1, f2, f3)
                                    max_fib = max(f1, f2, f3)
                                    total = 0
                                    c = 0
                                    for i in range(min_fib + 1, max_fib):
                                        if i % 2 == 0:
                                            total += i
                                            c += 1
                                    if c > 0:
                                        avg = total / c
                                        print(f'El promedio de los números pares entre {min_fib} y {max_fib} es {avg:.2f}')
                                    else:
                                        print(f'No hay números pares entre {min_fib} y {max_fib}')
                                else:
                                    print('No se ingresaron suficientes números de Fibonacci')
                                    os.system('pause')        
                    
                    case 5:
                        ejercicio_planteado()
                        os.system('pause')
                    case 0:
                        print('Sale de ciclo ')
                        break
                    case other: 
                        print('Ha digitado una opción invalida ')
                        os.system("pause")   
        case 2:    
            while True:
                os.system('cls')
                print("HAZ ELEGIDO EXAMEN 2")
                print("")
                print(" 1. EXAMEN 2:PUNTO 1")
                print(" 2. EXAMEN 2:PUNTO 2")
                print(" 3. EXAMEN 2:PUNTO 3")
                print(" 4. EXAMEN 2:PUNTO 4")
                
                print("*************")
                print("0. SALIR")
                print("")    
                opcion =int(input('Elija una opción: '))
                match opcion:
                    case 1:   
                        numero=int(input("Numero: "))
                        c=0
                        while numero!=-5:
                            aux=numero
                            cantidad_datos=0
                            while numero==aux:
                                cantidad_datos+=1
                                numero=int(input("Numero: "))
                            c+=1
                            if c==1:
                                grupo_mayor=aux
                                cantidad_mayor=cantidad_datos
                                grupo_menor=aux
                                cantidad_menor=cantidad_datos
                            else:
                                if cantidad_datos>cantidad_mayor:
                                    cantidad_mayor=cantidad_datos
                                    grupo_mayor=aux
                                elif cantidad_datos<cantidad_menor:
                                    cantidad_menor=cantidad_datos
                                    grupo_menor=aux

                        print("Grupo mayo: ",grupo_mayor," Veces ",cantidad_mayor)
                        print("Grupo menor: ",grupo_menor," Veces: ",cantidad_menor)
                        c_2=cantidad_menor
                        c_3=1
                        while c_3<cantidad_mayor:
                            c_2+=cantidad_menor
                            c_3+=1

                        print("Su multiplicacion es= ",c_2) 
                        os.system('pause')
                    case 2:
                        cantidad_datos1=int(input("Cantidad de datos vector 1: "))
                        v_1=[]
                        print("Datos en lista 1: ")
                        for i in range(cantidad_datos1):
                            v_1.append(int(input("Dato({})=".format(i))))

                        cantidad_datos2=int(input("Cantidad de datos en vector 2: "))
                        v_2=[]
                        print("Datos en lista 2: ")
                        for j in range(cantidad_datos2):
                            v_2.append(int(input("Dato({})=".format(j))))

                        v_fibonaccis=[]
                        v_multiplos=[]
                        for i in range(cantidad_datos1):
                            a=0
                            b=1
                            t=0
                            while t<v_1[i]:
                                t=a+b
                                a=b
                                b=t

                            if v_1[i]%3==0:
                                dato_1=v_1[i] in v_2
                                if dato_1==True:
                                    v_multiplos.append(v_1[i]) 
                                    if v_1[i]%5==0:
                                        print("Multiplo de 3 en comun y no multiplo de 5: ",v_1[i],"(ingresa a la lista)")
                                        v_multiplos.remove(v_1[i])  

                            if v_1[i]==t:
                                dato_1=v_1[i] in v_2
                                if dato_1==False:
                                    print("Fibonacci  no comun",v_1[i])
                                    dato_2=v_1[i] in v_fibonaccis
                                    if dato_2==False:
                                        v_fibonaccis.append(v_1[i])

                        for j in range(cantidad_datos2):
                            a=0
                            b=1
                            t=0
                            while t<v_2[j]:
                                t=a+b
                                a=b
                                b=t

                            if v_2[j]%3==0:
                                dato_1=v_2[j] in v_1
                                if dato_1==True:
                                    v_multiplos.append(v_2[j])
                                    if v_2[j]%5==0:
                                        print("Multiplo de 3 en comun y no multiplo de 5: ",v_2[j],"(ingresa a la lista)")
                                        v_multiplos.remove(v_2[j])    

                            if v_2[j]==t:
                                dato_1=v_2[j] in v_1
                                if dato_1==False:
                                    print("Fibonacci no comun",v_2[j])
                                    dato_2=v_2[j] in v_fibonaccis
                                    if dato_2==False:
                                        v_fibonaccis.append(v_2[j])    

                        print("Vector de fibonaccis no comunes y sin repetir: ",v_fibonaccis)
                        print("Vector con multiplos de 3 comunes que no son multiplos de 5: ",v_multiplos)                    
                        os.system('pause')
                    case 3:
                            cantidad_datos1 = int(input("Cantidad de datos en vector 1: "))
                            v_1 = []
                            print("Datos en vector 1: ")
                            for i in range(cantidad_datos1):
                                v_1.append(int(input("Dato({})=".format(i))))

                            cantidad_datos2 = int(input("Cantidad de datos en vector 2: "))
                            v_2 = []
                            print("Datos en vector 2: ")
                            for j in range(cantidad_datos2):
                                v_2.append(int(input("Dato({})=".format(j))))

                            sifibo = 0
                            v_rango = []
                            for i in range(cantidad_datos1):
                                a = 0
                                b = 1
                                t = 0
                                while t < v_1[i]:
                                    t = a + b
                                    a = b
                                    b = t

                                if v_1[i] == t:
                                    sifibo += 1
                                    if sifibo == 3:
                                        tercer_fibonacci = v_1[i]
                                        print("Tercer fibonacci: ", tercer_fibonacci)
                                        v_rango.append(v_1[i])

                            dato = cantidad_datos2 - tercer_fibonacci
                            v_rango.insert(1, dato)
                            print("El primer rango tendra una cantidad de:", v_rango[0], "datos", "El segundo rango tendra una cantidad de:", v_rango[1], "datos")
                            i = 0
                            j = 0
                            c = 0
                            while i < len(v_rango):
                                c += 1
                                if c == 1:
                                    # Orden ascendente
                                    limite_final_a = j + v_rango[i]
                                    while j < limite_final_a:
                                        x = j + 1
                                        while x < limite_final_a:
                                            if v_2[x] < v_2[j]:
                                                aux = v_2[j]
                                                v_2[j] = v_2[x]
                                                v_2[x] = aux
                                            x += 1
                                        j += 1
                                    i += 1
                                else:
                                    # Orden descendente
                                    limite_final_b = j + v_rango[i]
                                    while j < limite_final_b:
                                        x_1 = j + 1
                                        while x_1 < limite_final_b:
                                            if v_2[x_1] > v_2[j]:
                                                aux = v_2[j]
                                                v_2[j] = v_2[x_1]
                                                v_2[x_1] = aux
                                            x_1 += 1
                                        j += 1
                                    i += 1

                            print("Lista ordenada ascendente y descendentemente: ")
                            for z in range(len(v_2)):
                                print("Posicion:", z, "Dato:", v_2[z])
                            os.system('pause')
                    case 4:
                            v = []
                            cantidad_datos = int(input("Cantidad de datos en vector: "))
                            print("Datos en vector:")
                            for i in range(cantidad_datos):
                                v.append(int(input("Dato({})=".format(i))))

                            matriz = []
                            Filas = int(input("Numero de filas: "))
                            Columnas = int(input("Numero de columnas: "))
                            for i in range(Filas):
                                fila = []
                                for j in range(Columnas):
                                    fila.append(int(input(f'Dato {i},{j} = ')))
                                matriz.append(fila)

                            print("Vector:", v)
                            print("Matriz:", matriz)

                            si_primo = 0
                            for primo in v:
                                c = 1
                                div = 0
                                while c <= primo:
                                    if primo % c == 0:
                                        div += 1
                                    c += 1

                                if div == 2:
                                    si_primo += 1
                                    if si_primo == 1:
                                        for i in range(Filas):
                                            j = 0
                                            while j < Columnas:
                                                if primo == matriz[i][j]:
                                                    fila_primo_1 = i
                                                    print("Fila del primer primo en común:", fila_primo_1)
                                                    break
                                                j += 1
                                    elif si_primo == 2:
                                        for i in range(Filas):
                                            j = 0
                                            while j < Columnas:
                                                if primo == matriz[i][j]:
                                                    fila_primo_2 = i
                                                    print("Fila del segundo primo en común:", fila_primo_2)
                                                    break
                                                j += 1

                            for j in range(Columnas):
                                aux=matriz[fila_primo_1][j]
                                matriz[fila_primo_1][j]=matriz[fila_primo_2][j]
                                matriz[fila_primo_2][j]=aux

                            for i in range(Filas):
                                for j in range(Columnas):
                                    print(f'Dato {i},{j}=',matriz[i][j])
                    case 0:
                        print('Sale de ciclo ')
                        break
                    case other: 
                        print('Ha digitado una opción invalida ')
                        os.system("pause")                                               
        case 3: 
            while True:
                os.system('cls')
                print("HAZ ELEGIDO TALLER 1")
                print("")
                print(" 1. TALLER 1:PUNTO 1")
                print(" 2. TALLER 1:PUNTO 2")
                print(" 3. TALLER 1:PUNTO 3")
                print(" 4. TALLER 1:PUNTO 4")
                print(" 5. TALLER 1:PUNTO 5") 
                print("*************")
                print("0. SALIR")
                print("")
                
                opcion =int(input('Elija una opción: '))
                match opcion:
                    case 1:
                        nd = int(input("Número de datos "))
                        cont = 1
                        es_prim = 0
                        es_fib = 0
                        while cont <= nd:
                            dato = int(input("Ingresar dato "))
                            cont2 = 1
                            mv = 0
                            while cont2 <= dato:
                                if dato % cont2 == 0:
                                    mv += 1
                                cont2 += 1
                            if mv == 2:
                                es_prim += 1
                                if es_prim == 1:
                                    primay = dato
                                elif dato > primay:
                                    primay = dato

                            a = 0
                            b = 1
                            t = 0
                            while t < dato:
                                t = a+b
                                a = b
                                b = t
                            if dato == t:
                                es_fib += 1
                                if es_fib == 1:
                                    fibmen = dato
                                elif dato < fibmen:
                                    fibmen = dato
                            cont += 1
                        print("El primo mayor y fibonacci menor son ", primay, fibmen)
                        if primay < fibmen:
                            aux = fibmen
                            fibmen = primay
                            primay = aux

                        psum = 0
                        npares = 0
                        cont3 = fibmen+1
                        print("Numeros pares entre estos dos datos: ")
                        while cont3 < primay:
                            if cont3 % 2 == 0:
                                print(cont3)
                                psum += cont3
                                npares += 1
                            cont3 += 1

                        if npares > 0:
                            prom = psum/npares
                            print("Promedio de pares entre el fibonacci menor y el primo mayor es ", prom)
                        else:
                            print("Sin números pares entre el fibonacci menor y el primo mayor") 
                            os.system('pause') 
                            
                    case 2:
                            nd = int(input("Cantidad de datos: "))
                            cont = 1
                            es_prim = 0
                            es_fib = 0
                            while cont <= nd:
                                dato = int(input("Ingrese dato "))
                                cont2 = 1
                                mv = 0
                                while cont2 <= dato:
                                    if dato % cont2 == 0:
                                        mv += 1
                                    cont2 += 1
                                if mv == 2:
                                    es_prim += 1
                                    if es_prim == 1:
                                        primay = dato
                                    elif dato > primay:
                                        primay = dato
                                a = 0
                                b = 1
                                t = 0

                                while t < dato:
                                    t = a+b
                                    a = b
                                    b = t
                                if dato == t:
                                    es_fib += 1
                                    if es_fib == 1:
                                        fibmen = dato
                                    elif dato < fibmen:
                                        fibmen = dato
                                cont += 1
                            print(primay, " es el primo mayor ", fibmen, "es el fibonacci menor")
                            if primay < fibmen:
                                aux = fibmen
                                fibmen = primay
                                primay = aux

                            sfac = 0
                            nfac = 0
                            cont2 = fibmen+1
                            while cont2 < primay:
                                if cont2 % 2 != 0:
                                    c = cont2
                                    nfac = 1
                                    while c > 0:
                                        nfac *= c
                                        c -= 1
                                    print("El impar ", cont2)
                                    sfac += nfac
                                    nfac += 1
                                cont2 += 1
                            if nfac > 0:
                                prom = sfac/nfac
                                print("Factoriales de los impares promediados ", prom)
                            else:
                                print("Sin impares entre el fibonacci menor y el primo mayor") 
                                os.system('pause')  
                                                
                    case 3:
                                cd = int(input("digitar cantidad de numeros a analizar"))
                                suma = 0
                                c = 0
                                for i in range(1, cd+1):
                                    num = int(input("digitar dato"))
                                    if esfib(num):
                                        if isprime(num):
                                            suma += num
                                            c += 1
                                p = suma/c
                                print("promedio de los numeros qque son fibonacci y primos a la vez:", p) 
                                os.system('pause')
                    
                    case 4:
                                cd = int(input("digitar cantidad de numeros a analizar"))
                                cp = 0
                                ca = 0
                                aux = 0
                                for i in range(1, cd+1):
                                    num = int(input("digitar dato"))
                                    if isprime(num):
                                        cp += 1
                                        if cp == 2:
                                            aux = num
                                    if num == aux:
                                        ca += 1
                                print("las veces que se repite el segundo primo es:", ca)                              
                                os.system('pause')
                    case 5:
                            ct = int(input("ingrese la cantidad de ternas a digitar : "))
                            se = 0
                            si = 0
                            ses = 0
                            for i in range(ct):
                                print(f"\nTerna N° {i+1}")
                                a = int(input("ingrese el valor a : "))
                                b = int(input("ingrese el valor b : "))
                                c = int(input("ingrese el valor c : "))
                                if a == b == c:
                                    se += 1
                                elif a == b or a == c or b == c:
                                    si += 1
                                else:
                                    ses += 1
                            print(f"\ntriangulos equialteros : {se}")
                            print(f"triangulos isoceles : {si}")
                            print(f"triangulos escalenos : {ses}\n") 
                    case 0:
                            print('Sale de ciclo ')
                            break
                    case other: 
                            print('Ha digitado una opción invalida ')
                            os.system("pause") 
        case 4:
             while True:
                os.system('cls')
                print("HAZ ELEGIDO TALLER 2")
                print("")
                print(" 1. TALLER 2:PUNTO 1")
                print(" 2. TALLER 2:PUNTO 2")
                print(" 3. TALLER 2:PUNTO 3")
                print(" 4. TALLER 2:PUNTO 4")
                print(" 5. TALLER 2:PUNTO 5") 
                print("*************")
                print("0. SALIR")
                print("")
                
                opcion =int(input('Elija una opción: '))
                match opcion:
                    case 1: 
                            a = [5, 7, 12, 18, 25, 31]
                            b = [37, 35, 29, 19, 14]
                            c = []
                            ta = len(a)
                            tb = len(b)
                            i = ta-1
                            j = 0
                            print(a)
                            print(b)
                            while i >= 0 and j < tb:
                                if a[i] > b[j]:
                                    c.append(a[i])
                                    i -= 1
                                else:
                                    c.append(b[j])
                                    j += 1
                            if i == -1:
                                while j <= tb:
                                    c.append(b[j])
                                    j += 1
                            else:
                                while i >= 0:
                                    c.append(a[i])
                                    i -= 1
                            print("vector ordenado por mezcla : ", c)
                            os.system('cls')
                    case 2:   
                            a = [5, 7, 12, 18, 25, 31]
                            b = [37, 35, 29, 19, 14]
                            c = []
                            ta = len(a)
                            tb = len(b)
                            i = ta-1
                            j = 0
                            print(a)
                            print(b)
                            while i >= 0 and j < tb:
                                if a[i] > b[j]:
                                    if a[i] % 2 == 0:
                                        c.append(a[i])
                                    i -= 1
                                else:
                                    if b[j] % 2 == 0:
                                        c.append(b[j])
                                    j += 1
                            if i == -1:
                                while j <= tb:
                                    if b[j] % 2 == 0:
                                        c.append(b[j])
                                    j += 1
                            else:
                                while i >= 0:
                                    if a[i] % 2 == 0:
                                        c.append(a[i])
                                    i -= 1
                            print("vector ordenado por mezcla : ", c)
                            os.system('cls')
                        
                    case 3: 
                            a = [3, 5, 13, 21, 15, 4, 9]
                            v = []
                            x = 0
                            print(a)
                            for i in range(len(a)):
                                c = 0
                                b = 1
                                t = 0
                                while t < a[i]:
                                    t = c+b
                                    c = b
                                    b = t
                                if t == a[i]:
                                    if x == 0:
                                        g = a[i]
                                        l = a[i]
                                        x = 1
                                    else:
                                        if a[i] > g:
                                            g = a[i]
                                        else:
                                            if a[i] < l:
                                                l = a[i]
                            k = l
                            while k <= g:
                                r = 2
                                p = False
                                while r < k and p == False:
                                    if k % r == 0:
                                        p = True
                                    r += 1
                                if not p:
                                    v.append(k)
                                k += 1
                            print("los numeros primos que estan entre el ", l, " y el ", g, " son : ", v)
                            os.system('cls')                    
                    case 4:
                            a = [1, 3, 13, 5, 21, 15, 4, 9]
                            v = []
                            x = 1
                            do = 0
                            dr = 0
                            print(a)
                            for i in range(len(a)):
                                c = 0
                                b = 1
                                t = 0
                                while t < a[i]:
                                    t = c+b
                                    c = b
                                    b = t
                                if t == a[i]:
                                    if x == 2:
                                        l = a[i]
                                    else:
                                        if x == 3:
                                            g = a[i]
                                    x += 1
                            if l < g:
                                k = l
                                while k <= g:
                                    if k % 3 == 0:
                                        do += k
                                        dr += 1
                                    k += 1
                            else:
                                k = g
                                while k <= l:
                                    if k % 3 == 0:
                                        do += k
                                        dr += 1
                                    k += 1
                            if dr > 0:
                                prom = do/dr
                            print("el promedio de los multiplos de 3 que estan entre el ",
                                l, " y el ", g, " es : ", prom)
                            os.system('cls')
                    case 5: 
                            a = [1, 3, 13, 5, 21, 15, 4, 9]
                            v = []
                            x = 1
                            r = 1
                            print(a)
                            print("vector ingrasado : ", a)
                            for i in range(len(a)):
                                c = 0
                                b = 1
                                t = 0
                                while t < a[i]:
                                    t = c+b
                                    c = b
                                    b = t
                                if t == a[i]:
                                    if x == 2:
                                        l = a[i]
                                        pl = i
                                    else:
                                        if x == 3:
                                            g = a[i]
                                            pg = i
                                    x += 1
                            if l < g:
                                while l > 0:
                                    r *= l
                                    l -= 1
                                a.insert(pl, r)
                                a.remove(a[pl+1])
                                a.insert(pg, r)
                                a.remove(a[pg+1])
                            else:
                                while g > 0:
                                    r *= g
                                    g -= 1
                                a.insert(pl, r)
                                a.remove(a[pl+1])
                                a.insert(pg, r)
                                a.remove(a[pg+1])

                            print("vector resultante : ", a)
                    case 0:
                            print('Sale de ciclo ')
                            break
                    case other: 
                            print('Ha digitado una opción invalida ')
                            os.system("pause")
                            
        case 5:
             while True:
                os.system('cls')
                print("HAZ ELEGIDO TALLER 3")
                print("")
                print(" 1. TALLER 3:PUNTO 1")
                print(" 2. TALLER 3:PUNTO 2")
                print(" 3. TALLER 3:PUNTO 3")
                print(" 4. TALLER 3:PUNTO 4")
                print(" 5. TALLER 3:PUNTO 5")
                print(" 6. TALLER 3:PUNTO 6") 
                print(" 7. TALLER 3:PUNTO 7") 
                print(" 8. TALLER 3:PUNTO 8") 
                print(" 9. TALLER 3:PUNTO 9") 
                print(" 10. TALLER 3:PUNTO 10")
                print(" 11. TALLER 3:PUNTO 11")  
                print("*************")
                print("0. SALIR")
                print("")
                
                opcion =int(input('Elija una opción: '))
                match opcion:
                    case 1: 
                            f = int(input("Ingrese la cantidad de filas: "))
                            c = int(input("Ingrese la cantidad de columnas: "))
                            m1 = []
                            m2 = []
                            v = []

                            leermatriz(m1, f, c)
                            leermatriz(m2, f, c)

                            m2 = [num for row in m2 for num in row]

                            for i in range(f):
                                for j in range(c):
                                    if isprime(m1[i][j]):
                                        if m1[i][j] in m2 and m1[i][j] not in v:
                                            v.append(m1[i][j])

                            print(v)    
                            os.system('pause')
                    case 2: 
                            f = int(input("Ingrese la cantidad de filas: "))
                            c = int(input("Ingrese la cantidad de columnas: "))
                            m = []
                            leermatriz(m, f, c)
                            v = []

                            for i in range(len(m)):
                                if isprime(m[i][i]):
                                    v.append(m[i][i])

                            for i in range(len(m)):
                                if isprime(m[i][len(m)-1-i]):
                                    v.append(m[i][len(m)-1-i])

                            print(v)
                            os.system('pause')                                   
                    case 3: 
                                f = int(input("Ingrese la cantidad de filas: "))
                                c = int(input("Ingrese la cantidad de columnas: "))
                                mat = []
                                leermatriz(mat, f, c)

                                sum1 = 0
                                sum2 = 0
                                cont1 = 0
                                cont2 = 0
                                for i in range(f):
                                    for j in range(c):
                                        if i < j:
                                            if mat[i][j] % 2 == 0:
                                                sum1 += mat[i][j]
                                                cont1 += 1
                                        if i > j:
                                            if mat[i][j] % 2 != 0:
                                                sum2 += mat[i][j]
                                                cont2 += 1
                                print("Promedio de los pares que están sobre la diagonal principal: ", sum1/cont1)
                                print("Promedio de los impares que están bajo la diagonal principal: ", sum2/cont2) 
                                os.system('pause')                                              
                    case 4:
                            r = int(input("Ingrese el numero de filas: "))
                            c = int(input("Ingrese el numero de columnas: "))
                            matrix = []
                            leermatriz(matrix, r, c)
                            segprime = 0
                            cuaprime = 0
                            cont = 0
                            cont1 = 0
                            for j in range(c):
                                for i in range(r):
                                    if isprime(matrix[i][j]):
                                        cont += 1
                                        if cont == 2:
                                            segprime = matrix[i][j]
                                        if cont == 4:
                                            cuaprime = matrix[i][j]
                            isconsec(segprime, cuaprime)
                            os.system('pause')
                    case 5:
                                f= int(input("Ingrese la cantidad de filas: "))
                                c = int(input("Ingrese la cantidad de columnas: "))
                                mat = []
                                leermatriz(mat, f, c)

                                for j in range(c):
                                    if j % 2 == 0:
                                        for i in range(f):
                                            for k in range(i+1, f):
                                                if mat[i][j] > mat[k][j]:  # order ascendent
                                                    aux = mat[i][j]
                                                    mat[i][j] = mat[k][j]
                                                    mat[k][j] = aux
                                    else:
                                        for i in range(f):
                                            for k in range(i+1, f):
                                                if mat[i][j] < mat[k][j]:  # order descendent
                                                    aux = mat[i][j]
                                                    mat[i][j] = mat[k][j]
                                                    mat[k][j] = aux
                                for f in mat:
                                    print(f)
                                    os.system('pause')
                    case 6:
                            f = int(input("Ingrese la cantidad de filas: "))
                            c = int(input("Ingrese la cantidad de columnas: "))
                            m1 = []
                            m2 = []
                            v = []
                            leermatriz(m1, f, c)
                            leermatriz(m2, f, c)

                            m1 = [num for row in m1 for num in row]
                            m2 = [num for row in m2 for num in row]
                            m3 = m1 + m2

                            merge_sort(m3)

                            v = m3

                            print(v)
                            os.system('pause')
                    case 7:
                                f = int(input("ingerse la cantidad de filas"))
                                c = int(input("ingrese la cant de columnas"))
                                m = []
                                leermatriz(m, f, c)

                                prom = []
                                for i in range(f):
                                    sum = 0
                                    for j in range(c):
                                        sum += m[i][j]
                                    prom.append(sum/c)
                                for I in range(f):
                                    for k in range(I+1, f):
                                        if prom[I] > prom[k]:
                                            aux = prom[I]
                                            prom[I] = prom[k]
                                            prom[k] = aux
                                            aux = m[I]
                                            m[I] = m[k]
                                            m[k] = aux

                                for row in m:
                                    print(row)
                                    os.system('pause')
                    case 8: 
                        while True:
                                os.system('cls')
                                print("HAZ ELEGIDO TALLER 3 y el punto 8")
                                print("")
                                print(" 1. SUBPUNTO 1")
                                print(" 2. SUBPUNTO 2")
                                print(" 3. SUBPUNTO 3")
                                print(" 4. SUBPUNTO 4")
                                print(" 5. SUBPUNTO 5")
                                print("*************")
                                print("0. SALIR")
                                print("")
                                
                                opcion =int(input('Elija una opción: '))
                                match opcion:
                                    case 1:
                                            f = int(input("Ingrese la cantidad de filas: "))
                                            c = int(input("Ingrese la cantidad de columnas: "))
                                            m = []
                                            leermatriz(m, f, c)

                                            sum1 = 0
                                            sum2 = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if i == j:
                                                        sum1 += m[i][j]
                                                    if i+j == f-1:
                                                        sum2 += m[i][j]
                                            print("Promedio de la diagonal principal: ", sum1/f)
                                            print("Promedio de la diagonal secundaria: ", sum2/f)
                                            os.system('pause')
                                    case 2:
                                            f = int(input("Ingrese la cantidad de filas: "))
                                            c = int(input("Ingrese la cantidad de columnas: "))
                                            m = []
                                            leermatriz(m, f, c)
                                            # ordenar ascendentemente la diagonal principal
                                            for i in range(f):
                                                for j in range(c):
                                                    if i == j:
                                                        for x in range(f):
                                                            for y in range(c):
                                                                if x == y:
                                                                    if m[i][j] < m[x][y]:
                                                                        aux = m[i][j]
                                                                        m[i][j] = m[x][y]
                                                                        m[x][y] = aux

                                            for i in range(f):
                                                for j in range(c):
                                                    print(m[i][j], end=" ")
                                                print() 
                                                os.system('pause')
                                    case 3: 
                                        f = int(input("Ingrese la cantidad de filas: "))
                                        c = int(input("Ingrese la cantidad de columnas: "))
                                        m = []
                                        leermatriz(m, f, c)
                                        # promedio pares encima de la diagonal principal
                                        sum1 = 0
                                        cant = 0
                                        for i in range(f):
                                            for j in range(c):
                                                if i < j and m[i][j] % 2 == 0:
                                                    sum1 += m[i][j]
                                                    cant += 1

                                        print("Promedio de los pares encima de la diagonal principal: ", sum1/cant)

                                        # promedio de los impares de la diagonal secundaria
                                        sum2 = 0
                                        cant2 = 0
                                        for i in range(f):
                                            for j in range(c):
                                                if i+j == f-1 and m[i][j] % 2 != 0:
                                                    sum2 += m[i][j]
                                                    cant2 += 1
                                        print("Promedio de los impares de la diagonal secundaria: ", sum2/cant2)
                                        os.system('pause')
                                        
                                    case 4:
                                        f = int(input("Ingrese la cantidad de filas: "))
                                        c = int(input("Ingrese la cantidad de columnas: "))
                                        m = []
                                        leermatriz(m, f, c)

                                        pmen = 100000
                                        for i in range(f):
                                            for j in range(c):
                                                if isprime(m[i][j]) and m[i][j] < pmen:
                                                    pmen = m[i][j]

                                        for x in range(f):
                                            for y in range(c):
                                                if x == y:
                                                    m[x][y] = pmen

                                        fibmay = 0
                                        for i in range(f):
                                            for j in range(c):
                                                if esfib(m[i][j]) and m[i][j] > fibmay:
                                                    fibmay = m[i][j]
                                        # poner la diagonal secundaria con el menor fibonacci
                                        for x in range(f):
                                            for y in range(c):
                                                if x+y == f-1:
                                                    m[x][y] = fibmay

                                        for f in m:
                                            print(f)
                                            os.system('pause')
 
                                    case 5: 
                                            f = int(input("Ingrese la cantidad de filas: "))
                                            c = int(input("Ingrese la cantidad de columnas: "))
                                            m = []
                                            leermatriz(m, f, c)
                                            maypar = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if m[i][j] % 2 == 0:
                                                        if m[i][j] > maypar:
                                                            maypar = m[i][j]

                                            menimpar = 100000
                                            for i in range(f):
                                                for j in range(c):
                                                    if m[i][j] % 2 != 0:
                                                        if m[i][j] < menimpar:
                                                            menimpar = m[i][j]
                                            # poner el contorno con el mayor par
                                            for x in range(f):
                                                for y in range(c):
                                                    if x == 0 or y == 0 or x == f-1 or y == c-1:
                                                        m[x][y] = maypar

                                            # poner la parte interna con el menor impar
                                            for x in range(f):
                                                for y in range(c):
                                                    if x != 0 and y != 0 and x != f-1 and y != c-1:
                                                        m[x][y] = menimpar

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 0:
                                                print('Sale de ciclo ')
                                                break
                                    case other: 
                                                print('Ha digitado una opción invalida ')
                                                os.system("pause")
                    case 9:
                         while True:
                                os.system('cls')
                                print("HAZ ELEGIDO TALLER 3 y el punto 9")
                                print("")
                                print(" 1. SUBPUNTO 1")
                                print(" 2. SUBPUNTO 2")
                                print(" 3. SUBPUNTO 3")
                        
                                print("*************")
                                print("0. SALIR")
                                print("")
                                
                                opcion =int(input('Elija una opción: '))
                                match opcion:
                                    case 1:
                                            f = int(input("Ingrese la cantidad de filas: "))
                                            c = int(input("Ingrese la cantidad de columnas: "))
                                            f2 = int(input("Ingrese la cantidad de filas: "))
                                            c2 = int(input("Ingrese la cantidad de columnas: "))
                                            m1 = []
                                            m2 = []
                                            v = []

                                            leermatriz(m1, f, c)
                                            leermatriz(m2, f2, c2)

                                            m2 = [num for row in m2 for num in row]

                                            for i in range(f):
                                                for j in range(c):
                                                    if m1[i][j] in m2 and m1[i][j] not in v:
                                                        v.append(m1[i][j])

                                                    print(v)
                                                    os.system('pause')
                                    case 2:
                                            f = int(input("Ingrese la cantidad de filas: "))
                                            c = int(input("Ingrese la cantidad de columnas: "))
                                            f2 = int(input("Ingrese la cantidad de filas: "))
                                            c2 = int(input("Ingrese la cantidad de columnas: "))
                                            m1 = []
                                            m2 = []
                                            v = []

                                            leermatriz(m1, f, c)
                                            leermatriz(m2, f2, c2)

                                            m2 = [num for row in m2 for num in row]

                                            for i in range(f):
                                                for j in range(c):
                                                    if isprime(m1[i][j]):
                                                        if m1[i][j] in m2 and m1[i][j] not in v:
                                                            v.append(m1[i][j])

                                            print(v) 
                                            os.system('pause')               
                                    case 3:
                                                f = int(input("Ingrese la cantidad de filas: "))
                                                c = int(input("Ingrese la cantidad de columnas: "))
                                                f2 = int(input("Ingrese la cantidad de filas: "))
                                                c2 = int(input("Ingrese la cantidad de columnas: "))
                                                m1 = []
                                                m2 = []
                                                v = []

                                                leermatriz(m1, f, c)
                                                leermatriz(m2, f2, c2)

                                                m2 = [num for row in m2 for num in row]

                                                for i in range(f):
                                                    for j in range(c):
                                                        if isprime(m1[i][j]):
                                                            if m1[i][j] not in m2 and m1[i][j] not in v:
                                                                v.append(m1[i][j])

                                                print(v)
                                                os.system('pause')
                                    case 0:
                                            print('Sale de ciclo ')
                                            break
                                    case other: 
                                            print('Ha digitado una opción invalida ')
                                            os.system("pause")
                                                                                           
                    case 10:
                                f = int(input("Ingrese la cantidad de filas: "))
                                c = int(input("Ingrese la cantidad de columnas: "))
                                m = []
                                v = []
                                leermatriz(m, f, c)
                                m = [num for row in m for num in row]
                                for i in range(len(m)):
                                    cont = 0
                                    for j in range(len(m)):
                                        if m[i] == m[j]:
                                            cont += 1
                                    if esfib(m[i]) and cont not in v:
                                        v.append(cont)
                                print(v)
                                os.system('pause')
                        
                    case 11 : 
                        while True:
                                os.system('cls')
                                print("HAZ ELEGIDO TALLER 3 y el punto 11")
                                print("")
                                print(" 1. SUBPUNTO 1")
                                print(" 2. SUBPUNTO 2")
                                print(" 3. SUBPUNTO 3")
                                print(" 4. SUBPUNTO 4")
                                print(" 5. SUBPUNTO 5")
                                print(" 6. SUBPUNTO 6")
                                print(" 7. SUBPUNTO 7")
                                print(" 8. SUBPUNTO 8")
                                print(" 9. SUBPUNTO 9")
                                print("*************")
                                print("0. SALIR")
                                print("")
                                
                                opcion =int(input('Elija una opción: '))
                                match opcion:
                                    case 1:
                                            r = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, r, c)

                                            aux = m[0]
                                            m[0] = m[r-1]
                                            m[r-1] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 2:   
                                                f = int(input("Ingrese el numero de filas: "))
                                                c = int(input("Ingrese el numero de columnas: "))
                                                m = []

                                                leermatriz(m, f, c)

                                                for j in range(c):
                                                    may = 0
                                                    men = 100000
                                                    s = 0
                                                    c1 = 0
                                                    for i in range(f):
                                                        s = s + m[i][j]
                                                        c1 = c1 + 1

                                                        if m[i][j] > may:
                                                            may = m[i][j]

                                                        if m[i][j] < men:
                                                            men = m[i][j]
                                                    prom = s / c1
                                                    print("el mayor de la columna es: ", may)
                                                    print("el menor de la columna es: ", men)
                                                    print("el prom de la columna es: ", prom)   
                                                    os.system('pause')                                                                                   
                                    case 3:
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)

                                            for i in range(f):
                                                for j in range(c):
                                                    if i % 2 == 0:
                                                        for k in range(j+1, c):
                                                            if m[i][j] > m[i][k]:
                                                                aux = m[i][j]
                                                                m[i][j] = m[i][k]
                                                                m[i][k] = aux
                                                    else:
                                                        for k in range(j+1, c):
                                                            if m[i][j] < m[i][k]:
                                                                aux = m[i][j]
                                                                m[i][j] = m[i][k]
                                                                m[i][k] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 4:
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)

                                            for i in range(f):
                                                for j in range(c):
                                                    for k in range(f):
                                                        for l in range(c):
                                                            if m[i][j] > m[k][l]:
                                                                aux = m[i][j]
                                                                m[i][j] = m[k][l]
                                                                m[k][l] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 5:
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)
                                            # Intercambiar las filas de una matriz de acuerdo al orden ascendente de los promedios de cada fila
                                            prom = []
                                            for i in range(f):
                                                s = 0
                                                c1 = 0
                                                for j in range(c):
                                                    s = s + m[i][j]
                                                    c1 = c1 + 1
                                                prom.append(s/c1)
                                            for I in range(f):
                                                for k in range(I+1, f):
                                                    if prom[I] > prom[k]:
                                                        aux = prom[I]
                                                        prom[I] = prom[k]
                                                        prom[k] = aux
                                                        aux = m[I]
                                                        m[I] = m[k]
                                                        m[k] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 6:
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)
                                            # Intercambiar las filas donde se encuentre el mayor y el menor de la matriz
                                            may = 0
                                            men = 100000
                                            posmay = 0
                                            posmen = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if m[i][j] > may:
                                                        may = m[i][j]
                                                        box = i
                                                    if m[i][j] < men:
                                                        men = m[i][j]
                                                        box1 = i
                                                posmay = box
                                                posmen = box1

                                            aux = m[posmay]
                                            m[posmay] = m[posmen]  # intercambio filas
                                            m[posmen] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 7: 
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)
                                            # Intercambiar la fila donde se encuentre el Fibonacci 2 con la fila donde se encuentra el  Fibonacci 4.
                                            fib2f = 0
                                            fib4f = 0
                                            cf = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if esfib(m[i][j]):
                                                        cf = cf + 1
                                                        if cf == 2:
                                                            fib2f = i
                                                        if cf == 4:
                                                            fib4f = i

                                            aux = m[fib2f]
                                            m[fib2f] = m[fib4f]  # intercambio filas
                                            m[fib4f] = aux

                                            for f in m:
                                                print(f)
                                                os.system('pause')
                                    case 8: 
                                            f = int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)

                                            # Intercambiar las filas donde se encuentre el primo mayor y el Fibonacci menor
                                            mayprimo = 0
                                            menfib = 100000
                                            posmayprimo = 0
                                            posmenfib = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if isprime(m[i][j]):
                                                        if m[i][j] > mayprimo:
                                                            mayprimo = m[i][j]
                                                            posmayprimo = i
                                                    if esfib(m[i][j]):
                                                        if m[i][j] < menfib:
                                                            menfib = m[i][j]
                                                            posmenfib = i

                                            aux = m[posmayprimo]
                                            m[posmayprimo] = m[posmenfib]  # intercambio filas
                                            m[posmenfib] = aux

                                            for f in m:
                                                print(f) 
                                                os.system('pause')               
                                    case 9: 
                                            f= int(input("Ingrese el numero de filas: "))
                                            c = int(input("Ingrese el numero de columnas: "))
                                            m = []

                                            leermatriz(m, f, c)

                                            # Determinar si el primo 2 y el primo 4  son consecutivos, es decir, no hay un número primo entre los dos

                                            primo2 = 0
                                            primo4 = 0
                                            c1 = 0
                                            for i in range(f):
                                                for j in range(c):
                                                    if isprime(m[i][j]):
                                                        c1 = c1 + 1
                                                        if c1 == 2:
                                                            primo2 = m[i][j]
                                                        if c1 == 4:
                                                            primo4 = m[i][j]

                                            if isconsec(primo2, primo4):
                                                print("Lel segundo y cuarto primo son consecutivos")
                                            else:
                                                print("el segundo y cuarto primo nos son consecutivos")
                                                os.system('pause')
                                    case 0:
                                            print('Sale de ciclo ')
                                            break
                                    case other: 
                                            print('Ha digitado una opción invalida ')
                                            os.system("pause")
        case 6:
            os.system('cls')
            print("HAZ ELEGIDO EL EJERCICIO DE SUSTENTACION")
            print("")
            print(" 1. EJERCICIO DE SUSTENTACION 3")
            print("0. SALIR")
            print("")
            opcion=int(input("DIGITE LA OPCION-->"))
            match opcion:
                case 1:
                    Sustentacions_ejercicio3()
                    os.system('pause')
                case other: 
                    print('Ha digitado una opción invalida ')
                    os.system("pause")    
        case 0:
            print('GRACIAS POR SU ATENCION ')
            print("REALIZADO POR Jose Zambrano.")
            break
        case other: 
            print('Ha digitado una opción invalida ')
            os.system("pause")                    