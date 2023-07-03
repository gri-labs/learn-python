import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=int(3307),
    database="mysql"
)
connection.connect()
# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = """
INSERT INTO `estudiantes`.`estudiantes` (nombre, carrera)
VALUES ('Alex', 'Matemáticas')
"""

# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()