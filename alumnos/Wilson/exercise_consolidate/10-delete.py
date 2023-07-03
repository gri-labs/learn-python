import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='estudiantes',
    port=int(3308),
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Consultar todos los registros
delete_sql = "DELETE FROM estudiantes WHERE id=1;"

# Ejecutar los cambios en la base de datos
cursor.execute(delete_sql)

# Confirmar los cambios en la base de datos
connection.commit()
# Cerrar el cursor y la conexión
cursor.close()
connection.close()