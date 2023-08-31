datos=int(input("Cantidad de datos= "))
c=1
promedio_par=0
contador_pares=0
promedio_impar=0
contador_impares=0
while c<=datos:
    numero=int(input("Digitar numero= "))
    if numero%2==0:
        promedio_par+=numero
        contador_pares+=1
    else:
        promedio_impar+=numero
        contador_impares+=1
    c+=1    
if contador_pares>0:
    totalpares=promedio_par/contador_pares
    print("Promedio de pares= ",totalpares) 
else:
    print("No hay pares")
if contador_impares>0:
    totalimpares=promedio_impar/contador_impares
    print("Promedio de impares= ",totalimpares)  
else:
    print("No hay impares")    