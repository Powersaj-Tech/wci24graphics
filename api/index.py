from flask import Flask
import Volunteers

app = Flask(__name__)


@app.route('/')
def hello_world():
    return Volunteers.returnVolunteerList()
