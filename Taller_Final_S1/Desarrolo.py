#FUNCIONES PARA EL MENU
def volverAlInicio():
    print("--------------------------")
    print("0. Volver a inicio")
    print("--------------------------")
def menuPuntos(tipoDeEvaluacion,puntos,volver):
    print(f'''
|-----------------------------------------|
                {tipoDeEvaluacion}                       ''')
    for i in range(1,puntos+1):
        print(f"{i}. Punto {i}")
    print("------------------------------------------")
    print(f"0. {volver}")
    print("|-----------------------------------------|")

def menuParciales(tipoDeEvaluacion,puntos,volver):
    print(f'''
|-----------------------------------------|
                {tipoDeEvaluacion}                       ''')
    for i in range(1,puntos+1):
        print(f"{i}. Parcial {i}")
    print("------------------------------------------")
    print(f"0. {volver}")
    print("|-----------------------------------------|")

def desarrolloDelPunto(num):
    print("\n_________________________________________")
    print(f"|Desarrollo del punto {num}:                |")
    print("------------------------------------------")

def menuVolverAEjecutar():
    print("|-----------------------------------------|")
    print("1. Ejecutar codigo nuevamente")
    print("0. Volver")
    print("|_________________________________________|")

#FUNCIONES GENERALES

def leerVector():
    cd = int(input("Ingrese la cantidad de datos-> "))
    v=[]
    for i in range(cd):
        v.append(int(input(f"Dato {i+1}: ")))
    return v

def leerMatriz():
    nf = int(input("Numero de filas-> "))
    nc = int(input("Numero de columnas-> "))
    m=[]
    for i in range(nf):
        f=[]
        for j in range(nc):
            f.append(int(input(f"Digite el dato ({i},{j})-> ")))
        m.append(f)
    return m
def matrizCuadrada():
    cd = int(input("Orden de la matriz cuadrada: "))
    m=[]
    for i in range(cd):
        f=[]
        for j in range(cd):
            f.append(int(input(f"Digite el dato {i},{j}: ")))
        m.append(f)
    return m,cd
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)
def dimensionMatriz(m):
    nf = len(m)
    nc = len(m[0])
    return nf,nc
def dimensionMatrices(m1,m2):
    nf1 = len(m1)
    nc1 = len(m1[0])
    nf2 = len(m2)
    nc2 = len(m2[0])
    return nf1,nc1,nf2,nc2
def fibonacci(num):
    a=0
    b=1
    t=0
    while(t<num):
        t=a+b
        a=b
        b=t
    if t==num:
        return True
    else:
        return False
def primo(num):
    c=2
    b=0
    while c<num and b==0:
        if num % c == 0:
            b=1
        c+=1
    if b==0:
        return True
    else:
        return False
def primosConsecutivos(n,m):
    b=0
    if n<m:
        for i in range(n+1,m):
            if primo(i):
                b=1
        if b==0:
            return True 
        else: 
            return False
    else:
        for i in range(m+1,n):
            if primo(i):
                b=1
        if b==0:
            return True 
        else: 
            return False
def factorial(num):
    r=1
    for i in range(1,num+1):
        r*=i
    return r
def encontrarNumeroEnVector(v,num):
    cd = len(v)
    b=0
    i=0
    while i<cd and b==0:
        if num==v[i]:
            b=1
        i+=1
    if b==1:
        return True
    else:
        return False

def encontrarFibonacciNumeroN(v,n):
    cd = len(v)
    c=0
    for i in range(cd):
        if fibonacci(v[i]):
            c+=1
            if c==n:
                nf= v[i]
                pf= i
    if c<n:
        return -1,-1
    else: 
        return nf,pf
def numeroEnUnaMatriz(m,num):
    b = 0
    i = 0
    nf,nc = dimensionMatriz(m)
    while i<nf and b==0:
        j = 0
        while j<nc and b==0:
            if num==m[i][j]:
                b=1
            j+=1
        i+=1
    if b==0:
        return False
    else:
        return True
def intercambiarDatos(v,p1,p2):
    aux = v[p1]
    v[p1] = v[p2]
    v[p2] = aux
def intercambiarDatosMatriz(m,f1,c1,f2,c2):
    aux = m[f1][c1]
    m[f1][c1] = m[f2][c2]
    m[f2][c2] = aux
