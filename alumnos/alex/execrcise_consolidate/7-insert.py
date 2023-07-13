import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=int(3307),
    database="mysql"
)
# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = """
INSERT INTO `estudiantes`.`estudiantes` (id, nombre, carrera)
VALUES (1, 'Jesús', 'Diseño')
"""

# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()