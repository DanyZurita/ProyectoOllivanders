<<<<<<< HEAD
from app import app

@app.route('/')
@app.route('/index.html')

def index():
    return "Hello World!"
=======
from app import app, bootstrap
from flask import Flask, render_template
from GildedRose import logica


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', home=logica.update(0))


@app.route('/update')
def update():
    return '<h1>Bad Request</h1>', 400


@app.route('/update/<day>')
def update_day(day):
    if not day:
        abort(404)
    return render_template('update.html', day=day, update=logica.update(int(day)))
>>>>>>> a6fea659ffd9a7f9264ac3b72f0373ace29301a0
