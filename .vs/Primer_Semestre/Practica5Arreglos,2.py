#Las siguientes apliaciones funcionan solo con vectores ordenados
#Insertar un dato en la posicion que corresponda de manera que el vector siga ordenado
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

dato=int(input("Dato a insertar= "))
i=0
b=0
while i<=cantidad_datos-1 and b==0:
    if a[i]>=dato:
        b=1
        pos=i
    else:
        i+=1

if b==1:
    a.insert(pos,dato)
else:
    a.insert(cantidad_datos,dato)

for i in range(len(a)):
    print("Dato: ",i," = ",a[i])

#Insertar un dato en un vector desordenado y despues ordenarlo
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

dato=int(input("Dato a insertar"))
a.insert(0,dato)
a.sort()
print(a)

#Eliminar un dato de una lista ordenada o desordenada
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

dato=int(input("Dato a insertar"))
if (dato in a)==True:
    a.remove(dato)
else:
    print("El dato no existe en la lista")

for i in range (len(a)):
    print("Dato: ",i," = ",a[i])

#Busqueda binaria(sirve solo si los datos estan ordenados)
cantidad_datos=int(input("Cantidad de datos= "))
a=[]
for i in range(cantidad_datos):
    a.append(int(input("Dato({})=".format(i))))

dato_buscar=int(input("Dato a buscar= "))
limite_inferior=0
limite_superior=cantidad_datos-1
b=0
while limite_inferior<=limite_superior and b==0:
    medio=int((limite_inferior+limite_superior)/2)
    if a[medio]==dato_buscar:
        b=1
    else:
        if dato_buscar<a[medio]:
            limite_superior=medio-1
        else:
            limite_inferior=medio+1

if b==1:
    print("Dato a buscar: ",dato_buscar,"Se encuentra en la posicion",medio)
else:
    print("Dato a buscar: ",dato_buscar,"no se encuentra en la lista")

#Busqueda por mezcla(Este funciona teniendo dos vectores ordenados)
cantidad_datos_a=int(input("Cantidad de datos en vector 1="))
a=[]
b=[]
c=[]
for i in range(cantidad_datos_a):
    a.append(int(input("Dato({})=".format(i))))

cantidad_datos_b=int(input("Cantidad de datos en vector 2="))
for i in range(cantidad_datos_b):
    b.append(int(input("Dato({})=".format(i))))

i=0
j=0
while i<cantidad_datos_a and j<cantidad_datos_b:
    if a[i]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

#Esto es por si termino uno antes que otro
if i==cantidad_datos_a:
    while j<cantidad_datos_b:
        c.append(b[j])
        j+=1
else:
    while i<cantidad_datos_a:
        c.append(a[i])
        i+=1

print("Vector ordenado por mezcla:")
for i in range(len(c)):
    print("Posicion: ",i,"Dato= ",c[i])

##LISTA DE RANGOS CON DATOS
datos=[]
rango=[]
v_mayor=[]
cantidad_datos_rango=int(input("Cantidad de datos de la lista de rango="))
cantidad_datos_lista=int(input("Cantidad de elementos de la lista datos="))
#leer lista rango
for i in range(cantidad_datos_rango):
    rango.append(int(input("Digitar valor rango({})=".format(i))))

#Leer lisra datos
for j in range(cantidad_datos_lista):
    datos.append(int(input("Digitar valor dato({})=".format(j))))

i=0
j=0
while i<cantidad_datos_rango:
    limite_final=j+rango[i]-1
    mayor=datos[j]
    while j<=limite_final:
        if datos[j]>mayor:
            mayor=datos[j]
        j+=1

    v_mayor.append(mayor)
    i+=1

print("Mayores de cada rango:")
for i in range(len(v_mayor)):
    print("Rango:",i,"mayor:",v_mayor[i])    

###Ejercicio combinatorio de todo
cantidad_estudiantes=int(input("Cantidad de estudiantes:"))
codigo=[]
nota_final=[]
v_nota1=[]
v_nota2=[]
v_nota3=[]
c=0
suma_calificaciones=0
contador_calificaciones=0
while c<cantidad_estudiantes:
    calculo_nota_final=0
    codigo.append(int(input("Codigo de estudiante:")))
    print("A continuacion digite las tres notas del estudiante")
    nota1=float(input("Nota 1:"))
    v_nota1.append(nota1)
    nota2=float(input("Nota 2:"))
    v_nota2.append(nota2)
    nota3=float(input("Nota 3:"))
    v_nota3.append(nota3)
    calculo_nota_final=((nota1*0.3)+(nota2*0.3)+(nota3*0.4))
    suma_calificaciones+=calculo_nota_final
    contador_calificaciones+=1
    nota_final.append(calculo_nota_final)
    c+=1

#organizamos vector segun notas finales de mayor a menor
for i in range(len(nota_final)):
    for j in range(i+1,len(nota_final)):
        if nota_final[j]>nota_final[i]:
            #intercambiamos las notas finales para ordenarlas
            nota_final[i],nota_final[j]=nota_final[j],nota_final[i]
            #mantenemos relacion con las notas 1,2 y 3
            v_nota1[i],v_nota1[j]=v_nota1[j],v_nota1[i]
            v_nota2[i],v_nota2[j]=v_nota2[j],v_nota2[i]
            v_nota3[i],v_nota3[j]=v_nota3[j],v_nota3[i]
            #mantenemos relacion con el cogido
            codigo[i],codigo[j]=codigo[j],codigo[i]

print("Lista de estudiantes de mayor a menor nota:")
for i in range(len(nota_final)):
    print("Codigo de estudiante:",codigo[i],"Nota 1:",v_nota1[i],"Nota 2:",v_nota2[i],"Nota 3:",v_nota3[i],"Nota final=",nota_final[i])

promedio_calificaciones=suma_calificaciones/contador_calificaciones
print("El promedio de notas finales es=",promedio_calificaciones)
for i in range(len(nota_final)):
    if nota_final[i] >= 3.0:
        print("Estudiante con código:", codigo[i], "Aprueba con una nota de:", nota_final[i])
    else:
        print("Estudiante con código:", codigo[i], "No aprueba con una nota de:", nota_final[i])

print("Estudiantes con nota mayor:")
nota_mayor=nota_final[0]
print("Codigo de estudiante:",codigo[0],"nota:",nota_mayor)
i=1
b=0
while i<=len(nota_final) and b==0:
    aux=nota_mayor
    while nota_final[i]==aux:
        print("Codigo de estudiante:",codigo[i],"Nota:",nota_final[i])
        i+=1
    b+=1

print("Estudiantes con nota menor:")
nota_menor=nota_final[-1]
print("Codigo de estudiante:",codigo[-1],"nota:",nota_final[-1])
i=1
b=0
while i<=len(nota_final) and b==0:
    aux=nota_menor
    while nota_final[i]==aux:
        print("Codiigo de estudiante:",codigo[i],"nota:",nota_final[i])
        i+=1
    b+=1    

