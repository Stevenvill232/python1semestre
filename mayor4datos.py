a=int(input("Digitar primer valor"))
b=int(input("Digitar segundo valor"))
c=int(input("Digitar tercer valor"))
d=int(input("Digitar cuarto valor"))
if a>b:
    if a>c:
        if a>d:
            print(a,"Es el mayor")
        else:
            print(d,"Es el mayor")
    else:
        if c>d:
            print(c,"Es el mayor")
        else:
            print(d,"Es el mayor")
else:
    if b>c:
        if b>d:
            print(b,"Es el mayor")
        else:
            print(d,"Es el mayor")
    else:
        if c>d:
            print(c,"Es el mayor")
        else:
            print(d,"Es el mayor")                                            