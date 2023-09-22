CREATE DATABASE IF NOT EXISTS import_sql;

USE import_sql;

CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    departamento VARCHAR(50),
    salario DECIMAL(10, 2)
);

INSERT INTO empleados (nombre, departamento, salario)
VALUES
    ('Juan', 'Ventas', 50000.00),
    ('Ana', 'Marketing', 55000.00),
    ('Pedro', 'TI', 60000.00),
    ('María', 'Marketing', 52000.00),
    ('Carlos', 'Ventas', 48000.00),
    ('Luis', 'TI', 62000.00),
    ('Laura', 'Recursos Humanos', 58000.00),
    ('Marta', 'Recursos Humanos', 55000.00);