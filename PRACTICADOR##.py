def leer_matriz():
    matriz_1 = []
    filas = int(input("Número de filas= "))
    columnas = int(input("Número de columnas= "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila)
    print(matriz_1)    
    return matriz_1   #obligatorio el "return" paara salir de la funcion con exito y guardar lo que queremos utilizar

def calculo_primos(valor):  #en "valor" se reemplaza lo que nosotros queramos, en este caso la "matriz_1"
    suma = 0
    contador = 0
    siprimo = 0
    for i in range(len(valor)):
        for j in range(len(valor[i])):
            c = 1
            div = 0
            while c <= valor[i][j]:
                if valor[i][j] % c == 0:
                    div += 1
                c += 1
            if div == 2:
                siprimo += 1
                print(valor[i][j], "Es primo")
                suma += valor[i][j]
                contador += 1 

    promedio = suma / contador
    print("Promedio de los primos de la matriz:", promedio)
    return int(promedio) #return de la accion que se realizo y que queremos guardar

def promedio_fibo(valor):
    a=0
    b=1
    t=0
    while t<valor:
        t=a+b
        a=b
        b=t
    if valor==t:
        print("El promedio ",valor," es fibonacci")
    else:
        print("El promedio ",valor," No es fibonacci")

    return valor                     


#matriz = leer_matriz() #La línea (matriz = leer_matriz()) obtiene la matriz ingresada por el usuario y la almacena en la variable matriz.
                       #siempre debem asignarse los valores que se obtuvieron a una variable, esto para segur siendo utilizadas  
#promedio_primos = calculo_primos(matriz) #calcula el promedio de los números primos en la matriz utilizando la función calculo_primos(),
                                         # pasando la matriz como argumento, y almacena este promedio en la variable promedio_primos.
#si_fue_fibo= promedio_fibo(promedio_primos) 

while True:
    print("===menu===\n")
    print("opcion 1: (leer matriz)\n","Opcion 2: (calcular el promedio de los primos)\n","Opcion 3: (ver si el promedio es fibonacci)\n")
    opcion=int(input("inggrese el punto "))
    if opcion==1:
        leer_matriz()
    elif opcion==2:
        matriz = leer_matriz()
        promedio_primos = calculo_primos(matriz)
    elif opcion==3:
        matriz = leer_matriz()
        promedio_primos = calculo_primos(matriz)
        promedio_fibo(promedio_primos)
    else:
        print("Opcion no registrada")
        break

nuevo=int(input("Cambio nuevo en github jaja"))
if nuevo==1:
    print("Si funciono")
else:
    print("No funciono")    