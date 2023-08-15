"""generar una lista con 10 valores enteros aleatorios entre 1 y 20 (se puede usar randint() del módulo random). Luego:
Muestre la lista
El usuario ingresa debe ingresar un valor un valor. El programa debe informar cuántos valores de la lista son mayores a dicho valor,
para eso debe utilizar una función. La función debe recibir como argumentos la lista y un entero, y 
debe retornar la cantidad de valores de la lista mayores a dicho entero.
Crear una función que calcule el promedio de la lista y utilizarla.
Crear una función que encuentre el valor más grande y el más pequeño de la lista y los retorne."""
import random

def generate_random_number():
    return random.randint(1, 20)

random_numbers = []

while len(random_numbers) < 10:
    random_num = generate_random_number() 
    if random_num not in random_numbers:
        random_numbers.append(random_num) 
print("random numbers list:", random_numbers)

def display_numbers_above_threshold(numbers_list, threshold):
    above_threshold = [num for num in numbers_list if num > threshold]
    return above_threshold
user_input = int(input("Enter a minimun: "))
numbers_above_input = display_numbers_above_threshold(random_numbers, user_input)
print("Numbers above the input:", numbers_above_input)

def calculate_average(numbers_list):
    total_sum = sum(numbers_list)
    list_length = len(numbers_list)
    result = total_sum / list_length
    return result
avg = calculate_average(random_numbers)
print("Average:", avg)

def find_smallest_largest(numbers_list):
    smallest = min(numbers_list)
    largest = max(numbers_list)
    return [smallest, largest]
result = find_smallest_largest(random_numbers)
smallest, largest = result
print(f"Smallest {smallest} Largest: {largest}")