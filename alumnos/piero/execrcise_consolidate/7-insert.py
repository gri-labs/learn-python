import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    port=int(3307),
    database='patatas'
)

# Crear un cursor para ejecutar sentencias SQL
cursor = connection.cursor()

# Insertar un registro
insert_sql = """
INSERT INTO patatas_tipo (id, Tipo, Precio_kg)
VALUES (1, 'Rojas', 3.20)
"""

# Ejecutar los cambios en la base de datos
cursor.execute(insert_sql)

# Confirmar los cambios en la base de datos
connection.commit()

# Cerrar el cursor y la conexión
cursor.close()
connection.close()