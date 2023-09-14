class Animal:
    def __init__(self, name):
        self.name = name


class Horse(Animal):
    def __init__(self, name, race):
        # super() llama al constructor de la clase padre
        # no siempre es necesario llamar al constructor de la clase padre
        # pero es una buena práctica hacerlo
        super().__init__(name)
        self.race = race

    def speaking(self):
        return "jiiiiiiiiiiii"


specific_horse = Horse("Caballo Específico", "Pura Sangre")

print(f"{specific_horse.name} es un Animal: {isinstance(specific_horse, Animal)}")
