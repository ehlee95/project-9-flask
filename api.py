from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import *

app = Flask(__name__)


@app.route('/')
def index():
    return "General Assembly Students API, please go to /student or /cohort to view data"


@app.route('/student/', methods=['GET', 'POST'])
@app.route('/student/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Student.get(Student.id == id)))
        else:
            studentList = []
            for student in Student.select():
                studentList.append(model_to_dict(student))
            return jsonify(studentList)

    if request.method == 'POST':
        # dict_to_model takes the model as first arg, and the request JSON body as the second
        new_student = dict_to_model(Student, request.get_json())
        new_student.save()
        return jsonify({"success": True})

    if request.method == 'DELETE':
        record = Student.get(Student.id == id)
        record.delete_instance()
        return 'Deleted'

    if request.method == 'PUT':
        Student.update(request.get_json()).where(Student.id == id).execute()
        return 'Updated'


app.run(debug=True, port=3001)
