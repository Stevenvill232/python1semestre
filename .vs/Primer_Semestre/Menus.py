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
    print("2. Seguir en el menu")
    print("0. Volver")
    print("|_________________________________________|")

opcion=1
while opcion!=0:
    print("--------MENU----------\n","Opcion 1 (Leer matriz)\n","Opcion 2 (Terminar menu)")
    opcion=input("Digite la opcion: ")
    match opcion:
        case "1":
            p=1
            while p!=0:
                if p==1:
                    matriz = leer_matriz()
                    menuVolverAEjecutar()
                    p=int(input("Digite la opcion: ")) 
                if p==2:
                    print("1. Calcular el promedio de los primos\n","2. Volver a presentar las opciones")
                    opcion=int(input("Digite la opcion: "))
                    if opcion==1:
                        promedio_primos = calculo_primos(matriz)
                    else:
                        menuVolverAEjecutar()
                        p=int(input("Digite la opcion: "))  
                        if p==2:
                            print("1. Saber si el promedio es numero fibonacci \n","2. Volver a presentar las opciones")
                            opcion=int(input("Digite la opcion: "))
                            if opcion==1:
                                si_fue_fibo= promedio_fibo(promedio_primos) 
                            else:
                                menuVolverAEjecutar()
                                p=int(input("Digite la opcion: "))
                                if p==2:
                                    print("Ha llegao al final del respectivo menu")
                                    break         
                else:
                    print("\nOpcion no valida")
                    menuVolverAEjecutar()
                    p=int(input("Digite la opcion"))   
        case "2":
            opcion=0


