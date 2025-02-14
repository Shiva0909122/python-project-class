from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index7.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        
        # Creating a response and setting a cookie
        resp = make_response(render_template('result7.html', name=name))
        resp.set_cookie('username', name)
        return resp

@app.route('/getcookie')
def get_cookie():
    # Getting the cookie value
    username = request.cookies.get('username')
    return f'The username is {username}'

if __name__ == '__main__':
    app.run(debug=True)
