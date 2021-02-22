import coloredlogs
import logging
import traceback
from application import app
from flask import request
from helpers.constants import REQUEST_FAILED, REQUEST_SUCCESS
from validation.user_detail_schema import UserDetailSchema, UserGetDataSchema
from controllers.user_details_controller import UserDetailsController
from marshmallow import ValidationError

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


@app.route('/')
def home():
    return 'Welcome'


@app.route('/user', methods=['POST', 'GET'])
def user():

    # for creating or updating user data
    if request.method == 'POST':
        response = {
            "status": REQUEST_FAILED,
            "error": "Something Went Wrong. check your payload"
        }
        try:
            user_data = request.get_json()
            user_data = UserDetailSchema().load(user_data)  # data validation
            if user_data:
                user_obj = UserDetailsController()
                user_obj.create_user(user_data=user_data)
                response = {
                    "status": REQUEST_SUCCESS,
                }
        except ValidationError as err:
            logging.error(err)
            response = {
                "status": REQUEST_FAILED,
                "errors": "{err}".format(err=err)
            }
        except Exception as err:
            logging.error(f'Error coming from user due to {err}')
            logging.error(traceback.print_exc())
            response = {
                "status": REQUEST_FAILED,
                "errors": "Something Went Wrong"
            }
        finally:
            return response

    # for retrieving user data
    if request.method == 'GET':
        response = {
            "status": REQUEST_FAILED,
            "error": "Something Went Wrong. check your payload"
        }
        try:
            request_params = request.get_json()
            request_params = UserGetDataSchema().load(request_params)  # data validation
            if request_params:
                user_obj = UserDetailsController()
                result = user_obj.get_user_details(request_data=request_params)
                response = {
                    "status": REQUEST_SUCCESS,
                    "result": result
                }
        except ValidationError as err:
            logging.error(err)
            response = {
                "status": REQUEST_FAILED,
                "comment": "{err}".format(err=err)
            }
        except Exception as err:
            logging.error(f'Error coming from user due to {err}')
            logging.error(traceback.print_exc())
            response = {
                "status": REQUEST_FAILED,
                "comment": "Something Went Wrong"
            }
        finally:
            return response


if __name__ == '__main__':
    app.run(debug=True)
