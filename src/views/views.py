import coloredlogs
import logging
from application import app
from flask import request, jsonify
from validation.user_detail_schema import UserDetailSchema
from controllers.user_details_controller import UserDetailsController
from marshmallow import ValidationError

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


@app.route('/')
def home():
    return 'Welcome'


@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        response = {
            "status": "OK",
        }
        try:
            user_data = request.get_json()
            user_data = UserDetailSchema().load(user_data)
            user_obj = UserDetailsController()
            user_obj.create_user(user_data=user_data)
        except ValidationError as err:
            logging.error(err)
            response = {
                "status": "FAILED",
                "comment": "{err}".format(err=err)
            }
        except Exception as err:
            logging.error(f'Error coming from set_user_details due to {err}')
            response = {
                "status": "FAILED",
                "comment": "Something Went Wrong!"
            }
        finally:
            return response
    return 'New Methods will be created'


@app.route('/get_user_details')
def get_user_details():
    pass


if __name__ == '__main__':
    app.run(debug=True)
