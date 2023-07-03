import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='estudiantes',
    port=int(3307),
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Consultar todos los registros
# delete_sql = "SELECT * FROM estudiantes;"
consulta_sql = "SELECT * FROM estudiantes;"

# Ejecutar los cambios en la base de datos
cursor.execute(consulta_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()
