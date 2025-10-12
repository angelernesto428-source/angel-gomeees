--ejercicio1


CREATE DATABASE cursos;

USE cursos;
,
CREATE TABLE estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    activo BOOLEAN DEFAULT TRUE
);

--ejercicio 2

INSERT INTO Empleados (id, nombre, email, activo) VALUES
(1, 'Angel Gómez', 'angel.gomez@email.com', 'TRUE'),
(2,'jose luis', 'jose.luis@email.com', 'FALSE'),
(3,'manuel perez', 'manuel@email.com', 'TRUE'),
(4,'penelope lopez', 'lopez.pene@email.com', 'FALSE'),
(5,'ana rubio', 'anarubio@email.com', 'FALSE');

--ejercicio 3

SELECT * FROM Empleados WHERE id = 1;

SELECT nombre, email FROM Empleados;

--ejrcicoo 4

SELECT * FROM Empleados WHERE nombre = 'ana rubio' AND activo = TRUE;


--aplica si esta en true osea activa

--ejercicio 5

UPDATE Empleados
SET email = 'anarubio.nuevo@email.com'
WHERE id = 5;

-- ejrcicio 6

DELETE FROM Empleados WHERE id = 3;

-- ejercicio 7

SELECT * FROM Empleados ORDER BY nombre, id;

--nota no me quisp agarrar este codigo

--gracias por el curso profe nomas termine lo que sabia y espero que con el de pythpn si me da el gusto de pasar pueda aprender mas de lo que me interesa porque esto de la programacion me gusta :v