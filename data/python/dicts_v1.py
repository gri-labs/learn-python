my_dict = {
    "nombre": "Juan",
    "edad": 25
}

# Obtener llave
name = my_dict["nombre"]

print("Nombre: ", name)

# Modificar llave
my_dict["edad"] = 30

print("Edad: ", my_dict["edad"])

# Agregar llave
my_dict["apellido"] = "Perez"

print("Apellido: ", my_dict["apellido"])

# Eliminar llave
del my_dict["apellido"]

if "appellido" not in my_dict:
    print("No existe el apellido")

# Existe la llave
if "edad" in my_dict:
    print("Si existe el edad")

# Recorrer las llaves
for key in my_dict:
    print(key, ":", my_dict[key])

# Recorrer los pares
for key, value in my_dict.items():
    print(key, ":", value)

# Recorrer los valores
for value in my_dict.values():
    print(value)


alumnos = {
    "alumno1": {"nombre": "Juan", "edad": 25},
    "alumno2": {"nombre": "María", "edad": 30}
}