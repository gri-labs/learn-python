class Guitarra(object):

    def __init__(self, modelo, color, registro):
        self.modelo = modelo
        self.color = color
        self.registro = registro

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_registro(self):
        return self.registro

guitarra1 = Guitarra("Stratocaster", "Negra", 440)
print(guitarra1.modelo, guitarra1.color, guitarra1.registro)