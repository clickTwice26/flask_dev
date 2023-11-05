from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# import sqlite3
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///harry.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)
app.app_context().push()
# app.app_context().push()
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(200), nullable=False)
    server_type = db.Column(db.String(100), nullable=False)
    port_number = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) ->str:
        return f"{self.sno} - {self.project_name}"
@app.route('/',methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = request.form
        print(form_data)     
        project_name = form_data['project_name']
        server_type = form_data['server_type']
        port_number = form_data['port_number']
        # if 
        todo = Todo(project_name=project_name,server_type=server_type,port_number=port_number)
        db.session.add(todo)
        db.session.commit()
        
        # return render_template("index.html",allTodo=allTodo)
    allTodo = Todo.query.all()
    # return 'Welcome to index'
    return render_template("index.html", allTodo=allTodo)
@app.route('/products')
def products():
    return 'Welcome to products'
@app.route('/contact')
def contact():
    return 'Welcome to contact page'
@app.route('/start/<int:sno>')
def server_start(sno):
    log_string = f"{sno} server triggered for starting"
    with open("server_log.txt", "a") as server_loger:
        server_loger.write(log_string+"\n")
        server_loger.close()
    # return 'Welcome to contact page'
@app.route('/stop/<int:sno>')
def server_stop(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    # allrequest = Todo.query.all()
    # print(allrequest)
    # print(type(allrequest))
    return redirect("/")
@app.route('/panel/<int:sno>')
def server_panel():
    # allrequest = Todo.query.all()
    # print(allrequest)
    # print(type(allrequest))
    return 'Welcome to contact page'



if __name__ == "__main__":
    app.run(debug=True, port=8000)