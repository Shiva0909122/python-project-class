from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index8.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Getting form data
        name = request.form['name']
        age = request.form['age']
        color = request.form['color']

        # Creating a response and setting multiple cookies
        resp = make_response(render_template('result8.html', name=name, age=age, color=color))
        resp.set_cookie('username', name)
        resp.set_cookie('age', age)
        resp.set_cookie('color', color)
        return resp

@app.route('/getcookies')
def get_cookies():
    # Getting the values of all cookies
    name = request.cookies.get('username')
    age = request.cookies.get('age')
    color = request.cookies.get('color')
    return f'Username: {name}, Age: {age}, Favorite Color: {color}'
@app.route('/deletecookies')
def delete_cookies():
    resp = make_response("All cookies deleted")
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('age', '', expires=0)
    resp.set_cookie('color', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
