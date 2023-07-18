personas = 20
gatos = 30
perros = 15

if personas < gatos:
    print("¡Demasiados gatos! ¡El mundo está condenado!")
elif personas > gatos:
    print("¡No hay muchos gatos! ¡El mundo está a salvo!")

if personas < perros:
    print("¡El mundo está babeado!")
elif personas > perros:
    print("¡El mundo está seco!")
else:
    print("Las personas son perros.")

if personas >= perros:
    print("Las personas son mayores o iguales que los perros.")
else:
    print("Las personas no son mayores o iguales que los perros.")

if personas <= perros:
    print("Las personas son menores o iguales que los perros.")

if personas == perros:
    print("Las personas son perros.")