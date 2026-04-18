from flask import Flask, request, render_template,abort, redirect, url_for
from markupsafe import Markup
import sqlite3 as sql
import pandas as pd
import os
import emailHandler as emailFella

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

recoveryList = {}

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
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        with sql.connect("logins.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            print("SELECT * FROM users WHERE username = {} AND password = {}".format(username, password))
            user = cursor.fetchone()
            print(user)
            if user:
                error_message = "Login successful! Welcome, {} {}.".format(user[3], user[4])
                return render_template("dashboard.html", username=user[3])
            else:
                error_message = "Invalid username or password. Please try again."
                return render_template("login.html", error=error_message, success=False, username=username)
    return render_template("login.html", success=True)

@app.route("/forgot-password/", methods =["GET", "POST"])
@app.route("/recovery/", methods =["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        if email != None:
            email = email.lower()
        with sql.connect("logins.db") as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()
            if user:
                #sending recovery email
                recoveryList[email] = emailFella.sendPasswordResetEmail(email)
                print("Sending to CheckEmail")
                return render_template("checkEmail.html", email=email, reset_code=recoveryList[email])
            else:
                error_message = "Email not found. Please try again."
                return render_template("forgot_password.html", success=False, error=error_message, failEmail=email)
    return render_template("forgot_password.html", success=False, error=None, failEmail=None)

@app.route("/recoveryCode", methods =["GET", "POST"])
def checkEmail(email = None, reset_code = None):
    if request.method == "POST":
        email = request.form.get("email")
        reset_code = request.form.get("reset_code")
        try:
            reset_code = int(reset_code)
        except:
            pass
        print(email)
        print(reset_code)
        if email in recoveryList and recoveryList[email] == reset_code:
            return render_template("resetPassword.html", email=email, reset_code=reset_code)
        else:
            error_message = "Invalid reset code. Please try again."
            return render_template("checkEmail.html",email=email, success=False, error=error_message)
    print(email)
    return render_template("checkEmail.html", email=email, success=None, error=None)

@app.route("/recoveryReset", methods =["GET", "POST"])
def resetPassword(email = None, reset_code = None):
    print(email)
    print(reset_code)
    print(recoveryList)
    try:
        email = request.form.get("email")
        reset_code = int(request.form.get("reset_code"))
    except:
        pass
    print(email)
    print(reset_code)
    if request.method == "POST":
        email = request.form.get("email")
        reset_code = int(request.form.get("reset_code"))
        new_password = request.form.get("password")
        if email in recoveryList and recoveryList[email] == reset_code:
            with sql.connect("logins.db") as connection:
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
                user = cursor.fetchone()
            del recoveryList[email]
            return render_template("resetPassword.html", success=True, email=email)
        else:
            error_message = "Invalid password. Please try again."
            return render_template("resetPassword.html", success=False, error=error_message, email=email)
    return render_template("resetPassword.html", email=email, success=None, error=None)

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

@app.route("/dashboard", methods =["GET", "POST"])
def dashboard(user = None):
    if user == None:
         return render_template("login.html", success=False)
    else:
        return render_template("dashboard.html",username = user)

if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
