'''Calcule el promedio de goles anotados por un jugador en cuatro encuentros, solo
si la suma de estos es mayor a 10; de lo contrario imprimir “No se pide determinar
el promedio”.'''
primerEncuentro=int(input("Ingrese los goles del jugador en el primer encuentro"))
segundoEncuentro= int(input("Ingrese los goles del jugador en el segundo encuentro"))
tercerEncuentro= int(input("Ingrese los goles del jugador en el tercer encuentro"))
cuartoEncuentro= int(input("Ingrese los goles del jugador en el cuarto encuentro"))
totalGoles= primerEncuentro+segundoEncuentro+tercerEncuentro+cuartoEncuentro
promedio= totalGoles//4
if totalGoles >=10:
  print("El promedio de goles anotados por el jugador es:",promedio)
else:
  print("No se pide determinar el promedio")