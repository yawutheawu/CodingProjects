from flask import Flask,render_template,abort, redirect, url_for
from markupsafe import Markup

app = Flask(__name__)

with app.test_request_context():
    url_for('static', filename='style.css')

@app.route("/")
@app.route("/index")
@app.route("/index/")
def index():
    #return redirect(url_for('login'))
    return "<link rel= \"stylesheet\" type= \"text/css\" href= \"static/style.css\">\n<p>Hello, World!</p>\n<a href='/hello/'>Go to Next Page</a>"
@app.route('/hello')
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/fun')
@app.route('/fun/')
@app.route('/fun/<var1>')
@app.route('/fun/<var1>/')
@app.route('/fun/<var1>/<var2>')
def fun(var1=None,var2=1):
    var3 = None
    try:
        var2 = int(var2)
    except Exception as e:
        var2 = 1
        var3 = "The second variable must be an integer. Defaulting to 1."
    return render_template('fun.html', var1=var1, var2=var2, var3=var3)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')