from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for sessions
bcrypt = Bcrypt(app)  # Initialize Flask-Bcrypt

# DB connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_db_user",
        password="your_db_password",
        database="your_db_name"
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Insert into database
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        db.commit()
        db.close()

        return redirect('/login')  # Redirect to login page after successful registration

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        db.close()

        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = user['username']
            return redirect('/photos')
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>."
    
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)

