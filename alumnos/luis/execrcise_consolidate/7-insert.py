import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = """
INSERT INTO estudiantes (nombre, carrera)
VALUES ('luis', 'estudiante')
"""

# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()
