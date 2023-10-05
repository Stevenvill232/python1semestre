# se tiene una matriz y un vector con datos numericos 
#formar dos listas asi: lista 1 con los numeros no comunes sin repetir 
# lista 2 con los primos no repetidos
import random

def leer_vector():
    lista=[]
    for i in range(9):
        lista.append(random.randint(1,13))
    print("lista original",lista)
    return lista

def leer_matriz():
    matriz=[]
    for i in range(3):
        fila=[]
        for j in range(4):
            fila.append(random.randint(1,15))

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

def lista_1_primos_sin_repetir(lista):
    lista_1=[]
    for i in range(len(lista)):
        if primos(lista[i]):
            dato= lista[i] in lista_1
            if dato==False:
                lista_1.append(lista[i])

    return lista_1

def lista_2_fibonaccis_sin_repetir(lista):
    lista_2=[]
    for i in range(len(lista)):
        if fibonaccis(lista[i]):
            dato= lista[i] in lista_2
            if dato==False:
                lista_2.append(lista[i])

    return lista_2                        


lista=leer_vector()
a=lista_1_primos_sin_repetir(lista)
b=lista_2_fibonaccis_sin_repetir(lista)
print("Lista con primos sin repetir: ",a)
print("Lista con fibonaccis sin repetir: ",b)


              


