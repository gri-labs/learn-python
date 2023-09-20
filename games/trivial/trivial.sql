CREATE DATABASE trivial;

USE trivial;

CREATE TABLE `questions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(255) NOT NULL,
  `answer` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO questions (question, answer, category) VALUES ('¿Cuál es la capital de España?', 'Madrid', 'Geografía');
INSERT INTO questions (question, answer, category) VALUES ('¿Cuál es la capital de Francia?', 'París', 'Geografía');
INSERT INTO questions (question, answer, category) VALUES ('¿Cuál es la capital de Italia?', 'Roma', 'Geografía');
INSERT INTO questions (question, answer, category) VALUES ('¿Cuál es la capital de Portugal?', 'Lisboa', 'Geografía');


CREATE TABLE `score` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `points` int(11) NOT NULL,
  PRIMARY KEY (`id`)
);