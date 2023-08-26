#Valor de factura de agua      
codigo_bloqueo=int(input("Codigo de bloqueo= "))
codigo_usuario=int(input("Codigo de usuario= "))
c=0
while codigo_usuario != codigo_bloqueo:
    c+=1
    nombre_usuario=input("Nombre de usuario: ")
    valor_agua=int(input("Valor de agua por metro cubico: ""$"))
    consumo_mensual=int(input("Consumo mensual en metros cubicos= "))
    estrato=int(input("Estrato del usuario= "))
    valor_agua=consumo_mensual*valor_agua
    valor_total=0
    valor_descuento=0
    if estrato==1:
        valor_descuento=valor_agua*0.4
        valor_total=valor_agua-valor_descuento
    elif estrato==2:
        valor_descuento=valor_agua*0.3
        valor_total=valor_agua-valor_descuento
    elif estrato==3:
        valor_descuento=valor_agua*0.15
        valor_total=valor_agua-valor_descuento
    elif estrato==4:
        valor_total=valor_agua
    elif estrato in [5, 6]:
        valor_descuento=valor_agua*0.2
        valor_total=valor_agua+valor_descuento
    elif estrato>6:
        print("!Estrato invalido!")    

    valor_pagar=0
    incremento=0                 

    if consumo_mensual>10:
        incremento=valor_total*0.1
        valor_pagar=valor_total+incremento
        print("Factura #",c)
        print("Codigo de usuario: ",codigo_usuario)
        print("Nombre: ",nombre_usuario)
        print("Valor con descuento por estrato= ",valor_total,"$")
        print("Por consumir mas de 10 m°3")
        print("Valor total a pagar",valor_pagar,"$")
    else:
        valor_pagar=valor_total
        print("Factura #",c)
        print("Codigo de usuario: ",codigo_usuario)
        print("Nombre: ",nombre_usuario)
        print("Valor con descuento por estrato= ",valor_total,"$")
        print("Valor total a pagar= ",valor_pagar)  

    codigo_usuario=int(input("Codigo de usuario= "))
    
    