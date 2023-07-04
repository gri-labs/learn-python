import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=int(3307),
    database='patatas'
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# borra todos los registros
delete_sql = "DELETE FROM patatas_tipo;"

# Ejecutar los cambios en la base de datos
cursor.execute(delete_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()