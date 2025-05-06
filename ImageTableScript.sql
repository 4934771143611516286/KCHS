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

DELETE FROM users WHERE id = 0; -- Run this line if you want to delete an entry where the login information is wrong, just replace the 0 with the id you want to delete. 
