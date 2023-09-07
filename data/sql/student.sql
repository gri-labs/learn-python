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