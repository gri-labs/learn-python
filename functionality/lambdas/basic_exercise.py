# Ejercicio lambda para python
#
# 1. Crear una función lambda que devuelva el número mayor de una lista

array_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1. Crear una función lambda que devuelva el número mayor de una lista

max_number_array = lambda array: max(array)

print(max_number_array(array_numbers))

print("Number max of array:", max_number_array(array_numbers))

# 2. Crear una función lambda que devuelva el número menor de una lista

min_number_array = lambda array: min(array)

print("Number min of array:", min_number_array(array_numbers))

# 3. Crear una función lambda que devuelva el número de elementos de una lista

len_array = lambda array: len(array)

print("Number of elements of array:", len_array(array_numbers))

# 4. Crear una función lambda que devuelva el número de elementos pares de una lista

array_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = lambda array: len([number for number in array if number % 2 == 0])

print("Number of even pars numbers of array:", even_numbers(array_numbers))
