import os #Para manejar lo de pausas del menu
#os.system('cls)
#os.system('pause)

######CONTROL DE FUNCIONES EN GENERAL
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
    return matriz    

def llenar_conjunto_desde_teclado():
    mi_conjunto = set()  # Crea un conjunto vacío
    while True:
        entrada = input("Ingrese un elemento (o presione Enter para finalizar): ")
        # Comprueba si el usuario presionó Enter para finalizar la entrada
        if not entrada:
            break
        
        # Agrega el elemento al conjunto
        mi_conjunto.add(entrada)
    print("Conjunto resultante:", mi_conjunto)
    return mi_conjunto

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

def ordenar_diccionario_por_valor(dic):
    diccionario =dic
    elementos_diccionario = diccionario.items()
    diccionario_ordenado = dict(sorted(elementos_diccionario, key=lambda t: t[1]))
    print("Diccionario ordenado:", diccionario_ordenado)
    return diccionario_ordenado

def ordenar_diccionario_por_clave(dic):
    diccionario =dic
    elementos_diccionario = diccionario.items()
    diccionario_ordenado = dict(sorted(elementos_diccionario, key=lambda t: t[0]))
    print("Diccionario ordenado:", diccionario_ordenado)
    return diccionario_ordenado

def ordenar_con_correspondencia(l1, l2):
    n = len(l1)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l1[j] < l1[i]:
                l1[i], l1[j] = l1[j], l1[i]
                l2[i], l2[j] = l2[j], l2[i]

    return l1, l2

#####CONTROL DE EJERCICIOS DEL TALLER

def punto_1():
    print('''Punto 1 (Se tiene una cantidad dada de ternas (3 valores numéricos por terna) correspondientes a los lados de triángulos, determinar si la suma de los perímetros 
        del segundo,cuarto equiláteros y segundo escaleno de acuerdo al orden de entrada, es un numero Fibonacci, si no lo es determinar si es primo
        y su factorial.)''')
    print("**A continuación, ingrese mínimo 4 triangulos equilateros y 2 escalenos, para desarrollar de forma correcta el ejercicio***")
    cantidad_ternas = int(input("Cantidad de ternas a procesar: "))
    
    contar_equilateros = 0
    contar_escalenos = 0
    perimetro_equilatero=0
    perimetro_escaleno=0
    
    for i in range(cantidad_ternas):
        lado_1 = int(input("Lado 1: "))
        lado_2 = int(input("Lado 2: "))
        lado_3 = int(input("Lado 3: "))
        
        if triangulo_equilatero(lado_1, lado_2, lado_3):
            print("Triangulo equilatero")
            contar_equilateros += 1
            if contar_equilateros==2:
                perimetro_equilatero += lado_1* 3
            elif contar_equilateros==4:
                perimetro_equilatero += lado_1 * 3    
            
        elif triangulo_escaleno(lado_1, lado_2, lado_3):
            print("Triangulo escaleno")
            contar_escalenos += 1
            if contar_escalenos==2:
                perimetro_escaleno= lado_1+lado_2+lado_3

    suma_perimetros=perimetro_equilatero+perimetro_escaleno
    print("Suma de perimetros del segundo, cuarto equilatero y el segundo escaleno= ",suma_perimetros)
    if fibonaccis(suma_perimetros):
        print("Esta suma de perimetros SI es un numero fibonacci") 

    if not fibonaccis(suma_perimetros):
        print("Esta suma de perimetros NO es un numero fibonacci")
        if es_primo(suma_perimetros):
            print("Esta suma de perimetros SI es un numero primo")
            print("El factorial de esta suma de perimetros es: ",factorial(suma_perimetros))
        else:
            print("Esta suma de perimetros NO es un numero primo")    

def punto_3():
    print("PUNTO 3 (Se tienen dos listas, crear una nueva lista con los PRIMOS COMUNES SIN REPETIR)")
    lista_1=leer_lista()
    lista_2=leer_lista()
    lista_creada=[]
    for i in range(len(lista_1)):
        if es_primo(lista_1[i]):
            dato= lista_1[i] in lista_2
            if dato==True:
                dato_2= lista_1[i] in lista_creada
                if dato_2==False:
                    lista_creada.append(lista_1[i])

    print("Lista creada con los primos comunes sin repetir entre los dos vectores: ",lista_creada)                

