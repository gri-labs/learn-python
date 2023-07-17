import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='estudiantes',
    port=int(3307),
)

# Crear el objeto cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = "INSERT INTO estudiantes (id, nombre, gmail) VALUES ( 1, 'alhida', 'alhidallanos@gmail.com');"

# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()


# Cerrar el cursor y la conexión
cursor.close()
connection.close()