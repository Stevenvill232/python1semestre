a=int(input("Digitar primer valor"))
b=int(input("Digitar segundo valor"))
c=int(input("Digitar tercer valor"))
if a<b:
    if b<c:
        print(a," ",b," ",c)
    else:
        if c<a:
            print(c," ",a," ",b)
        else:
            print(a," ",c," ",b)
else:
    if a<c:
        print(b," ",a," ",c)
    else:
        if c<b:
            print (c," ",b," ",a)
        else:
            print (b," ",c," ",a)
