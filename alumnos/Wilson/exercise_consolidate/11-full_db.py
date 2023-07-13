# Genera un script que pueda crear una base de datos de estudiantes
# con una tabla llamada estudiantes que tenga dos campos.
# Inserta un registro en la tabla estudiantes con dos campos.
# Consulta todos los registros de la tabla estudiantes y muéstralos en pantalla.
# Consulta un registro de la tabla estudiantes y muéstralo en pantalla.
# Cada ejecución del script tiene que estar en funciones separadas
import mysql.connector


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3308),
    )
    return connection


# crea la base de datos
def create_database(connection, name_database):
    create_database_sql = f"CREATE DATABASE IF NOT EXISTS {name_database};"
    return create_database_sql


# crea la tabla
def create_table(connection, name_table, name_database, columns_table):
    create_table_sql = f"CREATE TABLE IF NOT EXISTS `{name_table}`.`{name_database}` ({columns_table});"
    commit_query(connection, create_table_sql)
    return f"The table {name_table} was create in the data base {name_database}"


def commit_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


def insert_data(connection, name_database, name_table, columns, valor_to_add):
    # Insertar un registro
    insert_sql = f"INSERT INTO {name_database}.{name_table} {columns} VALUES {valor_to_add};"
    commit_query(connection, insert_sql)
    return insert_sql


def get_data(connection, name_database, name_table, column_to_select):
    # Consultar todos los registros
    select_sql = f"SELECT {column_to_select} FROM {name_table}.{name_database};"
    commit_query(connection, select_sql)
    # Obtener los resultados
    # rows = cursor.fetchall()
    # for row in rows:
    #    print(row)
    # return rows


def get_data_by_id(name_database, column_name, value_to_found):
    # Consultar todos los registros
    select_sql = f"SELECT {column_name} FROM {name_database} WHERE {column_name}={value_to_found};"


def delete_data_by_id(name_table, column, value_to_delete):
    # Consultar todos los registros
    delete_sql = f"DELETE FROM {name_table} WHERE {column} ={value_to_delete};"
    return delete_sql


def close_all_connections(connection):
    connection.close()


if __name__ == '__main__':
    conn = connection_database('127.0.0.1', 'root', 'root', 'estudiantes')
    insert_data(conn, cursor)
    get_data(conn, cursor)
    print(get_data_by_id(conn, cursor, 1))
    # delete_data_by_id(conn, cursor, 3)
    close_all_connections(conn, cursor)
