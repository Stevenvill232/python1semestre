# se tiene una matriz y un vector con datos numericos 
#formar dos listas asi: lista 1 con los numeros no comunes sin repetir 
# lista 2 con los primos no repetidos


def leer_vector():
    lista=[]
    cantidad_datos=int(input("Cantidad de datos de la lista: "))
    for i in range(cantidad_datos):
        lista.append(int(input(f'Dato({i})= ')))
    print("lista original",lista)
    return lista

def leer_matriz():
    matriz=[]
    filas=int(input("Cantidad de filas de la matriz: "))
    columnas=int(input("Columnas de la matriz: "))
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})')))
        matriz.append(fila)

    for fila in matriz:
        print(fila)        
    return matriz 
   
def primos(valor):
    c=1
    div=0
    while c<=valor:
        if valor %c==0:
            div+=1
        c+=1

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

def lista_1_no_comunes():
    lista=leer_vector()
    matriz=leer_matriz()
    lista_1=[]
    for i in range(len(lista)):
        dato= lista[i] in matriz
        if dato==False:
            dato_2= lista[i] in lista_1
            if dato_2==False:
                lista_1.append(lista[i])

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            dato= matriz[i][j] in lista
            if dato==False:
                dato_2=matriz[i][j] in lista_1
                if dato==False:
                    lista_1.append(matriz[i][j])

    print("Lista creada: ",lista_1)
    return lista_1
                

lista_1_no_comunes()


              


