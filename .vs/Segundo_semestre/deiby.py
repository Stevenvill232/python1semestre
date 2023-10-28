def claveNumerica(cadena):
    b=0
    c=0
    l=list(cadena)
    while c<len(l) and b==0:
        if l[c].isnumeric()==False:
            b=1
        c+=1
    if b==0:
        return True
    else: 
        return False

def primo(num):
    c = 2
    b = 0
    while c<num and b==0:
        if num%c==0:
            b=1
        c+=1
    if b==0:
        return True
    else: 
        return False

def primoUnoDos(v):
    c=0
    for i in v:
        c+=1
        if primo(i):
            if c==1:
                p1=i
            if c==2:
                p2=i
    return p1,p2
def primosConsecutivos(Pmen,Pmay):
    b=0
    c=Pmen+1
    while c<Pmay and b==0:
        if primo(c):
            b=1
        c+=1
    if c==0:
        return True
    else:
        return False
d = {
    "abc":[4,7,2,5],
    "123":[4,7,4,11],
    "xyz":[5,3,2,9]
}
a = "Hola mudo"
l = list(a)
print(l)