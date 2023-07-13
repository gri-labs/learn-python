from mystuff import MyStuff

# Instanciamos el objeto MyStuff de la clase MyStuff es muy similar a llamar a una función.
# Sin embargo, cuando la llamas, Python coordina una secuencia de eventos.
# Python busca MyStuff() y ve que es una class que has definido.
# Python crea un objeto vacío con todas las funciones que has especificado en la clase MyStuff
# Python luego busca si has creado una función especial "init" (conocida como "constructor"), y si la has definido,
# llama a esa función para inicializar tu objeto vacío recién creado.
# En la función init de la clase MyStuff, obtengo esta variable adicional llamada "self",
# que es el objeto vacío que Python ha creado para mí, y puedo establecer variables en él.
# En este caso, establezco self.tangerine en una cadena, que también podría haber pasado directamente.
thing = MyStuff()
thing.apple()
print(thing.tangerine)

