from flask import Flask 
app = Flask(__name__) 
#html is hyper text markup langauage <html,body, img, div, span>
# routing the decorator function hello_name 
@app.route('/<name>') 
def hello_name(name): 
    return 'Hello %s!' % name 

if __name__ == '__main__': 
    app.run(debug = True) 
