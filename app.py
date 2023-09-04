from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = '1234'

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS Profiles (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    else:
        return render_template('home.html')

@app.errorhandler(Exception)
def handle_error(error):
    return render_template('404.html'), 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM Profiles WHERE email=? AND password=?", (email, password))
        data = c.fetchone()
        conn.close()
        if data:
            session['username'] = data[1]
            session['user_id'] = data[0]
            return redirect('/')
        else:
            err = 'Invalid credentials. Please try again.'
            return render_template('login.html', error=err)
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        pwd = request.form['pwd']
        cpwd = request.form['cpwd']
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        if pwd == cpwd:
            c.execute("SELECT * FROM Profiles WHERE email=?", (email,))
            data = c.fetchall()
            if not data:
                c.execute("INSERT INTO Profiles (name, email, password) VALUES (?, ?, ?)", (username, email, cpwd))
                conn.commit()
                session['username'] = username
                session['user_id'] = c.lastrowid
                conn.close()
                return redirect('/')
            else:
                err = 'Account already exists with this email'
                conn.close()
                return render_template('signup.html', error=err)
        else:
            err = 'Password did not match'
            conn.close()
            return render_template('signup.html', error=err)
    else:
        return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
