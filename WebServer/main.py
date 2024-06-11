from flask import Flask #import flask class

app = Flask(__name__) #create an instance

@app.route('/') #decorator
def kham_code(): #define a function
    return 'Hello there' #return statement

if __name__== '__main__':
    app.run(debug=True) #enable debug mode