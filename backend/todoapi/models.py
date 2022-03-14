"""
models.py
- Data classes for the surveyapi application
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TodoTask(db.Model):
    __tablename__ = 'todo_task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    origin_filename = db.Column(db.String(256), nullable=True)
    filename = db.Column(db.String(256), nullable=True)
    desc = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    origin_filename=self.origin_filename,
                    filename=self.filename,
                    desc=self.desc)
