# Contar la cantidad de letras en una palabra utilizando una función:

def contar_letras(palabra):
    return len(palabra)


palabra = input("Ingresa una palabra: ")
cantidad_letras = contar_letras(palabra)
print("La palabra", palabra, "tiene", cantidad_letras, "letras")