def ordenarAscedentemente(v):
    cd = len(v)
    for i in range(cd-1):
        for j in range(i+1,cd):
            if v[i]>v[j]:
                intercambiarDatos(v,i,j)
def ordenarDescendentemente(v):
    cd = len(v)
    for i in range(cd-1):
        for j in range(i+1,cd):
            if v[i]<v[j]:
                intercambiarDatos(v,i,j)

#TALLERES Y EVALUACIONES
#TALLER 1
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

#TALLER 2

def taller2Punto1():
    v = leerVector()
    x=0
    z=0
    v1=[]
    v2=[]
    for i in v:
        if i%2==0:
            v1.append(i)
            x+=1
        if primo(i):
            v2.append(i)
            z+=1
    ordenarAscedentemente(v1)
    ordenarDescendentemente(v2)
    print(f"Vector con los numeros pares ordenados ascendentemente:{v1}")
    print(f"Vector con los numeros primos ordenados descendentemente:{v2}")

def taller2Punto2():
    v= leerVector()
    cd = len(v)
    n=0
    i=0
    while n<cd:
        c=0
        while i<cd and v[n]==v[i]:
            c+=1
            i+=1
        print(f"El numero {v[n]} se repite {c} veces.")
        n=i

def taller2Punto3():
    v = leerVector()
    cd = len(v)
    cd2 = 0 
    for i in v:
        cd2+=i
    v2=[]
    print("Vector 2")
    for i in range(cd2):
        v2.append(int(input(f"Ingrese dato {i}: ")))
    x=0
    for i in range(cd):
        b=0
        a=0
        for j in range(v[i]):
            if b==0:
                num_may = v2[x]
                num_men = v2[x]
                b = 1
            else:
                if v2[x]>num_may:
                    num_may = v2[x]
                if v2[x]<num_men:
                    num_men = v2[x]
            a = a + v2[x]
            x += 1
        pt = a / v[i]
        print("---------------------------------")
        print(f"Rango numero {i+1}")
        print(f'Numero mayor: {num_may}')
        print(f'Numero menor: {num_men}')
        print(f"Promedio: {pt}")

def taller2Punto4():
    v1 = leerVector()
    v2 = leerVector()
    vp = []
    for i in v1:
        if primo(i):
            if encontrarNumeroEnVector(v2,i):
                if encontrarNumeroEnVector(vp,i)==False:
                    vp.append(i)
    print(f"Primos comunes: {vp}")

def taller2Punto5():
    v1 = leerVector()
    v2 = leerVector()
    vf = []
    for i in v1:
        if fibonacci(i):
            if encontrarNumeroEnVector(vf,i)==False:
                vf.append(i)
    for i in v2:
        if fibonacci(i):
            if encontrarNumeroEnVector(vf,i)==False:
                vf.append(i)
    print(f"Union de los fibonacci sin repetidos: {vf}")

def taller2Punto6():
    print("Vector con datos ascendentes")
    a = leerVector()
    print("Vector con datos descendentes")
    b = leerVector()
    c = []
    da= len(a)
    db= len(b)
    i = da-1
    j = 0
    while j<db and i>=0:
        if a[i]>b[j]:
            c.append(a[i])
            i-=1
        else:
            c.append(b[j])
            j+=1
    if j<db:
        while j<db:
            c.append(b[j])
            j+=1
    if i>=0:
        while i>=0:
            c.append(a[i])
            i-=1
    print(f"Vector descendente por mezcla: {c} ")

def taller2Punto7():
    print("Vector con datos ascendentes")
    a = leerVector()
    print("Vector con datos descendentes")
    b = leerVector()
    c = []
    da= len(a)
    db= len(b)
    i = da-1
    j = 0
    while j<db and i>=0:
        if a[i]>b[j]:
            if a[i]%2==0:
                c.append(a[i])
            i-=1
        else:
            if b[j]%2==0:
                c.append(b[j])
            j+=1
    if j<db:
        while j<db:
            if b[j]%2==0:
                c.append(b[j])
            j+=1
    if i>=0:
        while i>=0:
            if a[i]%2==0:
                c.append(a[i])
            i-=1
    print(f"Vector pares descendente por mezcla: {c} ")
