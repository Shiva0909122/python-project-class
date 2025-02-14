from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/welcome/<name>')
def welcome(name):
    return f'Welcome {name}'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('username')
        return redirect(url_for('welcome', name=user))

if __name__ == '__main__':
    app.run(debug=True)
