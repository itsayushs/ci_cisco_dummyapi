import json
from flask import Flask, Blueprint
from flask_restplus import Api, Resource

app = Flask(__name__)
blue = Blueprint('api', __name__, url_prefix='/cisco/api')
api = Api(blue)
app.register_blueprint(blue)
app.config.from_pyfile('config.py')

with open('advisory.json') as json_file:
    response = json.load(json_file)


@api.route('/advisory')
class FromIosVersion(Resource):
    """Sends the response to the /advisory"""
    def get(self):
        """Accepting get & returning resonse form json & 200 code"""
        return response, 200


if __name__ == "__main__":
    app.run(port=9009)
