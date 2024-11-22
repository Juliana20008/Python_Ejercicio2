'''Leer los tres lados del triángulo (A,BY C), imprimir el tipo de triangulo teniendo en
cuenta que es un triángulo equilátero(solo si sus tres lados son iguales) y es un
triángulo escaleno(si todos los lados son diferentes). Además debe validar que sus
lados permitan formar un triángulo; la condición es que cada lado tiene que ser
menos que la suma de los otros dos.'''
primerLado= float(input("Ingrese la medida del primer lado del triangulo en centimetros"))
segundoLado= float(input("Ingrese la medida del segundo lado del triangulo en centimetros"))
tercerLado= float(input("Ingrese la medida del tercer lado del triangulo en centimetros"))
suma1=primerLado+segundoLado
suma2=primerLado+tercerLado
suma3=segundoLado+tercerLado
if (primerLado<suma3) and (segundoLado<suma2) and (tercerLado<suma1):
    print("Los lados corresponden a un triangulo")
    if primerLado==segundoLado and segundoLado==tercerLado:
        print("El triangulo es equilatero")
    elif primerLado!=segundoLado and segundoLado!=tercerLado:
        print("El triangulo es escaleno")
else:
    print("No es un triangulo")



