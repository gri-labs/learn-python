import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='estudiantes',
    port=int(3308),
)

# Crear el objeto cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = ""

# Ejecutar los cambios en la base de datos

# Confirmar los cambios en la base de datos

# Cerrar el cursor y la conexión