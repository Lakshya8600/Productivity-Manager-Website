import re
from flask import Flask, render_template , request
from datetime import date, datetime
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ProductivityManager.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ProductivityManagerClass(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    Growth = db.Column(db.Integer , nullable=False)
    Duty = db.Column(db.Integer , nullable=False)
    Pleasure = db.Column(db.Integer , nullable=False)
    Date = db.Column(db.String(50) , nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Title}"

@app.route("/") 
def Index():
    TodayDate = datetime.utcnow
    return render_template('index.html')

@app.route("/Graphs")
def Graphs():
    return render_template('index.html')

@app.route("/Records" , methods=['GET','POST'])
def Records():
    if request.method == 'POST':
        if request.form['Growth'] == "" or request.form['Duty'] == "" or request.form['Pleasure'] == "" or str(request.form['Date']) == "":
            print("Not found")
            return render_template('EnterParameter.html')
        user = ProductivityManagerClass(Growth=request.form['Growth'],Duty=request.form['Duty'],Pleasure=request.form['Pleasure'],Date=str(request.form['Date']))
        db.session.add(user)
        db.session.commit()
    allUser = ProductivityManagerClass.query.all()
    return render_template('Records.html',AllUser=allUser)

@app.route("/About")
def About():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 