from flask import Flask, request, render_template,abort, redirect, url_for, session, make_response, render_template_string
from markupsafe import Markup
import os
from dotenv import load_dotenv

# https://www.bordergate.co.uk/flask-session-cookies/
# https://medium.com/top-python-libraries/flask-sessions-and-cookies-managing-user-data-across-requests-f313a64ed85f

app = Flask(__name__)

debugMode = True

load_dotenv("secrests.env")

app.secret_key = os.getenv("sessionKey")
app.config['SECRET_KEY'] = os.getenv("sessionKey")

with app.test_request_context():
    url_for('static', filename='style.css')

@app.route("/homepage", methods =["GET", "POST"])
def dashboard(user = None):
    if user == None:
         return render_template("homepage.html", success=False)
    else:
        return render_template("dashboard.html",username = user)

if __name__ == "__main__":
    app.run(debug=debugMode,host='0.0.0.0')
