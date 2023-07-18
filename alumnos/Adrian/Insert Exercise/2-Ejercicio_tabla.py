#Ejercicio 2

USE gri;

CREATE TABLE pitufos (
	id INT (11) auto_increment,
    nombre VARCHAR (255),
    edad int,
    email VARCHAR(100),
    PRIMARY KEY (id)
) ENGINE= InnoDB;

insert into pitufos (nombre,edad,email) VALUES ('pepito',20,'pepito@gmail.com');

alter table pitufos ADD apellido VARCHAR(50); #esto es para añadir una columna

show create table pitufos;

select * from pitufos; #asi ves la tabla con los valores
