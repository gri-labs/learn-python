
-- Obtener el id del usuario que su nombre es Juan.
SELECT id FROM usuarios WHERE nombre = 'Juan';

-- Inserta en la base de datos, el usuario Juan, con nombre, apellido y correo. La tabla tiene auto númerico.
INSERT INTO usuarios (nombre, apellido, correo) VALUES ('Juan', 'Suarez', 'juan@suarez.com');
-- (El campo id es autoincremental, no es necesario especificarlo)

-- Actualizar el campo edad de Juan a 60 años.
UPDATE usuarios SET edad = 60 WHERE nombre = 'Juan';
