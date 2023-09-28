from types import MappingProxyType
from collections import ChainMap
from collections import defaultdict

mi_diccionario = {"nombre": "Juan", "edad": 30}

diccionario_inmutable = MappingProxyType(mi_diccionario)

print(diccionario_inmutable)

# diccionario_inmutable["nombre"] = "Pedro"

#####################

dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
combined = ChainMap(dic1, dic2)

print(combined)

#####################

mi_diccionario = defaultdict(int)  # Valor predeterminado para claves no existentes es 0

mi_diccionario["edad"] = 30

print(mi_diccionario["altura"])  # Devuelve 0 en lugar de generar un error
