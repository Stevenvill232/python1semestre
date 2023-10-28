
#manejo de cadenas
cadena='Esto es una cadena'
#print(len(cadena))
#for i in range(len(cadena)):
    #print(cadena[i])

#for lon in cadena:
    #print(lon)
#concatenacion
cad_1='Esto'
cad_2='es'
cad_3='una cadena'
cad_4=cad_1+cad_2+cad_3


#troceado
#obtener subcadenas
cad_4[:]#toda la cadena
#print(cad_4[0:8])
#cad_4[start:end:step(paso)
#print(cad_4[5:15:3])
#STR cambia lo de dentro del parentecis a cadena
#str(10)
#str(25,4)
l1=['a','b','c']
cad=''
#for i in range(len(l1)):
    #cad=cad + l1[i]
#print(cad)    

#FIND  me haya un dato en una cadena
#index tambien nos sirve para hallar la posicion
#los=cad_4.index('es')
#print(los)
#'cadena'.isnumeric() (me dice si todos los elementos de la cadena son numeros)
#cade='abc_d'
#cad.isalpha() me dices si los componentes son alfanumericos
#cad[0].isdigit() para saber si es un digito
#"9".isdigit() verdadero
#cad_4.upper()= CONVIERTE A MAYUSCULAS
#cad_4.lower()= Convierte todo a minusculas
#RELACION ENTRE CADENAS Y LISTAS
cadd='Hola mundo'
l=list(cadd)
#l=['H','l','a'] eso hace "list"
l.sort()
#print(l)
cadd="".join(l)#me convierte una lista a una cadena
#print(cadd)
#cad.replace('mundo','hola')= "hola hola" (me reemplaza mundo por hola )
#FUNCION SPLIT:
#split()=dividir una cadena en palabras o una cadena es subcadenas
#strip()=elimina caracteres especiales cono: nueva linea, tabulador, solo deja caracteres que son letras y numeros
nueva_cadena='        Esto es una cadena      \n '
sisas=nueva_cadena.strip()
print(sisas)