def taller2Punto8():
    v = leerVector()
    cd = len(v)
    vp = []
    bf = 0
    for i in range(cd):
        if fibonacci(v[i]):
            if bf==0:
                fib_may = v[i]
                fib_men = v[i]
                bf = 1
            else: 
                if v[i]>fib_may:
                    fib_may = v[i]
                if v[i]<fib_men:
                    fib_men = v[i]
    if fib_men>fib_may:
        for i in range(fib_may+1,fib_men):
            if primo(i):
                vp.append(i)
    else:
        for i in range(fib_men+1,fib_may):
            if primo(i):
                vp.append(i)
    print(f"Fibonacci mayor: {fib_may}")
    print(f"Fibonacci menor: {fib_men}")
    print(f"Vector primos que estan entre el fibonacci mayor y menor: {vp}")

def taller2Punto9():
    v=leerVector()
    f2,p2 = encontrarFibonacciNumeroN(v,2)
    f3,p3 = encontrarFibonacciNumeroN(v,3)
    c = 0
    a = 0
    if f2<f3:
        for i in range(f2+1,f3):
            if i%3==0:
                a+=i
                c+=1
    else:
        for i in range(f3+1,f2):
            if i%3==0:
                a+=i
                c+=1
    pt = a/c
    print(f"Fibonacci numero 2: {f2}")
    print(f"Fibonacci numero 3: {f3}")
    print(f"Promedio total: {pt}")

def taller2Punto10():
    v = leerVector()
    f2,p2 = encontrarFibonacciNumeroN(v,2)
    f3,p3 = encontrarFibonacciNumeroN(v,3)
    if f2<f3:
        f = f2
    else: 
        f = f3
    fm = factorial(f)
    v[p2] = fm
    v[p3] = fm
    print(f"Vector resultante: {v}")

#TALLER 3
def taller3Punto1():
    m,cd= matrizCuadrada()
    nf = len(m)
    v = []
    for i in range(nf):
        for j in range(nf):
            if i==j or i+j==nf-1:
                if primo(m[i][j]):
                    v.append(m[i][j])
    print(f'Vector con los primos de las diagonales: {v}')

def taller3Punto2():
    m,nf = matrizCuadrada()
    aPar = 0
    cPar = 0
    aImp = 0
    cImp = 0
    for i in range(nf):
        for j in range(nf):
            if i==j:
                if m[i][j]%2==0:
                    aPar+=m[i][j]
                    cPar+=1
            if i-j>0:
                if m[i][j]%2==1:
                    aImp+=m[i][j]
                    cImp+=1
    pPar = aPar/cPar
    pImp = aImp/cImp
    print(f'Promedio pares: {pPar}')
    print(f'Promedio impares: {pImp}')
    if pPar>pImp:
        print(f'El promedio de los pares es mayor que el de los impares')
    else:
        if pPar==pImp:
            print(f'El promedio de pares e impares es el mismo')
        else:
            print(f'El promedio de los impares es mayor que el de los pares')

def taller3Punto3():
    m = leerMatriz()
    nf,nc = dimensionMatriz(m)
    c=0
    for j in range(nc):
        for i in range(nf):
            if primo(m[i][j]):
                c+=1
                if c==2:
                    p2=m[i][j]
                if c==4:
                    p4=m[i][j]
    print(f'Primo numero 2: {p2}')
    print(f'Primo numero 4: {p4}')
    if primosConsecutivos(p2,p4):
        print(f'Los primos son consecutivos.')
    else:
        print(f'Los primos no son consecutivos.')

def taller3Punto4():
    m = leerMatriz()
    nf,nc = dimensionMatriz(m)
    for j in range(nc):
        for i in range(nf):
            for q in range(i+1,nf):
                if j%2==0:
                    if m[i][j]>m[q][j]:
                        intercambiarDatosMatriz(m,i,j,q,j)
                else:
                    if m[i][j]<m[q][j]:
                        intercambiarDatosMatriz(m,i,j,q,j)
    print("Matriz ordenada")
    imprimir_matriz(m)

