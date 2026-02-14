from flask import Flask,render_template,abort, redirect, url_for
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index/")
def index():
    #return redirect(url_for('login'))
    return "<p>Hello, World!</p>\n<a href='/hello/'>Go to Next Page</a>"

@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)