from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ProductivityManager.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ProductivityManager(db.Model):
    sno = db.Column(db.Integer , primary_key = True)
    Growth = db.Column(db.Integer , nullable=False)
    Duty = db.Column(db.Integer , nullable=False)
    Pleasure = db.Column(db.Integer , nullable=False)
    Date = db.Column(db.DateTime , default = datetime.utcnow )

    def __repr__(self) -> str:
        return f"{self.sno} - {self.Title}"

@app.route("/")
def Index():

    return render_template('index.html')

@app.route("/Graphs")
def Graphs():
    return render_template('index.html')

@app.route("/Records")
def Records():
    return render_template('index.html')

@app.route("/About")
def About():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True) 