#Punto 5
def taller3Punto5():
    matriz_1 = []
    matriz_2 = []
    vector = []
    print("Datos ascendentes de la matriz 1:")
    matriz_1 = leerMatriz()
    print("Datos ascendentes de la matriz 2:")
    matriz_2 = leerMatriz()
    filas_1,columnas_1,filas_2,columnas_2 = dimensionMatrices(matriz_1,matriz_2)
    print("Matriz 1: ", matriz_1, " Matriz 2: ", matriz_2)
    i = 0  # filas matriz 1
    j = 0  # columnas matriz 1
    z = 0  # filas matriz 2
    x = 0  # columnas matriz 2
    while i < filas_1 or z < filas_2:
        if i == filas_1:
            vector += matriz_2[z][x:]
            break
        elif z == filas_2:
            vector += matriz_1[i][j:]
            break
        elif matriz_1[i][j] < matriz_2[z][x]:
            vector.append(matriz_1[i][j])
            j += 1
            if j == columnas_1:
                j = 0
                i += 1
        else:
            vector.append(matriz_2[z][x])
            x += 1
            if x == columnas_2:
                x = 0
                z += 1
    print("Vector ordenado por mezcla: ", vector)
#Punto 6
def taller3Punto6():
    m1 = leerMatriz()
    nf,nc = dimensionMatriz(m1)
    imprimir_matriz(m1)
    promedios = []
    for i in range(nf):
        suma = sum(m1[i])
        promedio = suma / nc
        print(f'Promedio fila {i} = {promedio}')
        promedios.append(promedio)
    for i in range(nf-1):
        for j in range(i+1,nf):
            if promedios[i]>promedios[j]:
                m1[i],m1[j]=m1[j],m1[i]
                promedios[i],promedios[j]=promedios[j],promedios[i]
    print("Matriz con filas intercambiadas por promedios ascendentes: ")
    imprimir_matriz(m1)
#Punto 7 
def taller3Punto7_1():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    for i in range(nf):
        aux = m[i][0]
        m[i][0] = m[i][nc-1]
        m[i][nc-1] = aux
    print(f"Matriz intercambiada columna inicial y final:")
    imprimir_matriz(m)

def taller3Punto7_2():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    for j in range(nc):
        b=0
        a=0
        c=0
        for i in range(nf):
            if b==0:
                may= m[i][j]
                men = m[i][j]
                b=1
            else:
                if m[i][j]>may:
                    may=m[i][j]
                if m[i][j]<men:
                    men=m[i][j]
            a+=m[i][j]
        print(f"Columna:{j}, Mayor:{may},Menor:{men},Promedio:{a/nc}")

def taller3Punto7_3():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    for i in range(nf):
        if i%2==0:
            for j in range(nc-1):
                for k in range(j+1,nc):
                    if m[i][j]>m[i][k]:
                        aux = m[i][j]
                        m[i][j] = m[i][k]
                        m[i][k] = aux
        else:
            for j in range(nc-1):
                for k in range(j+1,nc):
                    if m[i][j]<m[i][k]:
                        aux = m[i][j]
                        m[i][j] = m[i][k]
                        m[i][k] = aux
    print("Matriz ordenada")
    imprimir_matriz(m)

def taller3Punto7_4():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    for i in range(nf):
        for j in range(nc):
            for p in range(nf):
                for q in range(nc):
                    if m[p][q]<m[i][j]:
                        aux = m[i][j]
                        m[i][j] = m[p][q]
                        m[p][q] = aux
    print("Matriz ordenada")
    imprimir_matriz(m)

def taller3Punto7_5():
    m = leerMatriz()
    imprimir_matriz(m)
    nf,nc = dimensionMatriz(m)
    may = m[0][0]
    men = m[0][0]
    Fmay = 0 
    Fmen = 0
    for i in range(nf):
        for j in range(nc):
            if m[i][j] > may:
                may = m[i][j]
                Fmay = i 
            if m[i][j]< men:
                men = m[i][j]
                Fmen = i
    for j in range(nc):
        aux = m[Fmay][j]
        m[Fmay][j] = m[Fmen][j]
        m[Fmen][j] = aux
    print(f'Numero mayor {may} en fila {Fmay}')
    print(f'Numero menor {men} en fila {Fmen}')
    print("Matriz nueva:")
    imprimir_matriz(m)

def taller3Punto7_6():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    cf = 0 
    bf = 0
    f2 = -1
    f4 = -1
    for i in range(nf):
        for j in range(nc):
            if fibonacci(m[i][j]):
                if bf==0:
                    cf=1
                    bf=1
                else:
                    cf+=1
                    if cf==2:
                        f2 = i
                    if cf==4: 
                        f4 = i
    if f2==-1 or f4==-1:
        print("No existen los fibonacci solicitados.")
    else:
        for j in range(nc):
            aux = m[f2][j]
            m[f2][j] = m[f4][j]
            m[f4][j] = aux
    print("Matriz intercambiando la fila del fibonacci 2 y 4:")
    imprimir_matriz(m)

