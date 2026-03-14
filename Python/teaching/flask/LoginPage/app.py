from flask import Flask, request, render_template,abort, redirect, url_for
from markupsafe import Markup
import sqlite3 as sql
import pandas as pd
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
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
                   users (userID INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, firstName TEXT, lastName TEXT, email TEXT UNIQUE)""")
    
    
    
    cursor.execute("""INSERT INTO users (username, password, firstName, lastName, email) 
                   VALUES ('ADMIN', 'SECUREADMINPASSWORD1234!@#$', 'ADMIN', 'ADMIN', 'admin@admin.com') 
                   ON CONFLICT(username) DO NOTHING""")
    
    print(pd.read_sql_query("SELECT * FROM users", connection))
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    del rows
    connection.commit()

@app.route("/")
@app.route("/index")
@app.route("/login/", methods =["GET", "POST"])
def index():
    return render_template("login.html")

@app.route("/recovery")
def forgot_password():
    return render_template("forgot_password.html")

@app.route("/registration/", methods =["GET", "POST"])
def register():
    iferror = None
    success = None
    if request.method == "POST":
        fname = str(request.form.get("firstName")).lower().capitalize()
        lname = request.form.get("lastName").lower().capitalize()
        email = request.form.get("email").lower()
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"({username},{password}, {fname}, {lname}, {email})")
        with sql.connect("logins.db") as connection:
            cursor = connection.cursor()
            try:
                cursor.execute("""INSERT INTO users (username, password, firstName, lastName, email) 
                               VALUES (?, ?, ?, ?, ?)""", (username, password, fname, lname, email))
                connection.commit()
                success = True
            except sql.IntegrityError as e:
                success = False
                if "UNIQUE constraint failed: users.username" in str(e):
                    iferror = "Username already exists"
                elif "UNIQUE constraint failed: users.email" in str(e):
                    iferror = "Email already exists"
                else:
                    iferror = "Database error: {}".format(str(e))
        if debugMode:
            print(pd.read_sql_query("SELECT * FROM users", connection))
        if success:
            return render_template("register.html", error = iferror, success = success, failName = None, failLast = None, failEmail = None)
        else:    
            return render_template("register.html", error = iferror, success = success, failName = fname, failLast = lname, failEmail = email)
    return render_template("register.html", error = iferror, success = success, failName = None, failLast = None, failEmail = None)

if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
