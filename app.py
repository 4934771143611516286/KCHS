from flask import Flask, request, redirect, session, send_file
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_username",
    password="your_mysql_password",
    database="importtestdb"
)
cursor = db.cursor()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM logininfotable WHERE username=%s AND passcode=%s", (username, password))
        user = cursor.fetchone()

        if user:
            session['user'] = username
            return f"<h2>Welcome, {username}!</h2><p><a href='/logout'>Logout</a></p>"
        else:
            return "<h2>Invalid login</h2><p><a href='/login'>Try again</a></p>"

    return send_file('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM logininfotable WHERE username=%s", (username,))
        if cursor.fetchone():
            return "<h2>Username already exists</h2><p><a href='/register'>Try again</a></p>"

        cursor.execute("INSERT INTO logininfotable (username, passcode) VALUES (%s, %s)", (username, password))
        db.commit()
        return "<h2>Registration successful!</h2><p><a href='/login'>Login here</a></p>"

    return send_file('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

