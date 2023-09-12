# Función llamada my_decorator, que toma como argumento una función func.
# Dentro de my_decorator, definimos una función anidada llamada wrapper,
# que está recubriendo la función func.
def my_decorator(func):
    # Wrapper coloca código que se ejecutará antes y después de la función func.
    def wrapper():
        # En este caso, antes de llamar a func(), se imprime "Something is happening before the function is called.",
        # y después de llamar a func(), se imprime "Something is happening after the function is called."
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    # Finalmente, la función wrapper se devuelve como resultado de my_decorator.
    return wrapper


# Se define la función say_hello, que imprime "Hello!".
# La función say_hello se pasa como argumento a my_decorator.
# Utilizando @my_decorator, se aplica el decorador my_decorator a la función say_hello.
# Cuando se llama a say_hello(), en realidad se llama a wrapper().
@my_decorator
def say_hello():
    print("Hello!")


say_hello()
