#!flask/bin/python
from flask import Flask, jsonify, request

import json
app = Flask(__name__)

emp={}
helper = []
class Employee:
	def __init__(self, name, company, age):
		self.name = name
		self.company = company
		self.age = age
	def myfunc(self):
            res = {}
            res['name'] = self.name
            res['company'] = self.company
            res['age'] = self.age

            return res


@app.route('/')
def get_Details():
    E1=Employee('Dheeraj','EOG',25)
    doer = E1.myfunc()
    emp = doer
    if not helper:
        helper.append(emp)
        
    return jsonify({'EMP_Details for':helper})

@app.route('/emp/check', methods=['POST'])
def put_Details():
    emp['name']=request.json['name']
    emp['company'] = request.json['company']
    emp['age'] = request.json['age']
    helper.append(emp)
    return jsonify({'EMP_Details':helper})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
