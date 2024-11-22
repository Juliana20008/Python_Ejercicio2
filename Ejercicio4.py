'''Desarrolle un algoritmo que ingrese dos números y luego los imprima de forma
ascendente.(primero se imprime el menor y luego el mayor)'''
primerNumero= int(input("ingrese el primer numero:"))
segundoNumero= int(input("ingrese el segundo numero:"))
if primerNumero<segundoNumero:
   print("Los numeros de forma ascendente son:",primerNumero,segundoNumero)
else:
   print("Los numeros de forma ascendente son:", segundoNumero, primerNumero)