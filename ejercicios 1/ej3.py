
compra = float(input("ingrese el monto de la compra: "))
if compra > 3499:
    rta = compra - (compra * 0.1)
    print (f"su compra con descuento es de {rta}")
else:
    print (f"el total de su compra es de {compra}")
