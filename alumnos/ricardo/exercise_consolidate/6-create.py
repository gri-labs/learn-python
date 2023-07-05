import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=int(3308),
    database='mysql',
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Crear una base de datos
create_database_sql = "CREATE DATABASE IF NOT EXISTS gri;"

# Crear una tabla
create_table_sql = "CREATE TABLE IF NOT EXISTS `gri`.`estudiantes` (id INT, nombre VARCHAR(255));"

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
