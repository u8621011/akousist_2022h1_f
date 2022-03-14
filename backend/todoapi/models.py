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
    desc = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        return dict(id=self.id,
                    title=self.title,
                    desc=self.desc)
