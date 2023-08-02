from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# import datetime
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

#
if __name__ == "__main__":
    app.run(debug=True)

