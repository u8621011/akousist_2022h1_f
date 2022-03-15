"""
application.py
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from flask_cors import CORS
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

def create_app(app_name='TODO_API'):
  app = Flask(app_name,
              static_url_path='/upload',
              static_folder = 'upload')
  app.config.from_object('todoapi.config.BaseConfig')

  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  from todoapi.api import api

  CORS(api)

  app.register_blueprint(api, url_prefix="/api")

  from todoapi.models import db
  db.init_app(app)

  return app
