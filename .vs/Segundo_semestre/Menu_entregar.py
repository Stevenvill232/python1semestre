import os #Para manejar lo de pausas del menu
#os.system('cls)
#os.system('pause)

def es_primo(valor):
    c=1
    div=0
    while c<=valor:
        if valor % c == 0:
            div+=1
        c+1
    if div==2:
        return True
    else:
        return False

def fibonaccis(valor):
    a=0
    b=1
    t=0
    while t<valor:
        t=a+b
        a=b
        b=t

    if valor==t:
        return True
    else:
        return False 

def leer_lista():
    lista=[]
    cantidad_datos=int(input("Cantidad de datos en el la lista: "))
    for i in range(cantidad_datos):
        lista.append(int(input(f'Dato({i})=')))
    print("lista generada segun los anteriores datos: ",lista)
    return lista           

def leer_matriz():
    matriz=[]
    filas=int(input("Cantidad de filas: "))
    columnas=int(input("Cantidad de columnas: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)

    print("Matriz generada segun los anteriores datos: ")
    for fila in matriz:
        print(fila)
                
def factorial(valor):
    c=valor
    factorial=1
    while c>0:
        factorial*=c
        c-=1
    return factorial

def triangulo_equilatero(lado_1, lado_2, lado_3):
    return lado_1 == lado_2 == lado_3

def triangulo_isosceles(lado_1, lado_2, lado_3):
    return lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3

def triangulo_escaleno(lado_1, lado_2, lado_3):
    return lado_1 != lado_2 and lado_1 != lado_3 and lado_2 != lado_3

def punto_1():
    print("Punto 1 (se tiene una cantidad dada de ternas...)")
    print("A continuación, ingrese mínimo 4 ternas para desarrollar de forma correcta el ejercicio")
    cantidad_ternas = int(input("Cantidad de ternas a procesar: "))
    
    contar_equilateros = 0
    contar_isosceles = 0
    contar_escalenos = 0
    
    for c in range(cantidad_ternas):
        lado_1 = int(input("Lado 1: "))
        lado_2 = int(input("Lado 2: "))
        lado_3 = int(input("Lado 3: "))
        
        if triangulo_equilatero(lado_1, lado_2, lado_3):
            print("Triangulo equilatero")
            contar_equilateros += 1
        elif triangulo_isosceles(lado_1, lado_2, lado_3):
            print("Triangulo isosceles")
            contar_isosceles += 1
        elif triangulo_escaleno(lado_1, lado_2, lado_3):
            print("Triangulo escaleno")
            contar_escalenos += 1
    
    print("Cantidad de triángulos equiláteros:", contar_equilateros)
    print("Cantidad de triángulos isósceles:", contar_isosceles)
    print("Cantidad de triángulos escalenos:", contar_escalenos)

punto_1()
