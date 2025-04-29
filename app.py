from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
import os
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a real secret key

# Setup database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_db_password",  # Replace with your actual MySQL password
    database="your_db_name"
)
cursor = db.cursor(dictionary=True)

# File upload config
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    if session.get('user_id'):
        flash('You are already logged in.', 'info')
        return redirect(url_for('photos'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        flash('You are already registered and logged in.', 'info')
        return redirect(url_for('photos'))

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

        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        flash('You are already logged in.', 'info')
        return redirect(url_for('photos'))

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

    session.pop('redirect_url', None)
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out. Redirecting to login...', 'info')
    return redirect(url_for('login'))

@app.route('/photos', methods=['GET', 'POST'])
def photos():
    if not session.get('user_id'):
        flash('You must log in to access the photo gallery.', 'warning')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        date_taken = request.form['dateTaken']
        description = request.form['descript']
        file = request.files.get('photo_file')
        link = request.form.get('link')

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            link = f"/static/uploads/{filename}"

        if not link:
            flash('Please provide an image link or upload a file.', 'danger')
            return redirect(url_for('photos'))

        cursor.execute(
            "INSERT INTO images (Title, dateTaken, Link, Descript) VALUES (%s, %s, %s, %s)",
            (title, date_taken, link, description)
        )
        db.commit()
        flash('Photo added successfully!', 'success')

    cursor.execute("SELECT * FROM images")
    photos = cursor.fetchall()
    return render_template('photos.html', photos=photos, username=session.get('username'))

@app.route('/delete_photo', methods=['POST'])
def delete_photo():
    if not session.get('user_id'):
        flash('You must be logged in to delete photos.', 'warning')
        return redirect(url_for('login'))

    photo_id = request.form['photo_id']
    cursor.execute("DELETE FROM images WHERE id = %s", (photo_id,))
    db.commit()

    flash('Photo deleted successfully!', 'success')
    return redirect(url_for('photos'))

if __name__ == '__main__':
    app.run(debug=True)
