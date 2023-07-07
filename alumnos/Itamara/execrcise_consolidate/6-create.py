import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=3307,
    database="alumnos"
)

connection.connect()

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Crear una base de datos
create_database_sql = "CREATE DATABASE IF NOT EXISTS alumnos;"

# Crear una tabla
create_table_sql = "CREATE TABLE 'alumnos'.'estudiantes' (id INT, nombre VARCHAR(50), telefono INT);"

# Ejecutar los cambios en la base de datos
cursor.execute(create_database_sql)
# Confirmar los cambios en la base de datos
connection.commit()
# Ejecutar los cambios en la base de datos
cursor.execute(create_table_sql)
# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()