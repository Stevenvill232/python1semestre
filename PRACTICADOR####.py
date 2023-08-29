def leer_matriz():
    matriz = []
    filas = int(input("Filas: "))
    columnas = int(input("Columnas: "))
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(int(input(f'Dato({i},{j})= ')))
        matriz.append(fila)

    print("Matriz:")
    for fila in matriz:
        print(fila)

    return matriz

def primo_mas_repetido_par_menor(matriz):
    contador=[]
    datos_no_repetidos=[]
    si_par=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c=1
            div=0
            while c<=matriz[i][j]:
                if matriz[i][j] % c==0:
                    div+=1
                c+=1
            if div==2:
                dato_actual=matriz[i][j]
                if dato_actual not in datos_no_repetidos:
                    datos_no_repetidos.append(dato_actual)
                    contador.append(1)
                else:
                    contador[datos_no_repetidos.index(dato_actual)]+=1

            if matriz[i][j] %2==0:
                si_par+=1
                if si_par==1:
                    par_menor=matriz[i][j]
                elif matriz[i][j]<par_menor:
                    par_menor=matriz[i][j]

    for i in range(len(contador)):
        for j in range(i+1,len(contador)):
            if contador[j]>contador[i]:
                contador[i],contador[j]=contador[j],contador[i]
                datos_no_repetidos[i],datos_no_repetidos[j]=datos_no_repetidos[j],datos_no_repetidos[i]

    print("Primo que mas se repite: ",datos_no_repetidos[0],"Veces: ",contador[0])
    print("Par menor: ",par_menor)
    return datos_no_repetidos[0],par_menor

def diagonales(matriz,primo_repetido,par_menor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            #diagonal principal
            if i==j:
                matriz[i][j]=primo_mas_repetido
            elif i+j==len(matriz)-1:
                matriz[i][j]=par_menor    

matriz=leer_matriz()
primo_mas_repetido,par_menor= primo_mas_repetido_par_menor(matriz)
diagonales(matriz,primo_mas_repetido,par_menor)                                                                
