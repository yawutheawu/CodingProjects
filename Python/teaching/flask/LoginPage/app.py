from flask import Flask, request, render_template,abort, redirect, url_for
from markupsafe import Markup
import sqlite3 as sql

debugMode = True

'''
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall() (or .fetchone() or fetchmany(n))
for row in rows:
    print(row)
'''

app = Flask(__name__)
with sql.connect("login.db") as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    connection.commit()

@app.route("/")
@app.route("/index")
@app.route("/login")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
