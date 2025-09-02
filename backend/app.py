import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance/peakform.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import auth  # make sure routes/__init__.py exists

app.register_blueprint(auth.auth_bp)

@app.route('/')
def home():
    return {"message": "PeakForm backend running"}

if __name__ == '__main__':
    app.run(debug=True)
