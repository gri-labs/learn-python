import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database=mysql,
    port=int(3307),
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Consultar todos los registros
select_sql = """
SELECT * FROM mysql
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
