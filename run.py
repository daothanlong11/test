from flask import Flask 

my_app = Flask(__name__)

@my_app.route('/')
def hello():
    return 'hello the fucking world'

#### met vl############