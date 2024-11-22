'''Resolver la siguiente ecuación, teniendo en cuenta que solo se puede realizar si la
variable r es diferente de 2; en caso contrario hacer P=1
P=(r-2)3'''
r= int (input("Ingrese el valor de r "))

if r !=2:
    solucion=(r-2)**3
    print("El resultado de la ecuacion es=", solucion)
else:
    solucion=1
    print("El resultado de la ecuacion es=", solucion)