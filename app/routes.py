from app import app

@app.route('/')
@app.route('/index.html')

def index():
    return "Hello World!"