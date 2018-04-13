from flask import Flask
from app.api.user import bp as user_api
from app.api.redirection import bp as redirect_api

app = Flask(__name__)
app.register_blueprint(user_api)
app.register_blueprint(redirect_api)


@app.route('/')
def sample_route():
    return '<h1>OK</h1>'