def punto_7():
    print("PUNTO 7 (Se tienen un vector con datos numéricos donde hay varios repetidos, hallar la multiplicación con sumas del primo que más se repite con el primo que menos se repite.)")
    lista_1=leer_lista()
    contados=[]
    contador_contados=[]
    for i in range(len(lista_1)):
        if es_primo(lista_1[i]):
            dato= lista_1[i] 
            if dato not in contados:
                contados.append(dato)
                contador_contados.append(1)
            else:
                contador_contados[contados.index(dato)]+=1    

    contados,contador_contados=ordenar_con_correspondencia(contados,contador_contados)

    print("Primo que mas veces se repite: ",contados[-1]," Con ",contador_contados[-1]," veces")            
    print("Primo que menos veces se repite: ",contados[0]," Con ",contador_contados[0]," veces")
    limite=contados[-1]
    c=1
    multiplicacion=0
    while c<=limite:
        multiplicacion+=contados[0]
        c+=1    
    print("Su multiplicacion con sumas es: ",multiplicacion)    

def punto_11():
    print("PUNTO 11 (Determinar si el primo 2 y el primo 4 según el recorrido por filas de la matriz, son consecutivos, es decir, no hay un número primo entre los dos) ")
    matriz = leer_matriz()
    si_primo = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if es_primo(matriz[i][j]):
                si_primo += 1
                if si_primo == 2:
                    primo_segundo = matriz[i][j]
                elif si_primo == 4:
                    primo_cuarto = matriz[i][j]

    print("Segundo primo de la matriz:", primo_segundo, "Cuarto primo de la matriz:", primo_cuarto)
    if primo_cuarto < primo_segundo:
        aux = primo_segundo
        primo_segundo = primo_cuarto
        primo_cuarto = aux
    c = primo_segundo + 1
    b = 0
    while c < primo_cuarto:
        if es_primo(c):
            b = 1
            break  
        else:
            c += 1
    if b == 0:
        print("Estos son consecutivos")
    else:
        print("Estos NO son consecutivos")
                                  
def punto_13():
    print("PUNTO 13 (Se tiene un conjunto y una matriz con datos numéricos, hallar el primo mayor del conjunto y su factorial y llenar este valor en las posiciones comprendidas entre el par menor y el Fibonacci mayor de la matriz)")
    conjunto = llenar_conjunto_desde_teclado()
    matriz = leer_matriz()

    si_primo = 0
    for elemento in conjunto:
        if es_primo(elemento):
            si_primo += 1
            if si_primo == 1:
                primo_mayor = int(elemento)
            else:
                if int(elemento) > primo_mayor:
                    primo_mayor = int(elemento)

    su_factorial = factorial(primo_mayor)
    print("Primo mayor del conjunto:", primo_mayor, "Su factorial =", su_factorial)

    si_par = 0
    si_fibonacci = 0
    par_menor = float('inf') #lo utilizamos para representar un valor inicial
    fibonacci_mayor = 0
    par_menor_fila = 0
    par_menor_columna = 0
    fibonacci_mayor_fila = 0
    fibonacci_mayor_columna = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                si_par += 1
                if matriz[i][j] < par_menor:
                    par_menor = matriz[i][j]
                    par_menor_fila = i
                    par_menor_columna = j

            if fibonaccis(matriz[i][j]):
                si_fibonacci += 1
                if matriz[i][j] > fibonacci_mayor:
                    fibonacci_mayor = matriz[i][j]
                    fibonacci_mayor_fila = i
                    fibonacci_mayor_columna = j

    print("Par menor de la matriz:", par_menor, "Su posicion:", "Fila:", par_menor_fila, "Columna:", par_menor_columna)
    print("Fibonacci mayor de la matriz:", fibonacci_mayor, "Su posicion:", "Fila:", fibonacci_mayor_fila, "Columna:", fibonacci_mayor_columna)

    # Reemplazar el factorial 
    for i in range(par_menor_fila, fibonacci_mayor_fila + 1):
        for j in range(par_menor_columna, fibonacci_mayor_columna + 1):
                matriz[i][j] = su_factorial

    for fila in matriz:
        print(fila)