def taller3Punto7_7():
    m = leerMatriz()
    imprimir_matriz(m)
    nf = len(m)
    nc = len(m[0])
    bp = 0
    bf = 0 
    ff = -1
    fp = -1
    for i in range(nf):
        for j in range(nc):
            if primo(m[i][j]):
                if bp==0:
                    fp = i
                    pmay = m[i][j]
                    bp = 1
                else:
                    if m[i][j]>pmay:
                        pmay=m[i][j]
                        fp=i
            if fibonacci(m[i][j]):
                if bf==0:
                    ff=i
                    fmen = m[i][j]
                    bf=1
                else:
                    if m[i][j]<fmen:
                        fmen = m[i][j]
                        ff=i
    if ff==-1 or fp==-1:
        print("No existen numeros primos o fibonacci")
    else:
        for j in range(nc):
            aux = m[ff][j]
            m[ff][j] = m[fp][j]
            m[fp][j] = aux
    print("Matriz intercambiando fila del primo mayor y fibonacci menor: ")
    imprimir_matriz(m)

def taller3Punto7_8():
    m = leerMatriz()
    nf = len(m)
    nc = len(m[0])
    cp = 0
    p2 = -1
    p4 = -1 
    for i in range(nf):
        for j in range(nc):
            if primo(m[i][j]):
                cp += 1
                if cp==2:
                    p2 = m[i][j]
                if cp==4:
                    p4 = m[i][j]
    if p2==-1 or p4==-1:
        print("No existen los primos requeridos.")
    else:
        if primosConsecutivos(p2,p4):
            print(f"Los primos 2 y 4 son consecutivos:{p2},{p4} ")
        else: 
            print(f"Los primos 2 y 4 no son consecutivos:{p2},{p4}")

def taller3punto8_1():
    m,cd = matrizCuadrada()
    a1=0
    a2=0
    for i in range(cd):
        for j in range(cd):
            if i==j:
                a1 += m[i][j]
            if i+j == cd-1:
                a2 += m[i][j]
    promP = a1/cd
    promS = a2/cd
    print(f"El promedio de la diagonal principal es: {promP}")
    print(f"El promedio de la diagonal segundaria es: {promS}")

def taller3punto8_2():
    m,cd = matrizCuadrada()
    imprimir_matriz(m)
    for i in range(cd-1):
        for j in range(i+1,cd):
            if m[i][i] > m[j][j]:
                intercambiarDatosMatriz(m,i,i,j,j)
    print("Matriz ordenada")
    imprimir_matriz(m)

def taller3punto8_3():
    m,cd = matrizCuadrada()
    imprimir_matriz(m)
    ap=0
    cp=0
    ai=0
    ci=0
    for i in range(cd):
        for j in range(cd):
            if j-i>0:
                if m[i][j]%2==0:
                    ap+=m[i][j]
                    cp+=1
            if i+j==cd-1:
                if m[i][j]%2==1:
                    ai+=m[i][j]
                    ci+=1
    print(f'El promedio de los pares encima de la diagonal principal es: {ap/cp}')
    print(f'El promedio de los impares en la diagonal secundaria es: {ai/ci}')

def taller3punto8_4():
    m,cd = matrizCuadrada()
    bf=0
    bp=0 
    for i in range(cd):
        for j in range(cd):
            if fibonacci(m[i][j]):
                if bf==0:
                    fmay = m[i][j]
                    bf=1
                else: 
                    if m[i][j]>fmay:
                        fmay = m[i][j]
            if primo(m[i][j]):
                if bp==0:
                    pmen = m[i][j]
                    bp=1
                else: 
                    if m[i][j]<pmen:
                        pmen = m[i][j]
    for i in range(cd):
        for j in range(cd):
            if i==j:
                m[i][j] = pmen
            if i+j==cd-1:
                m[i][j] = fmay
    print(f"Fibonacci mayor: {fmay}")
    print(f"Primo menor: {pmen}")
    imprimir_matriz(m)

