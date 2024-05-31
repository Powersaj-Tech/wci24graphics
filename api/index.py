import json

from flask import Flask
import api.Volunteers as Volunteers

app = Flask(__name__)

@app.route('/')
def hello_world():
    volunteer_list = Volunteers.returnVolunteerList()
    return json.dumps(volunteer_list)