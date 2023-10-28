m1=[[7,2,9,4],[5,3,2,1],[7,9,6,4]]
# a) llenar -5 en las posiciones compredndidas entre 0,3 y 2,1
# b) las posiciones son dinamicas, leer las posiciones

valor_llenar=-5
for i in range(3):
    for j in range(4):
        if i > 0 and i <= 2:
            if j >= 4:
                m1[i][j] = valor_llenar
            if j < 1:
                m1[i][j] = valor_llenar
        if i > 0 and i < 2:
            m1[i][j] = valor_llenar

for fila in m1:
    print("".join("{:4}".format(n) for n in fila))
            
diccionario = {'numeros': [1, 5, 8, 7, 9], '231jak': [1, 2, 6, 4, 7], '2345': [5, 4, 13, 8]}
lista_claves = list(diccionario.keys())
lista_valores = list(diccionario.values())
posicion_encontrada=None
for i in range(len(lista_claves)):
    if lista_claves[i].isnumeric():
        posicion_encontrada = i


def es_primo(valor):
    valor = int(valor)
    c = 1
    div = 0
    while c <= valor:
        if valor % c == 0:
            div += 1
        c += 1
    if div == 2:
        return True
    else:
        return False

if posicion_encontrada==None:
    print("No hay clave numerica")
else:
    si_primo=0
    for j in range(len(lista_valores[posicion_encontrada])):
        for valor in lista_valores[posicion_encontrada]:  # Itera sobre los valores de la lista
            if es_primo(valor):
                si_primo += 1
                if si_primo == 1:
                    primer_primo = valor
                elif si_primo == 2:
                    segundo_primo = valor

    print("Primer primo de la lista: ", primer_primo, "Segundo primo de la lista: ", segundo_primo,"")

    if segundo_primo<primer_primo:
        aux=primer_primo
        primer_primo=segundo_primo
        segundo_primo=aux

    hay_primos=0
    c=primer_primo+1
    while c<segundo_primo:
        if es_primo(c):
            hay_primos+=1
        c+=1    

    if hay_primos>0:
        print("Estos primos no son consecutivos")
    else:
        print("Estos primos son consecutivos")    

def reemplazar_entre_filas(matriz, i_inicio, i_final, j, valor):
    for i in range(i_inicio, i_final + 1):
        matriz[i][j] = valor

# Ejemplo de uso:
m1=[[7,2,9,4],[5,3,2,1],[7,9,6,4]]
# a) llenar -5 en las posiciones compredndidas entre 0,3 y 2,1
# b) las posiciones son dinamicas, leer las posiciones
i=0
j=3
x=2
y=1
while i< len(m1):
    while j<len(m1[0]):
        if i==x and j==y:
            m1[i][j]=-5
            break
        else:
            m1[i][j]=-5
            j+=1
    j=0
    i+=1
print(m1)            


