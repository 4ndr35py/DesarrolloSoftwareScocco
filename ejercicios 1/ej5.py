"""Franco está organizando un asado con sus amigos y necesita de tu ayuda.
Para estimar cuánta carne necesita comprar, va a suponer que cada invitado come 0.7 Kg de carne.
Ayuda a Franco escribiendo un programa que permita al usuario ingresar la cantidad de invitados y el precio de 1Kg.
de carne, y muestre cuántos Kg de carne en total debe pedir al carnicero y cuánto dinero necesita para pagar"""
cantinvitados = int(input("ingrese la cantdidad de invitados: "))
preciokgcarne = float(input("ingrese el precio de la carne: "))
kgtotal = cantinvitados * 0.7
totalplata = kgtotal * preciokgcarne
print(f"Usted debe comprar {kgtotal: .2f}kg de carne, gastando ${totalplata: .2f}")