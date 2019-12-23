from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')

def index():
    return "Hello World!"