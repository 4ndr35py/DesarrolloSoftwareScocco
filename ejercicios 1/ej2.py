"""Bitcoins a Pesos
Escriba un programa que permita a una persona conocer a cuántos Pesos Argentinos
equivalen hoy los Bitcoins (BTC) que encontró guardados en un disco rígido viejo.
El usuario del programa debe ingresar una cantidad en Bitcoins."""

cantbitcoin = float(input("cant de bitcoins: "))
valorpeso = 8260873.61
rta = cantbitcoin * valorpeso
print (f"Usted tiene ${rta} pesos")