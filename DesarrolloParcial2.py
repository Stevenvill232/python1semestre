####Punto 1 Parcial 2
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
####Punto 2 parcial 2
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
####Punto 3 parcial 2
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
####Punto 4 parcial 2
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