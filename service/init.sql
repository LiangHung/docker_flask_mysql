CREATE DATABASE IF NOT EXISTS user;
use user;

CREATE TABLE IF NOT EXISTS `Users` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(80),
    `email` VARCHAR(80),
    `password` VARCHAR(50),
    PRIMARY KEY (id)
);

ALTER TABLE User AUTO_INCREMENT = 1;

INSERT INTO `Users`
  (username,email,password)
VALUES
  ('test11', 'aaa@gamil.com','123456');