def taller3punto8_5():
    m,cd = matrizCuadrada()
    bp=0
    bi=0
    for i in range(cd):
        for j in range(cd):
            if m[i][j] % 2 == 0:
                if bp ==0:
                    pmay = m[i][j]
                    bp=1
                else:
                    if m[i][j]>pmay:
                        pmay=m[i][j]
            else: 
                if bi ==0:
                    imen = m[i][j]
                    bi=1
                else:
                    if m[i][j]<imen:
                        imen=m[i][j]
    for i in range(cd):
        for j in range(cd):
            if i==0 or i==cd-1 or j==0 or j==cd-1:
                m[i][j]= pmay
            else:
                m[i][j]= imen
    imprimir_matriz(m)

def taller3Punto9_1():
    print("Matriz 1")
    m1=leerMatriz()
    print("Matriz 2")
    m2=leerMatriz()
    nf1,nc1,nf2,nc2 = dimensionMatrices(m1,m2)
    v=[]
    for i in range(nf1):
        for j in range(nc1):
            b=0
            b2=0
            for k in range(nf2):
                for l in range(nc2):
                    if m1[i][j]==m2[k][l]:
                        b=1
                    if b==1:
                        for d in v:
                            if m1[i][j]==d:
                                b2=1
                        if b2==0:
                            v.append(m1[i][j])
    print(f'Vector con los elementos comunes: {v}')

def taller3Punto9_2():
    print("Matriz 1")
    m1=leerMatriz()
    print("Matriz 2")
    m2=leerMatriz()
    nf1,nc1,nf2,nc2 = dimensionMatrices(m1,m2)
    v=[]
    for i in range(nf1):
        for j in range(nc1):
            if primo(m1[i][j]):
                b=0
                b2=0
                for k in range(nf2):
                    for l in range(nc2):
                        if m1[i][j]==m2[k][l]:
                            b=1
                        if b==1:
                            for d in v:
                                if m1[i][j]==d:
                                    b2=1
                            if b2==0:
                                v.append(m1[i][j])
    print(f'Vector con los primos comunes: {v}')

def taller3Punto9_3():
    print("Matriz 1")
    m1=leerMatriz()
    print("Matriz 2")
    m2=leerMatriz()
    nf1,nc1,nf2,nc2 = dimensionMatrices(m1,m2)
    v=[]
    for i in range(nf1):
        for j in range(nc1):
            if primo(m1[i][j]):
                b=0
                b2=0
                for k in range(nf2):
                    for l in range(nc2):
                        if m1[i][j]==m2[k][l]:
                            b=1
                if b==0:
                    for d in v:
                        if m1[i][j]==d:
                            b2=1
                    if b2==0:
                        v.append(m1[i][j])
    for k in range(nf2):
        for l in range(nc2):
            b=0
            b2=0
            if primo(m2[k][l]):
                for i in range(nf1):
                    for j in range(nc1):
                        if m2[k][l]==m1[i][j]:
                            b=1
                if b==0:
                    for d in v:
                        if m2[k][l]==d:
                            b2=1
                    if b2==0:
                        v.append(m2[k][l])
    print(f'Vector con los primos no comunes: {v}')

def taller3Punto10():
    m=leerMatriz()
    nf = len(m)
    nc = len(m[0])
    n = []
    c = []
    v = []
    vn = []
    for i in range(nf):
        for j in range(nc):
            b=0
            d = 0
            while d<len(n) and b==0:
                if m[i][j]==n[d]:
                    b=1
                else:
                    d+=1
            if b==0:
                n.append(m[i][j])
                c.append(1)
            else:
                c[d]+=1
    for i,j in zip(c,n):
        if fibonacci(i):
            if encontrarNumeroEnVector(v,i)==False:
                v.append(i)
                vn.append(j)
    print(f"El vector de los contadores fibonacci es: {v}")
    # for i,j in zip(v,vn):
    #     print(f"El numero es {j}, y su contador es {i}")

#PARCIAL 1  
def Parcial1_Punto1():
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

def Parcial1_Punto2():
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


def Parcial1_Punto3():
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


def Parcial1_Punto4():
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

#PARCIAL 2

def Parcial_2_ejercicio_1():
    num = int(input('Escriba un numero:'))
    b = 0
    while num!=-5:
        c=0
        n=num
        while n==num:
            c+=1
            num = int(input('Escriba un numero:'))
        if b==0:
            cm=c
            cmen=c
            b=1
        else:
            if c>cm:
                cm=c
            if c<cmen:
                cmen=c
    r = 0
    for i in range(cmen):
        r+=cm
    print(f"La multiplicacion con sumas del contador mayor y menor es: {r} ")

