from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasker.db'

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()
    # db.session.add(Task(title='First Task', date='2021-01-01'))
    # db.session.add(Task(title='Second Task', date='2021-01-02'))
    # db.session.commit()

from routes import *

if __name__ == '__main__':
    app.run(debug=True)