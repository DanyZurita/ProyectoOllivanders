from app import app
from flask import Flask, render_template
from GildedRose import *

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/update')
def update():
    return '<h1>Bad Request</h1>', 400

@app.route('/update/<day>')
def update_day(day):
    if not day:
        abort(404)
    return render_template('update.html', days=day, main=main)