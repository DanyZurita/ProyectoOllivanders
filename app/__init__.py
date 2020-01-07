from flask import Flask
from flask import render_template
from GildedRose import *

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/update/<day>')
def update(day):
    return "main({})".format(day)
