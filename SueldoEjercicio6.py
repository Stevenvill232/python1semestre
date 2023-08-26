print("Empleado 1")
horas=float(input("Numero de horas trabajadas "))
valor=float(input("Valor de la hora "))
pagar=horas*valor
if pagar>200000:
    total=pagar*0.1
    totalpagar=pagar-total
    print("Sueldo a pagar",totalpagar)
else:
    if pagar<=200000:
        total=pagar*0.05
        totalpagar=pagar-total
        print("Sueldo a pagar",totalpagar)

print("Empleado 2")
horas=float(input("Numero de horas trabajadas "))
valor=float(input("Valor de la hora "))
pagar=horas*valor
if pagar>200000:
    total=pagar*0.1
    totalpagar=pagar-total
    print("Sueldo a pagar",totalpagar)
else:
    if pagar<=200000:
        total=pagar*0.05
        totalpagar=pagar-total
        print("Sueldo a pagar",totalpagar)

