from flask import Flask   
  
app = Flask(__name__)   # Flask constructor 
  
# A decorator used to tell the application 
# which URL is associated function 
@app.route('/')       
def hello(): 
    return 'HELLO python, this is day14 <br> This is a new line <br> this is another new line <br> Todays session is on Flask br'
  
if __name__=='__main__': 
   app.run(debug=True) 
