from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# import sqlite3
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///harry.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
app.app_context().push()
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200), nullable=False)
    server_type = db.Column(db.String(100), nullable=False)
    port_number = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) ->str:
        return f"{self.sno} - {self.project_name}"
@app.route('/')
def index():
    return render_template("index.html")
    # return 'Welcome to index'
@app.route('/products')
def products():
    return 'Welcome to products'
@app.route('/contact')
def contact():
    return 'Welcome to contact page'


if __name__ == "__main__":
    app.run(debug=True, port=8000)