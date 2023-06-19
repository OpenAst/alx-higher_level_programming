-- Script that creates a database if missing

CREATE DATABASE IF NOT EXISTS physiology;
USE physiology;
CREATE TABLE IF NOT EXISTS gns(
	matric_no INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (matric_no)
	);

INSERT INTO gns(matric_no, name) VALUES (190673, "Ogunlolu Rhoda Ore");
INSERT INTO gns(matric_no, name) VALUES (191349, 'Victor');
INSERT INTO gns(matric_no, name) VALUES (180223, 'Favour');