def punto_15():
    print("PUNTO 15 (Se tienen dos matrices con datos numéricos Formar un diccionario con los primos como clave y las veces que aparecen como valor, ordenado por la clave.)")
    matriz_1=leer_matriz()
    matriz_2=leer_matriz()
    lista_primos=[]
    lista_primos_contados=[]
    for i in range(len(matriz_1)):
        for j in range(len(matriz_1[i])):
            if es_primo(matriz_1[i][j]):
                dato_actual=matriz_1[i][j]
                if dato_actual not in lista_primos:
                    lista_primos.append(dato_actual)
                    lista_primos_contados.append(1)
                else:
                    lista_primos_contados[lista_primos.index(dato_actual)]+=1

    for i in range(len(matriz_2)):
        for j in range(len(matriz_2[i])):
            if es_primo(matriz_2[i][j]):
                dato_actual=matriz_2[i][j]
                if dato_actual not in lista_primos:
                    lista_primos.append(dato_actual)
                    lista_primos_contados.append(1)
                else:
                    lista_primos_contados[lista_primos.index(dato_actual)]+=1

    lista_primos,lista_primos_contados=ordenar_con_correspondencia(lista_primos,lista_primos_contados)

    diccionario_resultante=formar_diccionario_listas(lista_primos,lista_primos_contados)
    print("Diccionario resultante con los primos como claves y las veces que se repiten como valores: ",diccionario_resultante)

def punto_17():
    print('''PUNTO 17 (Se tienen tres cadenas con caracteres numéricos y alfabéticos, formar dos diccionarios asi:
Diccionario 1 con clave dígito y valor las veces que se repite, ordenado ascendentemente por valor 
Diccionario 2 con clave carácter y valor las veces que se repite, ordenado ascendentemente por clave)''')
    cadena_1=input("Ingresa su primera cadena de caracteres: ")
    cadena_2=input("Ingrese su segunda cadena de caracteres: ")
    cadena_3=input("Ingrese su tercer cadena de caracteres: ")
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

    for caracter in cadena_2:
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

    for caracter in cadena_3:
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

    diccionario_desordenado_digitos=formar_diccionario_listas(lista_digitos,contador_digitos)
    diccionario_resultante_digitos_ordenado=ordenar_diccionario_por_valor(diccionario_desordenado_digitos)
    diccionario_desordenado_caracteres=formar_diccionario_listas(lista_caracteres,contador_caracteres)      
    diccionario_resultante_caracteres_ordenado=ordenar_diccionario_por_clave(diccionario_desordenado_caracteres)
    print("Diccionario 1 resultante de digitos ordenados por valor: ",diccionario_resultante_digitos_ordenado)   
    print("Diccionario 2 resultante de caracter ordenado por clave: ",diccionario_resultante_caracteres_ordenado)

