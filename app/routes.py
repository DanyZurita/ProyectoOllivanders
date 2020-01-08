from app import app, bootstrap
from flask import Flask, render_template
from GildedRose import main


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html', home=main.main(int(0)))


@app.route('/update')
def update():
    return '<h1>Bad Request</h1>', 400


@app.route('/update/<day>')
def update_day(day):
    if not day:
        abort(404)
    return render_template('update.html', day=day, update=main.main(int(day)))
