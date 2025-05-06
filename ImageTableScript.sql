CREATE DATABASE kchsdb;
USE kchsdb;

CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(150) UNIQUE NOT NULL,
	password_hash VARCHAR(200) NOT NULL
);

CREATE TABLE images (
	id INT AUTO_INCREMENT PRIMARY KEY,
	Title VARCHAR(255) NOT NULL,
	dateTaken DATE,
	Link TEXT,
 	Descript TEXT
);

INSERT INTO users (username, passcode)
VALUES ('Username','Passphrase'); -- Switch these with the username and password of the new user.

SELECT * FROM users; -- Displays all user information

DROP TABLE users; -- Run this if you intend to delete the "users" table (clears EVERYTHING)
DROP TABLE images; -- Run this if you intend to delete the "images" table (clears EVERYTHING)
