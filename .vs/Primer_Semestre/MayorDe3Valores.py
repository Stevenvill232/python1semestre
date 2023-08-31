a=int(input("Digitar primer valor: "))
b=int(input("Digitar segundo valor: "))
c=int(input("Digitar tercer valor: "))
if a>b:
    if a>c:
        print(a,"Es el mayor")
    else:
        print(c,"Es el mayor")

else:
    if b>c:
        print(b,"Es el mayor")
    else:
        print(c,"Es el mayor")
        
