"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from functools import wraps
from datetime import datetime, timedelta

from flask import Blueprint, jsonify, request, current_app

from .models import db, TodoTask

api = Blueprint('api', __name__)


@api.route('/hello/<string:name>/')
def say_hello(name):
    response = { 'msg': "Hello {}".format(name) }
    return jsonify(response)


#@api.route('/surveys/', methods=('POST',))
#@token_required
#def create_survey(current_user):
#    data = request.get_json()
#    survey = Survey(name=data['name'])
#    questions = []
#    for q in data['questions']:
#        question = Question(text=q['question'])
#        question.choices = [Choice(text=c) for c in q['choices']]
#        questions.append(question)
#    survey.questions = questions
#    survey.creator = current_user
#    db.session.add(survey)
#    db.session.commit()
#    return jsonify(survey.to_dict()), 201


#@api.route('/surveys/', methods=('GET',))
#def fetch_surveys():
#    surveys = Survey.query.all()
#    return jsonify([s.to_dict() for s in surveys])


#@api.route('/surveys/<int:id>/', methods=('GET', 'PUT'))
#def survey(id):
#    if request.method == 'GET':
#        survey = Survey.query.get(id)
#        return jsonify(survey.to_dict())
#    elif request.method == 'PUT':
#        data = request.get_json()
#        for q in data['questions']:
#            choice = Choice.query.get(q['choice'])
#            choice.selected = choice.selected + 1
#        db.session.commit()
#        survey = Survey.query.get(data['id'])
#        return jsonify(survey.to_dict()), 201
