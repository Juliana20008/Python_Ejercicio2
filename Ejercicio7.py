'''En las pruebas de ICFES, se presentan dos tipos de prueba: Una de aptitud
matemática y otra de lenguaje. Leer los puntajes obtenidos por un estudiante en
cada prueba e imprimir en cual obtuvo mayor puntaje. Tenga en cuenta que
ambos puntajes podrían ser iguales.'''
aptitudMatematica= float(input("Ingrese el puntaje de la aptitud matematica en las pruebas ICFES:"))
aptitudLenguaje= float(input("Ingrese el puntaje de la aptitud de lenguaje en la pruebas ICFES:"))
if aptitudMatematica>aptitudLenguaje:
    print("La aptitud de mejor puntaje es la de matematicas con", aptitudMatematica)
elif aptitudMatematica<aptitudLenguaje:
    print("La aptitud de mejor puntaje es la de lenguaje con", aptitudLenguaje)
else:
    print("Los dos resultados tienen el mismo puntaje por lo tanto no hay una aptitud con mejor puntaje")