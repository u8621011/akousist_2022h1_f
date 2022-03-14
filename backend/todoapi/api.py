"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app, abort

from .models import db, TodoTask


api = Blueprint('api', __name__)


@api.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)


@api.route('/tasks', methods=('POST',))
def create_survey():
    data = request.get_json()

    if data is not None and "title" in data:
        new_task = TodoTask(title=data['title'])

        db.session.add(new_task )
        db.session.commit()
        return jsonify({
            "success": True,
            "data": new_task.to_dict()
            }), 201
    else:
        abort(404, description="Title not specified")


@api.route('/tasks', methods=('GET',))
def fetch_tasks():
    tasks = TodoTask.query.all()
    return jsonify({
        "success": True,
        "data": [t.to_dict() for t in tasks]
        })


@api.route('/tasks/<int:id>', methods=('GET', 'PUT', 'DELETE'))
def task(id):
    if request.method == 'GET':
        task = TodoTask.query.get(id)
        return jsonify({
            "success": True,
            "data": task.to_dict()
            }), 201
    elif request.method == 'PUT':   # update code here
        data = request.get_json()
        
        task = TodoTask.query.get(id)

        task_desc = data['desc']
        task.desc = task_desc

        db.session.commit()
        
        return jsonify({
            "success": True,
            "data": task.to_dict()
            }), 201
    elif request.method == 'DELETE':
        TodoTask.query.filter(TodoTask.id == id).delete()

        db.session.commit()
        
        return jsonify({
            "success": True,
            }), 201
