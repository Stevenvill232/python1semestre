#Determina el valor a pagar a cada empleado utilizando registro centinela.
nume=int(input('codigo limite '))
sums=0
sumd=0
code=int(input('Codigo empleado -> '))
while   code<=nume:
    nh=int(input('Numero de horas trabajadas -> '))
    vh=int(input('Valor de la hora -> '));
    pdesc=int(input('Porcentaje descuento -> '))
    st=nh*vh
    descuento=st*pdesc/100
    sn=st-descuento
    print('Codigo empleado -> ',code, ' Sueldo neto ',sn)
    sumd=sumd+descuento
    sums=sums+sn
    code=int(input('Codigo empleado -> '))

#Resultados totales
print('\nTotal sueldos pagado  ',sums)
print('Total descuentos       ',sumd)


