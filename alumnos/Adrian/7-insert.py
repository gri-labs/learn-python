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

# Insertar un registro
insert_sql = "INSERT INTO ESTUDIANTES ('id', 'nombre') VALUES (1, 'Adrian') "


# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()
