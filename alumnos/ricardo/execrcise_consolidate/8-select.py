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
select_sql = ""

# Ejecutar los cambios en la base de datos
cursor.execute()

# Obtener los resultados
rows = cursor.fetchall()

# Mostrar los resultados

# Cerrar el cursor y la conexión