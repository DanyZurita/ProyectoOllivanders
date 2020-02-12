from flask import Flask
<<<<<<< HEAD

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')

def index():
    return "Hello World!"
=======
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)
>>>>>>> a6fea659ffd9a7f9264ac3b72f0373ace29301a0
