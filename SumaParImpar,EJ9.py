a=int(input('Digitar valor 1 -> '))
b=int(input('Digitar valor 2 -> '))
c=int(input('Digitar valor 3 -> '))
d=int(input('Digitar valor 4 -> '))
sp=0;
si=0;
if a%2==0: 
    sp=sp+a;
else:
    si=si+a	

if b%2==0: 
    sp=sp+b;
else:
    si=si+b  
    
if c%2==0: 
    sp=sp+c;
else:
    si=si+c      
if d%2==0: 
    sp=sp+d;
else:
    si=si+d 
print("Suma de pares ",sp)
print("Suma de impares ",si)
