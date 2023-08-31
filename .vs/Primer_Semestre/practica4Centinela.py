#Permite la entrada de varios numeros enteros y determinar el promedio de los numeros que entran, finalizar al llegar un negativo
numero=int(input("Numero= "))
sumador=0
contador=0
while numero>0:
    sumador+=numero
    contador+=1
    numero=int(input("Numero= "))

if contador>0:
    promedio=sumador/contador
    print("Promedio= ",promedio)
else:
    print("No hay numeros positivos")    

#Rompimiento de control 
print("Rompimiento de control ")
numero = int(input("Número: "))

while numero != -5:
    aux = numero
    datos_grupo = 0

    while numero == aux:
        datos_grupo += 1
        numero = int(input("Número: "))

    print("Grupo", aux, "Veces que se repite:", datos_grupo)

print("Fin algoritmo")
#Rompimiento de control y sacar el grupo que mas se repite 2
print("Rompimiento de control y sacar el grupo que mas se repite 2")
umero=int(input("Numero= "))
grupo_mayor=0
while numero != -5:
    aux=numero
    contador_grupo=0

    while numero==aux:
        contador_grupo+=1
        numero=int(input("Numero= "))

    print("Dato= ",aux," Se repite: ",contador_grupo," Veces")
    if contador_grupo>grupo_mayor:
        grupo_mayor=contador_grupo
        dato_mayor=aux

if grupo_mayor>1:
    print("El grupo de datos ",dato_mayor,"Es el que mas veces se repite: ",grupo_mayor," Veces")
else:
    print("Todos los datos se repiten tan solo 1 vez") 

print("Fin algoritmo")

