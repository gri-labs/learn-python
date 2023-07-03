import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=int(3307),
    database="mysql"
)

# Crear un cursor para ejecutar sentencias SQL
connection.connect()
cursor = connection.cursor()
# Borrar un registro
delete_sql = "USE ´estudiantes´; DELETE FROM estudiantes WHERE nombre=Alex"

# Ejecutar los cambios en la base de datos
cursor.execute(delete_sql)
# Confirmar los cambios en la base de datos
connection.commit()
# Cerrar el cursor y la conexión
cursor.close()
connection.close()