import random

def generar_lista_de_atletas():
	"""
	Esta función genera aleatoriamente los datos de 20 atletas que participaron de una maratón.
	Devuelve una lista de atletas donde cada atleta es un diccionario con los campos:
		- nombre: el nombre del atleta
		- numero: el número con el que participó en la maratón
		- tiempo_llegada: la cantidad de segundos que tardó en llegar
	"""
	lista_atletas = []
	nombres = ('Daniel', 'Alejandro', 'Pablo', 'Hugo', 'Álvaro', 'Adrián', 'David', 'Sergio', 'Diego')
	apellidos = ('García', 'Rodríguez', 'González', 'Fernández', 'López', 'Martínez', 'Sanchez', 'Pérez')	
	for i in range(1, 21):
		atleta = {
			"nombre": random.choice(nombres)+" "+random.choice(apellidos),
			"numero": i,
			"tiempo_llegada": round(random.random()*120, 2)
		}
		lista_atletas.append(atleta)
	return lista_atletas
"""1.Utilizar la función anterior para generar y almacenar una lista de atletas
2.Escribir una función que reciba la lista de atletas e imprima una línea por cada atleta respetando el siguiente formato:
"<num_atleta> - : (<tiempo_llegada> segundos)", donde <num_atleta> es el número del atleta, su nombre y <tiempo_llegadad>
su tiempo de llegada.
3.Escribir una función que devuelva el número del atleta que resultó ganador.
4.Escribir una función que, recibiendo el número de atleta de un competidor, devuelva todos sus datos
(nombre, número y tiempo de llegadad).
5.OPCIONAL: Escribir una función que devuelva una tupla con los números de los 3 atletas que entraron al podio de 
ganadores en orden de llegada."""
lista_atletas=generar_lista_de_atletas()
def mostrar_atletas(lista):
	for elem in lista:
		print(f'{elem["numero"]} - {elem["nombre"]} : {elem["tiempo_llegada"]} segundos')
mostrar_atletas(lista_atletas)

def atleta_ganador(lista):
	tiempo_menor = 120
	ganador=None
	for elem in lista:
		if tiempo_menor > elem["tiempo_llegada"]:
			ganador=elem["numero"]
			tiempo_menor = elem["tiempo_llegada"]
	return ganador
ganador=atleta_ganador(lista_atletas)
print(f"el ganador es: {ganador}")

def datos_atleta(lista, ganador):
	for elem in lista:
		if ganador == elem["numero"]:
			return [elem["numero"], elem["nombre"], elem["tiempo_llegada"]]
datos_ganador=[]
datos_ganador=datos_atleta(lista_atletas, ganador)
print(f'el ganador es: {datos_ganador}')

def obtener_podio(lista_atletas):
    lista_atletas_ordenada = sorted(lista_atletas, key=lambda x: x["tiempo_llegada"])
    podio = ()
    for puesto, atleta in enumerate(lista_atletas_ordenada[:3], start=1):
        puesto_nombre = f"{puesto}"
        nombre = atleta["nombre"]
        numero = atleta["numero"]
        tiempo_llegada = atleta["tiempo_llegada"]
        podio += ((puesto_nombre, nombre, numero, tiempo_llegada),)
    return podio
podio_ganadores = obtener_podio(lista_atletas)
print("Podio de ganadores:")
for atleta in podio_ganadores:
    print("Puesto:", atleta[0])
    print("Nombre:", atleta[1])
    print("Número:", atleta[2])
    print("Tiempo de llegada:", atleta[3])
    print("-" * 30)
