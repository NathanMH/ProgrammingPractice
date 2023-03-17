import os
from flask import Flask
import sqlite3

app = Flask(__name__)

ROOT = os.path.dirname(__file__)
DATABASE = os.path.join(ROOT, 'testdb.sqlite')

@app.route('/getstarted')
def create_db():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS test_table 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date INTEGER,
        sleep INTEGER,
        alcohol INTEGER
    )
    ''')
    con.commit()
    con.close()
    return f'DB created successfully'

@app.route('/')
def hello():
    return "<p>Sup World!!</p>"

@app.route('/user/<username>')
def show_user_profile():
    return f'User [escape(usersname)]'

@app.route('/user/showdb')
def show_user_db():
    con = sqlite3.connect(DATABASE)
    cur = con.cursor()
    # for row in cur.execute('SELECT * FROM test_table'):
        # print(row)
    return str(cur.execute('SELECT * FROM test_table'))
    

if __name__ == '__main__':
    print(ROOT)
    print(DATABASE)
    
    app.run(debug = True)
