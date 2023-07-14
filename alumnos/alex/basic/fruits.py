# Que es una clase?
# Una clase es como un molde para crear objetos. Siempre empieza con mayúscula.
# Una clase define un tipo de objeto
class Fruits:
    # La función __init__ es un constructor, se ejecuta cuando se crea un objeto de la clase.
    # El constructor se usa para asignar valores a las variables de la clase
    # o cualquier otra operación que sea necesaria, como heredar de otra clase.
    # En este ejemplo __init__ asigna el valor "Y ahora mil años entre medio" a la variable tangerine
    # cuando se crea un objeto.
    # El primer parámetro de __init__ es self, que es una referencia al objeto actual.
    # Los otros parámetros son los que se pasan al constructor al crear el objeto.
    # por ejemplo melon
    def __init__(self, apple):
        self.tangerine = "Y ahora mil años entre medio"
        self.apple = apple

    # Las funciones dentro de una clase se llaman métodos.
    # Todos los métodos deben tener self como primer parámetro.
    # Los métodos son funciones que pertenecen a una clase.
    def get_apple(self):
        print("¡SOY UNA %s ELEGANTE!" % self.apple)

    def get_melon(self, melon):
        print("¡SOY UN %s ELEGANTE!" % melon)
