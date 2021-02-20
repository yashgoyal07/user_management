import coloredlogs
import logging
import json
from application import app
from pprint import pprint as pp
from flask import request
from validation.user_detail_schema import UserDetailSchema
from controllers.user_details_controller import UserDetailsController
from marshmallow import ValidationError

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


@app.route('/')
def home():
    return 'Welcome'


@app.route('/set_user_details', methods=['POST', 'GET'])
def set_user_details():
    if request.method == 'POST':
        try:
            user_data = request.get_json()
            user_data = UserDetailSchema().load(user_data)
            user_obj = UserDetailsController()
            user_obj.create_user(user_data=user_data)
            return 'OK'
        except ValidationError as err:
            logging.error(err)
            return "ValidationError"
        except Exception as err:
            logging.error(f'Error coming from set_user_details due to {err}')
            return "ExceptionError"
    return 'Please use POST method to send sensitive information.'


@app.route('/get_user_details')
def get_user_details():
    pass


if __name__ == '__main__':
    app.run(debug=True)