def punto_19():
    print('''PUNTO 19 (Se tienen un vector y una matriz con datos numéricos y repetidos encontrar:
            el par mayor y las veces que se repite
            el primo menor y las veces que se repite
            el Fibonacci menor y las veces que se repite
            Con estos datos hallar:
            El factorial de la suma del par y del primo
            La multiplicación con sumas de los contadores del primo y del Fibonacci.
            )''')
    lista = leer_lista()
    matriz = leer_matriz()
    es_par = 0
    lista_par = []
    contador_par = []
    si_primo = 0
    lista_primo = []
    contador_primo = []
    es_fibonacci = 0
    lista_fibonacci = []
    contador_fibonacci = []

    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            es_par += 1
            if es_par == 1:
                par_mayor = lista[i]
            elif lista[i] > par_mayor:
                par_mayor = lista[i]
            dato_actual = lista[i]
            if dato_actual not in lista_par:
                lista_par.append(dato_actual)
                contador_par.append(1)
            else:
                contador_par[lista_par.index(dato_actual)] += 1
        if es_primo(lista[i]):
            si_primo += 1
            if si_primo == 1:
                primo_menor = lista[i]
            elif lista[i] < primo_menor:
                primo_menor = lista[i]
            dato_actual = lista[i]
            if dato_actual not in lista_primo:
                lista_primo.append(dato_actual)
                contador_primo.append(1)
            else:
                contador_primo[lista_primo.index(dato_actual)] += 1
        if fibonaccis(lista[i]):
            es_fibonacci+=1
            if es_fibonacci==1:
                fibonacci_menor=lista[i]
            elif lista[i]<fibonacci_menor:
                fibonacci_menor=lista[i]
            dato_actual=lista[i]
            if dato_actual not in lista_fibonacci:
                lista_fibonacci.append(dato_actual)
                contador_fibonacci.append(1)
            else:
                contador_fibonacci[lista_fibonacci.index(dato_actual)]+=1                

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] % 2 == 0:
                es_par += 1
                if es_par == 1:
                    par_mayor = matriz[i][j]
                elif matriz[i][j] > par_mayor:
                    par_mayor = matriz[i][j]
                dato_actual = matriz[i][j]
                if dato_actual not in lista_par:
                    lista_par.append(dato_actual)
                    contador_par.append(1)
                else:
                    contador_par[lista_par.index(dato_actual)] += 1
            if es_primo(matriz[i][j]):
                si_primo += 1
                if si_primo == 1:
                    primo_menor = matriz[i][j]
                elif matriz[i][j] < primo_menor:
                    primo_menor = matriz[i][j]
                dato_actual = matriz[i][j]
                if dato_actual not in lista_primo:
                    lista_primo.append(dato_actual)
                    contador_primo.append(1)
                else:
                    contador_primo[lista_primo.index(dato_actual)] += 1
            if fibonaccis(matriz[i][j]):
                es_fibonacci+=1
                if es_fibonacci==1:
                    fibonacci_menor=matriz[i][j]
                elif matriz[i][j]<fibonacci_menor:
                    fibonacci_menor=matriz[i][j]
                dato_actual=matriz[i][j]
                if dato_actual not in lista_fibonacci:
                    lista_fibonacci.append(dato_actual)
                    contador_fibonacci.append(1)
                else:
                    contador_fibonacci[lista_fibonacci.index(dato_actual)]+=1 

    
    lista_par, contador_par = ordenar_con_correspondencia(lista_par, contador_par)
    lista_primo, contador_primo = ordenar_con_correspondencia(lista_primo, contador_primo)
    lista_fibonacci,contador_fibonacci = ordenar_con_correspondencia(lista_fibonacci,contador_fibonacci)
    print("Par mayor:", lista_par[-1], ", Veces que se repitió:", contador_par[-1])
    print("Primo menor:", lista_primo[0], ", Veces que se repitió:", contador_primo[0])
    print("Fibonacci menor: ",lista_fibonacci[0],", Veces que se repitió:",contador_fibonacci[0])
    suma_par_y_primo=lista_par[-1]+lista_primo[0]
    factorial_suma=factorial(suma_par_y_primo)
    print("Suma del par mayor + el primo menor es: ",suma_par_y_primo," Y su factorial es: ",factorial_suma)
    multiplicacion_suma=contador_primo[0]
    c=1
    while c<contador_fibonacci[0]:
        multiplicacion_suma+=contador_primo[0]
        c+=1 
    print("La multiplicacion con sumas entre las veces que se repite el primo menor y el fibonacci menor= ",multiplicacion_suma) 

#####EJERCICIOS DE CADENAS
def leer_cadena():
    cadena=input("Ingrese su cadena de caracteres: ")
    return cadena

def cadena_punto_1():
    print("se tiene una cadena, contar las veces que se repite un caracter")
    cadena=leer_cadena()
    contar=input("caracter a contar: ")
    print(cadena.count(contar))

def cadena_punto_2():
    print("se tiene una cadena ordenarla en forma ascendente y en forma descendente ")
    cadena=leer_cadena()
    cadena_lista=list(cadena)
    cadena_2_lista=list(cadena)
    cadena_lista.sort(reverse=True)
    cadena_2_lista.sort()
    cadena_entregada_ordenada_descendente=" ".join(cadena_lista)
    cadena_entregada_ordenada_ascendente=" ".join(cadena_2_lista)
    print("Cadena ordenada de forma descendente: ",cadena_entregada_ordenada_descendente)
    print("Cadena ordenada de forma ascendente: ",cadena_entregada_ordenada_ascendente)

