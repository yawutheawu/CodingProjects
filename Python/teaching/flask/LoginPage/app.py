from flask import Flask, request, render_template,abort, redirect, url_for
from markupsafe import Markup
import sqlite3 as sql
import os

def resetDir():
    fileName = __file__
    if type(fileName.split("\\")) == list and len(fileName.split("\\"))>1:
        fileName = fileName.split("\\")[-1]
        filePath = __file__.replace(fileName,"")
    else:
        fileName = fileName.split("/")[-1]
        filePath = __file__.replace(fileName,"")
    os.chdir(filePath)
    return os.path.abspath(filePath)
resetDir()


debugMode = True

'''
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall() (or .fetchone() or fetchmany(n))
for row in rows:
    print(row)
'''

app = Flask(__name__)
with sql.connect("logins.db") as connection:
    cursor = connection.cursor()
    # Try to make email bot send recovery code to user email
    cursor.execute("CREATE TABLE IF NOT EXISTS users (userID INTEGER PRIMARY KEY, username TEXT, password TEXT, firstName TEXT, lastName TEXT, email TEXT)")
    connection.commit()

@app.route("/")
@app.route("/index")
@app.route("/login")
def index():
    return render_template("login.html")

@app.route("/recovery")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/registration")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
