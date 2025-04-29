The Python script that adds and removes entries and creates HTML files from the MySQL database requires mysql.connector, which is installed using Pip, in addition to a locally-hosted MySQL server with a database. The script will not work otherwise.


KCHS Project - How to Run the Login System
===========================================

1. Download or clone the project folder:
   - It must look like:
     /KCHS_project/
     ├── app.py
     ├── templates/
         ├── login.html
         ├── register.html
         ├── photos.html

2. Install Python packages:
   Open Terminal/Command Prompt and run:

   pip3 install flask mysql-connector-python werkzeug

3. Set up the MySQL database:
   In MySQL shell:

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

4. Update app.py:
   - Make sure your MySQL connection matches your local username/password.
   - Change the app.secret_key to a strong random string.

5. Run the app:
   Navigate to the project folder:

   cd /path/to/KCHS_project
   python3 app.py

6. Open in browser:
   Visit http://127.0.0.1:5000/

7. Register and Login:
   - Register a new account.
   - Login using your new username and password.
   - After login, a spinner appears and then redirects to the Photos page.

NOTES:
- You must have MySQL server running.
- Always run "python3 app.py" from the project folder.
- If any errors occur, check your database setup or file structure.
