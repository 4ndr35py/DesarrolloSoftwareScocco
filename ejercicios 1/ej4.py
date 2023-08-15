"""Un club deportivo tiene 4 categorías de asociados según la edad:
infantiles (desde 13 a 15 años)
cadetes (a partir de los 15 y hasta 17)
juveniles (desde los 17 hasta los 19)
mayores (de 19 años en adelante)
Escriba un programa que permita al usuario ingresar el nombre y la edad de un socio y muestre su el nombre de la
categoría en la que le corresponde estar.
"""
nombre = input("ingrese el nombre: ")
edad = int(input("ingrese edad: "))
if edad <15 and edad>12:
    categoria = "infantil"
elif edad>14 and edad<19:
    categoria = "juvenil"
elif edad>18:
    categoria = " mayor"
else:
    print("edad no valida")    
print (f"{nombre} de {edad} anos pertenece a la categoria {categoria}")