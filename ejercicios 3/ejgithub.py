valor1=None
valor2=None

decision=0
menu="\n1. Ingresar valor 1 \n2. Ingresar valor 2 \n3. Mostrar suma \n4. Mostrar resta \n5. Mostrar multiplicación\n6. Mostrar división\n7. Salir"
while decision!=7:
    print(f'{menu}')
    decision=int(input("Elija una opcion: "))
    if decision==1:
        valor1=int(input("Ingrese el primer valor: "))
    if decision==2:
        valor2=int(input("Ingrese el segundo valor: "))
    if decision==3:
        suma = valor1 + valor2
        print(f'La suma es: {suma}')
    if decision==4:
        resta = valor1 - valor2
        print(f'La resta es: {resta}')
    if decision=='5':
        multiplicacion = valor1 * valor2
        print(f'La multiplicacion es: {multiplicacion}')
    if decision==6:
        division = valor1 % valor2
        print(f'La division es: {division}')
    if decision==7:
        print("chau")
    input("Ingrese ENTER para continuar:")
