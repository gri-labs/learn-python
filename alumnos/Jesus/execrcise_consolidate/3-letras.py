# Contar la cantidad de letras en una palabra utilizando una función:

def contar_letras(palabra):
    return len(palabra)


palabra = input("Ingresa una palabra: ")
res = contar_letras(palabra)
print("La palabra", palabra, "tiene", res, "letras")
