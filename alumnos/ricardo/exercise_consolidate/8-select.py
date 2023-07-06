import mysql.connector

connection = mysql.connector.connect(
)

# Crear un cursor para ejecutar sentencias SQL

# Consultar todos los registros
select_sql = "SELECT * FROM `estudiantes`.`estudiantes`;"

# Ejecutar los cambios en la base de datos
cursor.execute(select_sql)
# Obtener los resultados
rows = cursor.fetchall()

# Mostrar los resultados

# Cerrar el cursor y la conexión
