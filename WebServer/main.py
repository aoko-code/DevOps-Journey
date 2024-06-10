from flask import Flask

app = Flask(__name__)

@app.route('/')
def kham_code():
    return 'Hello there'

if __name__== '__main__':
    app.run(debug=True)