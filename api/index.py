
from flask import *

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html', id=2)

@app.route('/hello/<slug>')

def helloMsg(slug):
    return "hello %s" %slug


@app.route('/error')
def err():
    return abort(404)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=3001)
