'''
Clone for Cisco Security Advisories and Alerts API.
This API serves responses that are stored in the JSON file.

These Responses are captured from Official Cisco Advisory API.
https://tools.cisco.com/security/center/publicationListing.x
'''
from json import load

from flask import Blueprint, Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api_route = Blueprint('cisco_dummy_api', __name__, url_prefix='/cisco/api')
api = Api(api_route, version='1.1',
          title='[Clone] Cisco Security Advisories and Alerts API')
app.register_blueprint(api_route)
app.config['SECRET_KEY'] = 'ATMECSTech'


@api.route('/advisory')
class apiResponse(Resource):
    """Returns few Advisories fetched from Cisco API as Response"""
    def get(self):
        """Returns Date Specific Cisco API Response"""
        # with open('advisory_all.json') as json_file:
        with open('dummy_responses.json') as json_file:
            api_response = load(json_file)
        return api_response, 200


@api.route('/advisory/all')
class apiAllResponse(Resource):
    """Returns all 3037 Advisories fetched from Cisco API as Response"""
    def get(self):
        """Returns 3037 Advisories from Cisco API as Response"""
        # with open('advisory_all.json') as json_file:
        with open('all_responses.json') as json_file:
            api_response = load(json_file)
        return api_response, 200


@api.route('/advisory/nonew')
class apiNoNewResponse(Resource):
    """Returns no new advisories error from Cisco API as Response"""
    def get(self):
        """No New Advisories on particular date from Cisco API as Response"""
        return {"errorCode": "NO_DATA_FOUND",
                "errorMessage": "No data found"}, 406


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9009)
