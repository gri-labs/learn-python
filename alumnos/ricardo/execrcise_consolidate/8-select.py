import mysql.connector

connection = mysql.connector.connect(
    host=,
    user=,
    password=,
    database=
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Consultar todos los registros
select_sql = """
SELECT * FROM estudiantes
"""

cursor.execute(select_sql)

# Obtener los resultados
rows = cursor.fetchall()

# Mostrar los resultados
for row in rows:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
connection.close()