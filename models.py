from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()


app = Flask(__name__, template_folder="template")

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/clinic'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hard to guess'
db = SQLAlchemy(app)


class Patients(db.Model):
    __tablename__ = 'patient'
    id = db.Column(db.Integer, primary_key=True)
    pressure_sist = db.Column(db.Integer)
    pressure_dia = db.Column(db.Integer)
    breath = db.Column(db.Integer)
    pulse = db.Column(db.Integer)
    iss = db.Column(db.Integer)
    glasgo = db.Column(db.Integer)


    def __repr__(self):
        return '<Patients {}>'.format(self.id)







