from app.__init__ import app
from flask import render_template


@app.route('/')
@app.route('/index.html')

def index():
    return render_template('index.html')


app.add_url_rule('/', 'index', index)