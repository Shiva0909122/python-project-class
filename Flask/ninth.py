from flask import Flask, render_template, request, redirect, url_for, abort

app = Flask(__name__)

# In-memory storage for simplicity
users = {}

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to the Home Page</h1><p><a href='/signup'>Sign Up</a> | <a href='/login'>Login</a></p>"

# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Basic validation
        if not username or not password:
            return "<h3>Username and password are required.</h3><a href='/signup'>Try Again</a>"

        # Check if the user already exists
        if username in users:
            return "<h3>Username already exists. Choose another one.</h3><a href='/signup'>Try Again</a>"

        # Save user details
        users[username] = password
        return redirect(url_for('login'))
    
    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the user exists and password matches
        if username in users and users[username] == password:
            return f"<h1>Welcome, {username}!</h1><p>Login successful.</p>"
        else:
            # If the credentials are incorrect, abort with a 403 Forbidden error
            abort(403)

    return render_template('login.html')

# Custom 403 Error Page
@app.errorhandler(403)
def forbidden(e):
    return "<h1>403 Forbidden</h1><p>Invalid username or password.</p><a href='/login'>Try Again</a>", 403

# Custom 404 Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