def cadena_punto_3():
    print("Convertir una cadena dada a mayusculas y minusculas")
    cadena=leer_cadena()
    minusculas=cadena.lower()
    print(minusculas)
    mayusculas=cadena.upper()
    print(mayusculas)

def cadena_punto_4():
    print('''de una cadena dada donde hay digitos y caracteres alfabeticos formas dos cadenas, cadena 1 con los digitos sin repetidos
          cadena 2 con los alfabeticos sin repetidos''')
    cadena=leer_cadena()
    digitos=[] #creamos una lista para poder addicionar caracteres
    alfabetico=[] #ya que una cadena es inmodificable (tambien los podemos almacenar en conjuntos (set()))
    for caracter in cadena:
        if caracter.isdigit():
            dato= caracter in digitos
            if dato==False:
                digitos.append(caracter)
        elif caracter.isalpha():
            dato= caracter in alfabetico
            if dato==False:
                alfabetico.append(caracter)

    cadena_digitos= ''.join(digitos) #utilizamos join para convertir listas o conjuntos a cadenas
    cadena_alfabetico=''.join(alfabetico)
    print("Cadena de digitos sin repetirlos: ",cadena_digitos)
    print("Cadena de alfabeticos sin repetirlos: ",cadena_alfabetico)

def cadena_punto_5():
    print('''se tienen dos cadenas, formar dos cadenas asi: cadena 1 con los digitos no comunes de las dos cadenas 
          cadena 2 con las letras comunes de las dos cadenas, ambas sin repetir''')
    cadena_1=leer_cadena()
    cadena_2=leer_cadena()
    lista_1=[]
    lista_2=[]
    for caracter_1 in cadena_1:
        if caracter_1.isdigit():
            dato= caracter_1 in cadena_2
            if dato== False:
                dato= caracter_1 in lista_1
                if dato==False:
                    lista_1.append(caracter_1)
        elif caracter_1.isalpha():
            dato= caracter_1 in cadena_2
            if dato==True:
                dato= caracter_1 in lista_2
                if dato==False:
                    lista_2.append(caracter_1)            
    
    for caracter_2 in cadena_2:
        if caracter_2.isdigit():
            dato= caracter_2 in cadena_1
            if dato==False:
                dato= caracter_2 in lista_1
                if dato==False:
                    lista_1.append(caracter_2)
        elif caracter_2.isalpha():
            dato= caracter_2 in cadena_1
            if dato==True:
                dato=caracter_2 in lista_2
                if dato==False:
                    lista_2.append(caracter_2)            
    cadena_digitos=''.join(lista_1)
    cadena_letras=''.join(lista_2)
    print("Cadena 1 con digitos no comunes sin repetir: ",cadena_digitos)
    print("Cadena 2 con letras comunes sin repetir: ",cadena_letras)

def cadena_punto_6():
    print("determinar cuantas palabras hay en un parrafo ")
    parrafo=leer_cadena()
    palabras = set()
    parrafo = parrafo.lower()  # Convertir todo a minúsculas para tratar las palabras como únicas

    # Separar el párrafo en palabras
    palabras_en_parrafo = parrafo.split()

    for palabra in palabras_en_parrafo:
        # Limpiar la palabra de caracteres no alfabéticos (Solo dejamos letras)
        palabra = ''.join(c for c in palabra if c.isalpha()) # Esto es una expresión de comprensión de listas.
                #Recorre cada carácter c en la variable palabra. Básicamente, está tomando cada carácter de la palabra uno por uno.
  
        # Agregar la palabra al conjunto si no está vacía
        if palabra:
            palabras.add(palabra)

    print("Hay ",len(palabras)," Palabras en el anterior parrafo") 