def Parcial_2_ejercicio_2():
    print("Vector 1: ")
    a = leerVector()
    cd = len(a)
    print("Vector 2: ")
    b = leerVector()
    cdb = len(b)
    v1=[]
    v2=[]
    for i in (a):
        if fibonacci(i):
            if encontrarNumeroEnVector(b,i)==False:
                if encontrarNumeroEnVector(v1,i)==False:
                    v1.append(i)
        if i%3==0:
            if encontrarNumeroEnVector(b,i):
                if i%5!=0:
                    v2.append(i)
    for i in (b):
        if fibonacci(i):
            if encontrarNumeroEnVector(a,i)==False:
                if encontrarNumeroEnVector(v1,i)==False:
                    v1.append(i)
    print(f'Vector diferencia simetrica de los fibonacci: {v1}')
    print(f'Vector multiplos de 3 y no multiplos de 5 comunes: {v2}')

def Parcial_2_ejercicio_3():
    print("Vector 1: ")
    v1 = leerVector()
    cd1 = len(v1)
    print("Vector 2: ")
    v2 = leerVector()
    cd2 = len(v2)
    nf,pf = encontrarFibonacciNumeroN(v1,3)
    if nf==-1:
        print("No existe el numero de fibonaccis requeridos.")
    else:
        if nf>cd2:
            print('La cantidad de datos del vector 2 es menor que el numero fibonacci')
        else:
            for i in range(nf-1):
                for j in range(i+1,nf):
                    if v2[i]>v2[j]:
                        intercambiarDatos(v2,i,j)
            for i in range(nf,cd2-1):
                for j in range(i+1,cd2):
                    if v2[i]<v2[j]:
                        intercambiarDatos(v2,i,j)
            print(f"Vector resultante: {v2}")

def Parcial_2_ejercicio_4():
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
    print("Matriz:")
    for fila in matriz:
        print(fila)

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

    for fila in matriz:
        print(fila)

