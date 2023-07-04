import mysql.connector

# Establecer la conexión con la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=int(3307),
    database='patatas'
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Crear una base de datos
create_database_sql = "CREATE DATABASE IF NOT EXISTS patatas;"

# Ejecutar la sentencia para crear la base de datos
cursor.execute(create_database_sql)

# Crear una tabla
create_table_sql = "CREATE TABLE IF NOT EXISTS patatas_tipo (id INTEGER NOT NULL, Tipo VARCHAR(50), Precio_kg INT);"

# Ejecutar la sentencia para crear la tabla
cursor.execute(create_table_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()