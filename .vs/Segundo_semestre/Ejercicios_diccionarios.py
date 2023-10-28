def leer_lista():
    lista = []
    cantidad = int(input("Cantidad de datos en la lista: "))
    for i in range(cantidad):
        lista.append(int(input(f'Dato({i})= ')))
    return lista

def obtener_diccionario():
    lista = leer_lista()
    diccionario = {}
    for num in lista:
        if num in diccionario:
            diccionario[num] += 1
        else:
            diccionario[num] = 1
    print("Diccionario resultante:", diccionario)
    return diccionario

def ordenar_diccionario_por_valor():
    diccionario = obtener_diccionario()
    elementos_diccionario = diccionario.items()
    diccionario_ordenado = dict(sorted(elementos_diccionario, key=lambda t: t[1]))
    print("Diccionario ordenado:", diccionario_ordenado)
    return diccionario_ordenado

def formar_diccionario_listas(lc,lv):
    diccionario_1={}
    for i in range(len(lc)):
        diccionario_1[lc[i]]=lv[i]
    return diccionario_1    

def ordenar_diccionario_logica_por_claves():
    diccionario=obtener_diccionario()
    lista_claves=list(diccionario.keys())
    lista_valores=list(diccionario.values())
    for i in range(len(lista_claves)-1):
        for j in range(i+1,len(lista_claves)):
            if lista_claves[j]<lista_claves[i]:
                lista_claves[i],lista_claves[j]=lista_claves[j],lista_claves[i]
                lista_valores[i],lista_valores[j]=lista_valores[j],lista_valores[j]

    diccionario_ordenado=formar_diccionario_listas(lista_claves,lista_valores)
    print("Diccionario ordenado por claves: ",diccionario_ordenado)

def ordenar_diccionario_logica_por_valores():
    diccionario=obtener_diccionario()
    lista_claves=list(diccionario.keys())
    lista_valores=list(diccionario.values())
    for i in range(len(lista_valores)-1):
        for j in range(i+1,len(lista_valores)):
            if lista_valores[j]<lista_valores[i]:
                lista_valores[i],lista_valores[j]=lista_valores[j],lista_valores[i]
                lista_claves[i],lista_claves[j]=lista_claves[j],lista_claves[i]

    diccionario_ordenado=formar_diccionario_listas(lista_claves,lista_valores)
    print("Diccionario ordenado por valores: ",diccionario_ordenado)    


def factorial(valor):
    c=valor
    factorial=1
    while c>0:
        factorial*=c
        c-=1
    return factorial

def es_primo(valor):
    valor=int(valor)
    c=1
    div=0
    while c<=valor:
        if valor % c == 0:
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

def formar_diccionario_listas(lc,lv):
    diccionario_1={}
    for i in range(len(lc)):
        diccionario_1[lc[i]]=lv[i]
    return diccionario_1 

def formar_diccionario_listas_posibles_claves_repetidas(lc, lv):
    diccionario_1 = {}
    for i in range(len(lc)):
        clave = lc[i]
        valor = lv[i]
        if clave in diccionario_1:
            # Si la clave ya existe en el diccionario, agrega el valor a una lista
            diccionario_1[clave].append(valor)
        else:
            # Si la clave no existe en el diccionario, crea una nueva entrada
            diccionario_1[clave] = [valor]
    return diccionario_1

def diccionario_punto_2():
    print('''Se tienen 2 listas, formar dos diccionarios asi:
          (1). Con los primos comunes como claves y su respectivo factorial como valor
          (2). Con los fibonaccis no comunes como claves y los pares menores que el respectivo fibonacci coo valor''')
    lista_1 = leer_lista()
    lista_2 = leer_lista()
    primos_comunes = []
    factoriales_primos = []
    fibonaccis_no_comunes = {}
    
    for i in range(len(lista_1)):
        dato_actual = lista_1[i]
        if es_primo(dato_actual):
            if dato_actual in lista_2:
                if dato_actual not in primos_comunes:
                    primos_comunes.append(dato_actual)

        if fibonaccis(dato_actual):
            if dato_actual not in lista_2:
                if dato_actual not in fibonaccis_no_comunes:
                    fibonaccis_no_comunes[dato_actual] = []
            else:
                if dato_actual not in primos_comunes:
                    fibonaccis_no_comunes[dato_actual] = []            
                    
    for i in range(len(lista_2)):
        dato_actual = lista_2[i]
        if fibonaccis(dato_actual):
            if dato_actual not in lista_1:
                if dato_actual not in fibonaccis_no_comunes:
                    fibonaccis_no_comunes[dato_actual] = []
            else:
                if dato_actual not in primos_comunes:
                    fibonaccis_no_comunes[dato_actual] = []
                    
    for i in range(len(primos_comunes)):
        dato_factorial = factorial(primos_comunes[i])
        factoriales_primos.append(dato_factorial)

    for i in range(len(fibonaccis_no_comunes)):
        c = list(fibonaccis_no_comunes.keys())[i] - 1
        while c > 0:
            if c % 2 == 0:
                fibonaccis_no_comunes[list(fibonaccis_no_comunes.keys())[i]].append(c)
            c -= 1    

    diccionario_1 = formar_diccionario_listas_posibles_claves_repetidas(primos_comunes, factoriales_primos)
    
    print("Diccionario 1 con primos comunes como claves y su factorial como valores respectivamente:", diccionario_1)
    print("Diccionario 2 con fibonaccis no comunes como claves y los pares menores del respectivo fibonacci como valor:", fibonaccis_no_comunes)

def diccionario_punto_3():
    print('''Se tiene una cadena donde hay caracteres numericos y alfabeticos, formar 2 diccionarios asi: 
          (1). con los digitos como claves y las veces que se repiten como valor
          (2). con las letras como claves y las veces que se repiten como valor''')
    cadena_1=input("Digite su respectiva cadena (debe contener caracteres numericos y alfabeticos): ")
    lista_digitos=[]
    contador_digitos=[]
    lista_caracteres=[]
    contador_caracteres=[]
    for caracter in cadena_1:
        if caracter.isdigit():
            dato_actual=caracter
            if dato_actual not in lista_digitos:
                lista_digitos.append(dato_actual)
                contador_digitos.append(1)
            else:
                contador_digitos[lista_digitos.index(dato_actual)]+=1
        elif caracter.isalpha():
            dato_actual_2=caracter
            if dato_actual_2 not in lista_caracteres:
                lista_caracteres.append(dato_actual_2)
                contador_caracteres.append(1)
            else:
                contador_caracteres[lista_caracteres.index(dato_actual_2)]+=1

    diccionario_1=formar_diccionario_listas(lista_digitos,contador_digitos)  
    diccionario_2=formar_diccionario_listas(lista_caracteres,contador_caracteres)
    print("Dicionario 1 con los digitos como clave y las veces que se repite como valor: ",diccionario_1)
    print("Dicionario 2 con las letras como clave y las veces que se repiten como valor: ",diccionario_2)

diccionario_punto_3()
