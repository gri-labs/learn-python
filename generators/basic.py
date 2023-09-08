def funcion_generadora():
    for i in range(10):
        yield i


for item in funcion_generadora():
    print(item)