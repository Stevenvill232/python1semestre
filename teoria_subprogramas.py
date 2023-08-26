def say_hello(name):
    print(f"Hola, {name}")

say_hello("Steven")

#return nos sirve para retornar o expresar un valor 
def uno():
    return 1

print(uno())
if uno()==1:
    print("Siempre 1")
else:
    print("No se va a presentar")    

#si no incluyeramos return nos saldra none
def empty():
    x=0

print(empty())

#parametro por valor, a pesar de que se esta modificando los valores por dentro de la funcion
#este no afectara por fuera ya que en este tipo de parametro unicamente se tiene en cuenta lo que esta fuera de la funcion
def f(a, b, c):
# No altera los objetos originales.
  	a, b, c = 4, 5, 6  #Esta asignación es permitida en python

a, b, c = 1, 2, 3
f(a, b, c)
print(a, b, c) # Imprime 1, 2, 3.

a = 10
b = 2
def my_min(x, y):
    if x < y:
        return x
    else:
        return y

result = my_min(a, b)
print(result)  # Imprimirá 2

### id nos da la direccion de la variable
a=1
print(id(a))
a=2
print(id(a))

#### Parametro por valor si se puede modificar dentro de una funcion si es una LISTA 
a=1
b=2
c=2
def f(a,b,c):
    return 4,5,6

a,b,c=f(a,b,c)
print(f(a,b,c))

### Funcion que recibe PARAMETRO
def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Juan")  # Imprimirá "Hola, Juan!"
saludar("María")  # Imprimirá "Hola, María!"

### Funcion que no recibe parametro
def imprimir_mensaje():
    mensaje = "¡Hola desde la función!"
    print(mensaje)

imprimir_mensaje()  # Imprimirá "¡Hola desde la función!"

###con parametro
def leer_vecor_1(l1):
    cantidad_datos=int(input("Cantidad de datos= "))
    for i in range(cantidad_datos):
        l1.append(int(input("Dato({})= ".format(i))))
    print(l1)
    return l1        
leer_vecor_1(l1=[])
####sin parametro
def leer_vector():
    l1=[]
    cantidad_datos=int(input("Cantidad de datos= "))
    for i in range(cantidad_datos):
        l1.append(int(input("Dato({})= ".format(i))))
    print(l1)
    return l1    

leer_vector()

####con parametro
def leer_vecor_1(matriz_1):
    filas=int(input("Numero de filas= "))
    columnas=int(input("Numero de columnas= "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz_1.append(fila)
    print(matriz_1)
    return matriz_1    
leer_vecor_1(matriz_1=[])            

####sin parametro
def matriz_2():
    mat_2=[]
    filas=int(input("Numero de filas= "))
    columnas=int(input("Numero de columnas= "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        mat_2.append(fila)
    print(mat_2)
    return mat_2

matriz_2()

### Con parametro
def sifibonacci(numero):
    a=0
    b=1
    t=0
    while t<numero:
        t=a+b
        a=b
        b=t

    if numero==t:
        print("Numero es fibonacci")
    else:
        print("Numero no es fibonacci")
    return numero    

sifibonacci(int(input("Numero: ")))

#### Sin parametro
def sifibonacci():
    numero=int(input("Numero: "))
    a=0
    b=1
    t=0
    while t<numero:
        t=a+b
        a=b
        b=t

    if numero==t:
        print("Numero es fibonacci")
    else:
        print("Numero no es fibonacci")
    return numero    

sifibonacci()

####Aplicacion
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
    return int(promedio) #return de la accion que se realizo y que queremos guardar para el siguiente paso

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


matriz = leer_matriz() #La línea (matriz = leer_matriz()) obtiene la matriz ingresada por el usuario y la almacena en la variable matriz.
                       #siempre debem asignarse los valores que se obtuvieron a una variable, esto para segur siendo utilizadas  
promedio_primos = calculo_primos(matriz) #calcula el promedio de los números primos en la matriz utilizando la función calculo_primos(),
                                         # pasando la matriz como argumento, y almacena este promedio en la variable promedio_primos.
si_fue_fibo= promedio_fibo(promedio_primos)