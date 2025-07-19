from flask import Flask, render_template, request, redirect, url_for, jsonify
import jwt
import datetime

app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey123'


VALID_EMAIL = "admin@example.com"
VALID_PASSWORD = "admin123"

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == VALID_EMAIL and password == VALID_PASSWORD:

            token = jwt.encode(
                {
                    'user': email,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
                },
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )

            print(" JWT Token:", token)

            # You can also return token in response or store in session
            return f"<h3>✅ Login Successful</h3><p> JWT Token: {token}</p><a href='/home'>Go to Home</a>"
        else:
            return "<h3>❌ Invalid Email or Password</h3><a href='/login'>Try Again</a>"

    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)