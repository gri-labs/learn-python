#Ejercicio 3:
# Crea tu propia clase
# Genera una nueva PR

class One_Piece_Character:
    def __init__(self, name):
        self.name = name

    def get_power(self):
        if self.name == "Luffy":
            return "Es el capitan y es de goma"
        elif self.name == "Zoro":
            return "Espadacin maestro de la tecnica Three sword estyle"
        elif self.name == "Usopp":
            return "es un cobarde pero es un fucking sniper con las tirachinas"
        else:
            return "No hay personaje con este nombre"


name = input("Ingrese el nombre del personaje: ")

character = One_Piece_Character(name)

power = character.get_power()

print(f'el poder de {name} es:', power)