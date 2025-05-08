# 📸 Knox History Photo Archive Web App – Deployment Guide

This guide walks you through deploying the Flask photo archive web app under a subpath like `https://www.knoxhistory.org/gallery/`.

---

## ✅ Step 1: Prepare Flask App for Subpath `/gallery`

Modify your `app.py` to support a URL prefix by using `DispatcherMiddleware`.

### 🧠 Example Structure (`wsgi.py` or refactor `app.py`)
```python
from flask import Flask, redirect, url_for
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

app = Flask(__name__)

@app.route('/')
def redirect_home():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('home.html')

# Wrap app at "/gallery"
application = DispatcherMiddleware(
    Response('Main Knox Site'),
    {'/gallery': app}
)
```

**Do NOT call `app.run()`** at the bottom. You will use `gunicorn` instead.

---

## ✅ Step 2: Update HTML Templates with `url_for()`

In all templates (`register.html`, `login.html`, `photos.html`, `home.html`):

### 🔁 Replace hardcoded paths:

| Old | New |
|-----|-----|
| `<form action="/login">` | `<form action="{{ url_for('login') }}">` |
| `<a href="/register">` | `<a href="{{ url_for('register') }}">` |
| `<a href="/home">` | `<a href="{{ url_for('home') }}">` |
| `<form action="/photos">` | `<form action="{{ url_for('photos') }}">` |
| `<form action="/delete_photo">` | `<form action="{{ url_for('delete_photo') }}">` |

Use `url_for()` everywhere to ensure URLs respect the `/gallery` prefix.

---

## ✅ Step 3: Serve Flask App with `gunicorn`

Install gunicorn:

```bash
pip install gunicorn
```

Run your app with:

```bash
gunicorn -w 4 -b 127.0.0.1:5000 wsgi:application
```

Or if using `app.py`:

```bash
gunicorn -w 4 -b 127.0.0.1:5000 app:application
```

---

## ✅ Step 4: Configure NGINX on `knoxhistory.org`

Edit your NGINX server block config (`/etc/nginx/sites-available/knoxhistory.org` or similar):

```nginx
location /gallery/ {
    proxy_pass http://127.0.0.1:5000/gallery/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

Then restart NGINX:

```bash
sudo systemctl restart nginx
```

---

## ✅ Step 5: Access the App Publicly

After restarting everything, access your app at:

```
https://www.knoxhistory.org/gallery/home
```

You can now visit:
- `/gallery/home` to view the public photo archive
- `/gallery/login` to log in

---

## ✅ Optional: Static Asset Paths

For images, JS, CSS, use:
```html
<img src="{{ url_for('static', filename='yourfile.jpg') }}">
```

This ensures static files are loaded correctly under `/gallery/static`.

---

## 🏁 Deployment Summary

- Flask app lives at `/gallery` using `DispatcherMiddleware`
- `gunicorn` serves the app locally on port 5000
- NGINX proxies `/gallery/` traffic to Flask
- All templates use `url_for()` for routing

You’re now ready to host your app professionally as part of the Knox History website!
