from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for sessions

# DB connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="your_db_user",
        password="your_db_password",
        database="your_db_name"
    )

@app.route('/')
def index():
    if 'username' in session:
        return redirect('/photos')
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        db.close()

        if user:
            session['username'] = user['username']
            return redirect('/photos')
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>."
    
    return render_template('login.html')
