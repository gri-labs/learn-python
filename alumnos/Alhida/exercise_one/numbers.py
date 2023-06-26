def numbers_pares(numbers):
    pares = []
    for num in numbers:
        if num % 2 == 0:
            pares.append(num)
    return pares

def numbers_impar(numbers):
    impares = []
    for num in numbers:
        if num % 2 != 0:
            impares.append(num)
    return impares
