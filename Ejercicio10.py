'''. Elabore un algoritmo que lea el nombre, la edad, el sexo (F: Femenino, M:
masculino) y el estado civil(1:Casado,2:soltero,3:Separado,4: otro) de una persona
que desea participar en las elecciones este año. Si es menor de edad imprimir
mensaje que diga que no puede votar, de lo contrario imprimir el mensaje
indicado la mesa en la cual le corresponde votar.
'''

nombre=str(input("Ingrese el nombre"))
edad= int(input("Ingrese la edad:"))
sexo=input("Ingresar tu genero (F:femenino, M:masculino):")
sexo1=sexo.upper()
estadoCivil= input("Ingresar su estado civil 1:Casado,2:soltero,3:Separado,4: otro ")
estado1=estadoCivil.upper()
if edad<18:
    print("Es menor de edad por lo cual usted no puede votar")
elif sexo=="F" and estadoCivil=="casada":
    print("Usted vota en la mesa 1")
elif sexo=="F" and estadoCivil=="soltera":
    print("Usted vota en la mesa 2")
elif sexo=="F" and estadoCivil=="separada":
    print("Usted vota en la mesa 3")
elif sexo=="F" and estadoCivil=="otro":
    print("Usted vota en la mesa 4")
elif sexo=="M" and estadoCivil=="casado":
    print("Usted vota en la mesa 5")
elif sexo=="M" and estadoCivil=="soltero":
    print("Usted vota en la mesa 6")
elif sexo=="M" and estadoCivil=="separado":
    print("Usted vota en la mesa 7")
elif sexo=="M" and estadoCivil=="otro":
    print("Usted vota en la mesa 8")



