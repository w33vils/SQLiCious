from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a table for users
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
''')

# Insert a sample user for demonstration purposes
c.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpassword')")

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    # Simulate SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    user = c.fetchone()

    if user:
        return 'Aw3some: Simple, Right? Flag: AP{SQL1nj3ct10nSucc3ss}'
    else:
         return render_template('lol.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
