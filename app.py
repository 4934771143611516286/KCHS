from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a strong secret key!

# Setup database connection
db = mysql.connector.connect(
    host="localhost",
    user="your_db_username",   # change to your database username
    password="your_db_password",   # change to your database password
    database="your_db_name"    # change to your database name
)
cursor = db.cursor(dictionary=True)

# Home page
@app.route('/')
def home():
    return redirect(url_for('login'))

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        if existing_user:
            flash('Username already exists. Please choose another.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
        db.commit()

        flash('Registration successful! Redirecting to login...', 'success')
        session['redirect_url'] = url_for('login')
        return redirect(url_for('register'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            flash('Logged in successfully! Redirecting to gallery...', 'success')
            session['redirect_url'] = url_for('photos')
            return redirect(url_for('login'))
        else:
            flash('Invalid username or password.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out. Redirecting to login...', 'info')
    session['redirect_url'] = url_for('login')
    return redirect(url_for('login'))

# Photos gallery and upload
@app.route('/photos', methods=['GET', 'POST'])
def photos():
    if 'user_id' not in session:
        flash('Please log in to add photos.', 'warning')
        session['redirect_url'] = url_for('photos')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        date_taken = request.form['dateTaken']
        link = request.form['link']
        description = request.form['descript']

        cursor.execute("INSERT INTO images (Title, dateTaken, Link, Descript) VALUES (%s, %s, %s, %s)",
                       (title, date_taken, link, description))
        db.commit()
        flash('Photo added successfully!', 'success')

    cursor.execute("SELECT * FROM images")
    photos = cursor.fetchall()
    return render_template('photos.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)
