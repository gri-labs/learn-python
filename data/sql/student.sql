CREATE DATABASE school;

USE school;

CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `dni` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);

SELECT * FROM students WHERE last_name LIKE '%Garcia%';
SELECT COUNT(*) FROM students WHERE last_name LIKE '%Garcia%';
SELECT * FROM students WHERE age BETWEEN 5 AND 25;
SELECT * FROM students WHERE age > 25;
SELECT COUNT(*) FROM students WHERE age > 25;


ALTER TABLE students
ADD created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
ADD updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP;

SELECT COUNT(*) FROM students WHERE YEAR(created_at) = 2023;
SELECT COUNT(*) FROM students WHERE YEAR(created_at) = 2023 AND MONTH(created_at) = 4;
SELECT COUNT(*) FROM students WHERE created_at BETWEEN '2022-01-01' AND '2023-04-30';