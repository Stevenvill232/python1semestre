#Pago de empleados forma 1
print("Pago de empleados forma 1")
cantidad_empleados=int(input("Cantidad de empleados= "))
c=1
sueldo_sin_descuento=0
descuento=0
sueldo_neto=0
total_sueldos=0
total_descuentos=0
while c<=cantidad_empleados:
    c+=1
    nombre_empleado=input("Nombre del empleado: ")
    cedula=int(input("cedula: "))
    print("brinde los siguientes datos del empleado a pagar: ")
    horas_trabajadas=int(input("Numero de horas trabajadas: "))
    valor_hora=int(input("Valor por hora trabajada: "))
    porcentaje_descuento=int(input("Porcentade de descuento: "))
    sueldo_sin_descuento=horas_trabajadas*valor_hora
    descuento=sueldo_sin_descuento*porcentaje_descuento/100
    sueldo_neto=sueldo_sin_descuento-descuento
    print("Empleado: ",nombre_empleado)
    print("Con cedula: ",cedula)
    print("sueldo a pagar: ",sueldo_neto)
    total_sueldos+=sueldo_neto
    total_descuentos+=descuento

print("Total de sueldos pagados sin descuentos= ",total_sueldos+total_descuentos)
print("Total de sueldos con descuento= ",total_sueldos)
print("Total realizado de descuentos= ",total_descuentos)

print("Fin algoritmo")
#Pago de empleado con codigo limite
print("Pago de empleado con codigo limite")
codigo_limite=int(input("codigo limite "))
suma_sueldos=0
suma_descuentos=0
codigo_empleado=int(input("Codigo empleado -> "))
while   codigo_empleado != codigo_limite:
    numero_horas=int(input("Numero de horas trabajadas -> "))
    valor_hora=int(input("Valor de la hora -> "));
    porcentaje_descuento=int(input("Porcentaje descuento -> "))
    sueldo_total=numero_horas*valor_hora
    descuento=sueldo_total*porcentaje_descuento/100
    sueldo_neto=sueldo_total-descuento
    print("Codigo empleado -> ",codigo_empleado,  "Sueldo neto" ,sueldo_neto)
    suma_descuentos+=descuento
    suma_sueldos+=sueldo_neto
    codigo_empleado=int(input("Codigo empleado -> "))

print("Total sueldos pagado  ",suma_sueldos)
print("Total descuentos  ",suma_descuentos)

print("Fin algoritmo")


