import mysql.connector

connection = mysql.connector.connect(
    host= 'localhost',
    user=,'root',
    password= 'root',
    database='gri',
    port= int(3308)
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Consultar todos los registros
select_sql = "SELECT * FROM estudiantes"

# Ejecutar los cambios de la base de datos
cursor.execute(select_sql)

# Obtener los resultados. El Fetcchall recoge todos los datos que ha generado la query.
rows = cursor.fetchall()

# Mostrar los resultados. el row sera una array y lo tengo que interar con un for
for row in rows:
    print(row)

# Cerrar el cursor y la conexión
cursor.close()
connection.close()
