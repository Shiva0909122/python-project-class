from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'write /admin in the search '
    
@app.route('/admin')  # decorator for route(argument) function
def hello_admin():  # binding to hello_admin call
    return 'Hello python students welcome to class <br> clear the /admin url and write /guest/(guest name)' 


@app.route('/guest/<guest>')
def hello_guest(guest):  # binding to hello_guest call
    return 'welcome  %s as Guest of todays session' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':  # dynamic binding of URL to function
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
