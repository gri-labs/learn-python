import mysql.connector

connection = mysql.connector.connect(
    host=,
    user=,
    password=
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = """
INSERT INTO estudiantes (nombre, carrera)
VALUES ('Ricardo', 'Ingeniería en Sistemas')
"""

# Ejecutar los cambios en la base de datos
cursor.(insert_sql)

# Confirmar los cambios en la base de datos
connection.()

# Cerrar el cursor y la conexión
cursor.()
.close()