import mysql.connector

connection = mysql.connector.connect(
    host= 'localhost',
    user='root',
    password='root',
    port=int(3307),
    database='mysql'
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Crear una base de datos
create_database_sql = "CREATE DATABASE IF NOT EXISTS patatas;"

# Crear una tabla
create_table_sql = "CREATE TABLE patatas_tipo (id	INTEGER NOT NULL, Tipo VARCHAR (50), Precio_kg INT);"

# Ejecutar los cambios en la base de datos
cursor.execute(create_database_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Ejecutar la sentencia para crear la tabla
cursor.execute(create_table_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()