from flask import Flask, request, render_template,abort, redirect, url_for, session, make_response, render_template_string
from markupsafe import Markup
import os
from dotenv import load_dotenv

# https://www.bordergate.co.uk/flask-session-cookies/
# https://medium.com/top-python-libraries/flask-sessions-and-cookies-managing-user-data-across-requests-f313a64ed85f

app = Flask(__name__)

debugMode = True

load_dotenv("secrets.env")

app.config['SECRET_KEY'] = str(os.getenv("sessionKey"))

with app.test_request_context():
    url_for('static', filename='style.css')

@app.route('/', methods = ['GET'])
def setUserSession():
    if not 'username' in session:
         session['username'] = str(request.remote_addr)
         print(session['username'])
 
    return render_template("homepage.html", user=session["username"])

@app.route("/homepage", methods =["GET", "POST"])
def homepage(user = None):
    if request.method == "POST":
        session["username"] = str(request.remote_addr)
        resp = make_response(redirect(url_for('dashboard')))
        resp.set_cookie('favorite_color', "White")
        return resp
    try:
        user = session["username"]
    except:
        user=None
    if user == None:
         return render_template("homepage.html", success=False)
    else:
        return render_template("dashboard.html",username = user, favoriteColor = request.cookies.get('favorite_color'))

@app.route("/dashboard", methods =["GET", "POST"])
def dashboard(user = None):
    try:
        user = session["username"]
    except:
        user=None
    return render_template("dashboard.html",username = user, favoriteColor = request.cookies.get('favorite_color'))

if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
    
