from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

contacts = {}

@app.route('/')
def home():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    contacts[name] = {'Phone': phone, 'Email': email}
    return redirect(url_for('home'))

@app.route('/search', methods=['POST'])
def search_contact():
    name = request.form['name']
    contact = contacts.get(name, None)
    # If contact is found, pass the contact details
    return render_template('index.html', contacts=contacts, search_result=contact)

if __name__ == '__main__':
    app.run(debug=True)
