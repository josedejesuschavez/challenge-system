from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world96986"

def create_app():
    #app = Flask(__name__)
    return app