from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# For creating the models pytho3 models.py
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)
db = SQLAlchemy()

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

if __name__ == "__main__":
    db.create_all()