def cadena_punto_7():
    print("reemplazar un caracter de una cadena por otro caracter dado")
    cadena=leer_cadena()
    lista=list(cadena)
    dato_reemplazar=input("Caracter que desea reemplzar de la cadena ingresada: ")
    dato_ingresar=input("Caracter por el cual reemplazara el anterior caracter seleccionado: ")    
    if dato_reemplazar in lista:
        posicion=lista.index(dato_reemplazar)
        lista.remove(dato_reemplazar)
        lista.insert(posicion,dato_ingresar)
    else:
        print("El dato que desea reemplazar no se encuentra en la cadena que ha ingresado")

    cadena_cambiada=''.join(lista)
    print("Cadena resultante: ", cadena_cambiada) 

def cadena_punto_8():
    cadena = leer_cadena()

    while True:
        dato_reemplazar = input("Secuencia que desea reemplazar de la cadena ingresada: ")
        
        
        dato_ingresar = input("Secuencia por la cual reemplazará la anterior secuencia seleccionada: ")
        
        cadena = cadena.replace(dato_reemplazar, dato_ingresar) #REPLACE:  forma de buscar y reemplazar texto en una cadena
        #replace(subcadena_a_buscar, subcadena_de_reemplazo)
        break

    print("Cadena resultante:", cadena)

def cadena_punto_9():
    cadena=leer_cadena()
    lista=list(cadena)

    contados=[]
    contador=[]
    for i in range(len(lista)):
        dato_actual=lista[i]
        if dato_actual not in contados:
            contados.append(dato_actual)
            contador.append(1)
        else:
            contador[contados.index(dato_actual)]+=1    

    for i in range(len(contador)):
        for j in range(i+1,len(contador)):
            if contador[j]>contador[i]: #La organizo DE MAYOR A MENOR
                contador[i],contador[j]=contador[j],contador[i]
                contados[i],contados[j]=contados[j],contados[i]

    print("Caracter que mas se repite: '",contados[0], "' Con: ",contador[0]," Veces")

######EJERCICIOS CON DICCIONARIOS
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

def diccionario_punto_1():
    print("Se tiene una lista con datos numericos repetidos, formar un diccionario con CLAVE numero y VALOR las veces que se repite")
    obtener_diccionario()

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

#### Control de puntos del parcial


######CONTROL DE MENU
def menu_taller():
    while True:
        os.system('cls')
        print('______MENU EJERCICIOS DEL TALLER_____ ')
        print('---------------------------------')
        print('   1. Ejercicio 1')
        print('   3. Ejercicio 3')
        print('   5. Ejercicio 5')
        print('   7. Ejercicio 7')
        print('   9. Ejercicio 9')
        print('   11. Ejercicio 11')
        print('   13. Ejercicio 13')
        print('   15. Ejercicio 15')
        print('   17. Ejercicio 17')
        print('   19. Ejercicio 19')
        print('   ')
        print('   (0). Atras')
        print('')
        print('--------------------------------')
        opcion=int(input('Elija una opcion: '))
        match opcion:
            case 1 :
                os.system('cls')
                punto_1()
                os.system('pause')
            case 3 :
                os.system('cls')
                punto_3()   
                os.system('pause')
            case 5 :
                os.system('cls')
                print("*Ejercicio repetido del punto 1*")
                punto_1()    
                os.system('pause')
            case 7 :
                os.system('cls')
                punto_7()
                os.system('pause')
            case 9 :
                os.system('cls')
                print("*Ejercicio repetido del punto 7*") 
                punto_7()
                os.system('pause')
            case 11:
                os.system('cls')
                punto_11()
                os.system('pause')
            case 13:
                os.system('cls')
                punto_13()
                os.system('pause')
            case 15:
                os.system('cls')
                punto_15()
                os.system('pause') 
            case 17:
                os.system('cls')
                punto_17()
                os.system('pause')         
            case 19:
                os.system('cls')
                punto_19()
                os.system('pause')                  
            case 0:
                print('Regresando al menú anterior ')
                break    
            case other:
                print('Ha digitado una opción invalida ')
                os.system('pause')


