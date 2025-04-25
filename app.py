from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

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
            return f"Welcome, {username}! You are now logged in."
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>."

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username exists
        cursor.execute("SELECT * FROM logininfotable WHERE username=%s", (username,))
        if cursor.fetchone():
            return "Username already taken. <a href='/register'>Try another</a>."

        # Insert new user
        cursor.execute("INSERT INTO logininfotable (username, passcode) VALUES (%s, %s)", (username, password))
        db.commit()

        return "Registration successful. <a href='/login'>Login here</a>."

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)

