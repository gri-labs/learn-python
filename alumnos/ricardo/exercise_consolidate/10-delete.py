import mysql.connector

connection = mysql.connector.connect(

)

# Crear un cursor para ejecutar sentencias SQL

# Es borrar un registro
delete_sql = "DELETE FROM estudiantes WHERE nombre = 'ricardo';"

# Ejecutar los cambios en la base de datos

# Confirmar los cambios en la base de datos

# Cerrar el cursor y la conexión
