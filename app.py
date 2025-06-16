from flask import Flask
import sqlite3


app =Flask(__name__)
app.secret_key = 'manmade_secret_key430'

@app.route('/')
def index():
    return "<h1>Groceries List</h1>"


if __name__ == '__main__':
    app.run()