def menu_ejercicios_cadenas():
    while True:
        os.system('cls')
        print('______MENU EJERCICIOS DE CADENAS_____ ')
        print('---------------------------------')
        print('   1. Contar las veces que se repite un caracter')
        print('   2. Ordenar una cadena ')
        print('   3. Convertir una cadena a mayusculas y minusculas')
        print('   4. Formas 2 cadenas a partir de una')
        print('   5. Se tienen dos cadenas, formar una nueva en especifico')
        print('   6. Determinar cuantas palabras hay en un parrafo')
        print('   7. Reemplazar un caracter por otro')
        print('   8. Reemplazar varios caracteres por otros')
        print('   9. Determinar cual es el caracter que mas se repite')
        print('')
        print('   (0). Atras')
        print('')
        print('--------------------------------')
        opcion=int(input("Elija una opcion: "))
        match opcion:
            case 1:
                os.system('cls')
                cadena_punto_1()
                os.system('pause')
            case 2:
                os.system('cls')
                cadena_punto_2()
                os.system('pause')
            case 3:
                os.system('cls')
                cadena_punto_3()
                os.system('pause')
            case 4:
                os.system('cls')
                cadena_punto_4()
                os.system('pause')
            case 5:
                os.system('cls')
                cadena_punto_5()
                os.system('pause')
            case 6:
                os.system('cls')
                cadena_punto_6()
                os.system('pause')
            case 7:
                os.system('cls')
                cadena_punto_7()
                os.system('pause')
            case 8: 
                os.system('cls')
                cadena_punto_8()
                os.system('pause')
            case 9:
                os.system('cls')
                cadena_punto_9()
                os.system('pause')
            case 0:
                print('Regresando al menú anterior ')
                break   
            case other:
                print('Ha digitado una opción invalida ')
                os.system("pause")
                                                
def menu_ejercicios_diccionarios():
    while True:
        os.system('cls')
        print('______MENU EJERCICIOS DE DICCIONARIOS_____ ')
        print('---------------------------------')
        print('   1. Formar un diccionario a partir de una lista')
        print('   2. Formar 2 diccionarios con primos, fibonaccis y su factorial y pares menores respectivamente')
        print('   3. A partir de una cadena formar 2 diccionarios')
        print('   ')
        print('   (0). Atras')
        print('')
        print('--------------------------------')
        opcion=int(input('Elija la opcion: '))
        match opcion:
            case 1:
                os.system('cls')
                diccionario_punto_1()
                os.system('pause')
            case 2:
                os.system('cls')
                diccionario_punto_2()
                os.system('pause')    
            case 3:
                os.system('cls')
                diccionario_punto_3()
                os.system('pause')     
            case 0:
                print('Regresando al menú anterior ')
                break   
            case other:
                print('Ha digitado una opción invalida ')
                os.system("pause")    


def menu_ejercicios_varios():
    while True:
        os.system('cls')
        print('______MENU EJERCICIOS VARIOS_____ ')
        print('---------------------------------')
        print('   1. Ejercicios con cadenas')
        print('   2. Ejercicios con diccionarios')
        print('   ')
        print('   (0). Atras')
        print('')
        print('--------------------------------')
        opcion=int(input('Elija una opcion: '))
        match opcion:
            case 1:
                menu_ejercicios_cadenas()
                os.system('pause')
            case 2:
                menu_ejercicios_diccionarios()    
                os.system('pause')
            case 0:
                print('Regresando al menú anterior ')
                break  
            case other:
                print('Ha digitado una opción invalida ')
                os.system("pause")    


def menuPrincipal():
    while True:
        os.system('cls')
        print('    ______MENU PRINCIPAL______ ')
        print('---------------------------------')
        print('   1. Ejercicios del nuevo taller')
        print('   2. Ejercicios varios')
        print('   ')
        print('   (0). Salir')
        print('')
        print('--------------------------------')
        print('                  by. *Franklin Villota*')
        # ingresar una opcion
        opcion =int(input('Elija una opción: '))
        match opcion:
            case 1 :
                menu_taller()
                os.system('pause')
            case 2 :
                menu_ejercicios_varios()
                os.system('pause')
                        
            case 0 :
                print('Gracias por su visita ')
                break
            case other: 
                print('Ha digitado una opción invalida ')
                os.system("pause")


menuPrincipal()