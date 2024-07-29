from io import BytesIO
from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Upload(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	filename = db.Column(db.String(50))
	data = db.Column(db.LargeBinary)


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

@app.route('/upload', methods = ['POST','GET'])
def upload():
    if request.method == 'POST':
        file = request.files['image']
        upload = Upload(filename=file.filename, data=file.read())
        db.session.add(upload)
        db.session.commit()
        return f'Uploaded: {file.filename}'
    
    return render_template('upload.html')


@app.route('/download/<upload_id>')
def download(upload_id):
	upload = Upload.query.filter_by(id=upload_id).first()
	return send_file(BytesIO(upload.data), download_name=upload.filename, as_attachment=True )

@app.route('/flash')
def flashit():
        flash("You are successfully login into the Flask Application")
        return redirect('/home')
if __name__ == "__main__":
    app.run(debug=True, port=3001)