#MENU 
opcion = 1
while opcion != 0:
    print('''|-----------------------------------------|
|            INICIO                       |
|1. Taller 1                              |
|2. Taller 2                              |
|3. Taller 3                              |
|4. Parciales                             |
|-----------------------------------------|
|0. Finalizar                             |
|-----------------------------------------|''')
    opcion = input('Digite la opcion-> ')
    print('-----------------------------------------')
    match opcion:
        case "1":
            taller1 = 10 
            while taller1 != 0:
                menuPuntos("Taller 1",5,"Volver al inicio")
                taller1 = input('Digite la opcion-> ')
                match taller1:
                    case "1":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(1)
                                Taller1_punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "2":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(2)
                                Taller1_punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "3":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(3)
                                Taller1_punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "4":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(4)
                                Taller1_punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "5":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(5)
                                Taller1_punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "0":
                        taller1 = 0
                    case _:
                        print("Opcion no valida")
        case "2":
            taller2 = 1
            while taller2 != 0:
                menuPuntos("Taller 2",10,"Volver al inicio")
                taller2 = input('Digite la opcion-> ')
                match taller2:
                    case "1":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(1)
                                taller2Punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "2":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(2)
                                taller2Punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "3":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(3)
                                taller2Punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "4":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(4)
                                taller2Punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "5":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(5)
                                taller2Punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "6":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(6)
                                taller2Punto6()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "7":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(7)
                                taller2Punto7()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "8":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(8)
                                taller2Punto8()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "9":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(9)
                                taller2Punto9()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "10":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(10)
                                taller2Punto10()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "0":
                        taller2 = 0
                    case _:
                        print("Opcion no valida")
        case "3":
            taller3 = 1
            while taller3 != 0:
                menuPuntos("Taller 3",10,"Volver al inicio")
                taller3 = input('Digite la opcion:')
                match taller3:
                    case "1":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(1)
                                taller3Punto1()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "2":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(2)
                                taller3Punto2()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "3":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(3)
                                taller3Punto3()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "4":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(4)
                                taller3Punto4()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "5":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(5)
                                taller3Punto5()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "6":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(6)
                                taller3Punto6()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "7":
                        p=1 
                        while p !=0 :
                            menuPuntos("Taller 3, punto 7",8,"Volver")
                            p = input('Digite su opcion->')
                            match p:
                                case "1":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(1)
                                            taller3Punto7_1()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "2":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(2)
                                            taller3Punto7_2()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "3":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(3)
                                            taller3Punto7_3()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "4":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(4)
                                            taller3Punto7_4()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "5":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(5)
                                            taller3Punto7_5()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "6":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(6)
                                            taller3Punto7_6()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "7":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(7)
                                            taller3Punto7_7()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "8":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(8)
                                            taller3Punto7_8()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "0":
                                    p=0
                                case _:
                                    print("\nOPCION NO VALIDA")
                    case "8":
                        p=1 
                        while p !=0 :
                            menuPuntos("Taller 3, Punto 8",5,"Volver")
                            p = input('Digite su opcion->')
                            match p:
                                case "1":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(1)
                                            taller3punto8_1()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "2":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(2)
                                            taller3punto8_2()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "3":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(3)
                                            taller3punto8_3()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "4":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(4)
                                            taller3punto8_4()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "5":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(5)
                                            taller3punto8_5()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "0":
                                    p=0
                                case _:
                                    print("\nOPCION NO VALIDA")
                    case "9":
                        p=1 
                        while p !=0 :
                            menuPuntos("Taller 3, Punto 9",3,"Volver")
                            p = input('Digite su opcion->')
                            match p:
                                case "1":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(1)
                                            taller3Punto9_1()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "2":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(2)
                                            taller3Punto9_2()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "3":
                                    v=1
                                    while v!=0:
                                        if (v==1):
                                            desarrolloDelPunto(3)
                                            taller3Punto9_3()
                                            menuVolverAEjecutar()
                                        else:
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        v=int(input("Digite su opcion-> "))
                                case "0":
                                    p=0
                                case _:
                                    print("\nOPCION NO VALIDA")
                    case "10":
                        p=1 
                        while p !=0 :
                            if (p==1):
                                desarrolloDelPunto(10)
                                taller3Punto10()
                                menuVolverAEjecutar()
                            else: 
                                print("\nOPCION NO VALIDA")
                                menuVolverAEjecutar()
                            p=int(input("Digite su opcion-> "))
                    case "0":
                        taller3 = 0
                    case _:
                        print("\n OPCION NO VALIDA")
        case "4":
            parcial = -1
            while parcial != 0:
                menuParciales("Parciales",2,"Volver al inicio")
                parcial=input("Digite su opcion-> ")
                match parcial:
                    case "1":
                        parcial1 = 1
                        while parcial1 != 0:
                            menuPuntos("Parcial 1",4,"Volver")
                            parcial1 = input('Digite la opcion->')
                            match parcial1:
                                case "1":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(1)
                                            Parcial1_Punto1()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "2":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(2)
                                            Parcial1_Punto2()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "3":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(3)
                                            Parcial1_Punto3()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "4":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(4)
                                            Parcial1_Punto4()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "0":
                                    parcial1 = 0
                                case _:
                                    print("Opcion no valida")
                    case "2":
                        parcial2 = 1
                        while parcial2 != 0:
                            menuPuntos("Parcial 2",4,"Volver")
                            parcial2 = input('Digite la opcion->')
                            match parcial2:
                                case "1":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(1)
                                            Parcial_2_ejercicio_1()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "2":
                                    p=1 
                                    while p !=0 :
                                        if (p==1):
                                            desarrolloDelPunto(2)
                                            Parcial_2_ejercicio_2()
                                            menuVolverAEjecutar()
                                        else: 
                                            print("\nOPCION NO VALIDA")
                                            menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "3":
                                    p=1
                                    while p !=0 :
                                        desarrolloDelPunto(3)
                                        Parcial_2_ejercicio_3()
                                        menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "4":
                                    p=1 
                                    while p !=0 :
                                        desarrolloDelPunto(4)
                                        Parcial_2_ejercicio_4()
                                        menuVolverAEjecutar()
                                        p=int(input("Digite su opcion-> "))
                                case "0":
                                    parcial2 = 0
                                case _:
                                    print("Opcion no valida")
                    case "0":
                        parcial = 0
                    case _:
                        print('Opcion no valida')
        case "0":
            opcion = 0 
        case _:
            print('Opcion no valida')