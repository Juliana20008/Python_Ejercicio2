'''El costo de entrada a un parque de diversiones depende de la edad de las
personas; si la persona tiene más de 1 año y menos de 4 años entra gratis; si tiene
entre 4 y 8 años paga US $2, si tiene entre 9 y 16 años paga US $5, si tiene entre 17
y 35 años paga US $6 y si tiene más de 35 años paga US$10. Imprimir el valor en
dólares y pesos colombianos.'''
edad= int(input ("Ingrese la edad:"))
pesos1=4400*2
pesos2=4400*5
pesos3=4400*6
pesos4=4400*10

if edad>1 and edad<4:
    print("Entra gratis")
if edad>=4 and edad<=8:
    print("paga 2$ US y en pesos colombianos es", pesos1)
if edad>=9 and edad<=16:
    print("paga 5$ US y en pesos colombianos es", pesos2)
if edad>=17 and edad<=35:
    print("paga 6$ US y en pesos colombianos es", pesos3)
if edad>35:
    print("paga 10$ US y en pesos colombianos es", pesos4)
