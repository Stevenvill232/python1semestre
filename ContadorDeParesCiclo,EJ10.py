cp=0
cd=1
while cd<=4:
    num=int(input("Digitar dato numerico= "))
    if num%2==0:
        cp=cp+1
    cd=cd+1
print("Cantidad de pares= ",cp)
