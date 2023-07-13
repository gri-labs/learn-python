def contar_letras(palabra):
    return len(palabra)

palabra = input("Ingresa una palabra: ")
cantidad_letras = contar_letras(palabra)
print("La palabra", palabra, "tiene", cantidad_letras, "letras")
