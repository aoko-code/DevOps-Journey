from flask import Flask, render_template #import flask class

app = Flask(__name__) #create an instance

@app.route('/') #decorator
def kham_code(): #define a function
    return 'Hello there' #return statement

#add another route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

if __name__== '__main__':
    app.run(debug=True) #enable debug mode