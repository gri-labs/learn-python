#Con MySQL Workbench, crea una base de datos nueva.
#Crea una tabla de usuarios con las siguientes características:
#Campo ID numérico
#Campo ID con índice primario y autonumérico
#Añade los siguientes campos:
#email
#nombre
#apellido
#edad
#Inserta datos de prueba en la tabla
#Borra los datos de prueba

DROP DATABASE IF EXISTS `gri`;
CREATE DATABASE IF NOT EXISTS `gri`;

use gri;

select * from alumnos;

SET SQL_SAFE_UPDATES = 0;

DELETE from alummnos where id= 1;

CREATE TABLE estudiantes (
	id INT PRIMARY KEY auto_increment,
    nombre VARCHAR (50),
    edad int
);

ALTER TABLE estudiantes ADD PRIMARY KEY (id);

INSERT INTO alumnos (nombre,edad) VALUES ('maria' , 20);

SHOW CREATE TABLE estudiantes;

SELECT * FROM estudiantes;

DELETE FROM estudiantes WHERE nombre = 'maria';

DROP DATABASE IF EXISTS `gri`;
CREATE DATABASE IF NOT EXISTS `gri`;

use gri;

select * from alumnos;

SET SQL_SAFE_UPDATES = 0;

DELETE from alummnos where id= 1;

CREATE TABLE estudiantes (
	id INT PRIMARY KEY auto_increment,
    nombre VARCHAR (50),
    edad int
);

ALTER TABLE estudiantes ADD PRIMARY KEY (id);

INSERT INTO alumnos (nombre,edad) VALUES ('maria' , 20);

SHOW CREATE TABLE estudiantes;

SELECT * FROM estudiantes;

DELETE FROM estudiantes WHERE nombre = 'maria';

SELECT * FROM estudiantes;

show create table estudiantes; #para ver la forma de crear la tabla

#Ricardo he intentado hacer esto pero la tabla no me salen los registros o no se verlos...
#Dice que hay 6 registros pero cuando lo exporto la tabla a excel me sale solo el nombre de las columnas.
