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