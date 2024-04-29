from app import app
from datamodels import db

with app.app_context():
    db.create_all()
