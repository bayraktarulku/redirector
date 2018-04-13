from flask import Flask

app = Flask(__name__)


@app.route('/')
def sample_route():
    return '<h1>OK</h1>'
