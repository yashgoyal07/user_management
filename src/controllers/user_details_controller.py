import coloredlogs
import logging
from models.mysql_model import MysqlModel
from helpers.mysql_queries import *
from configs.mysql_config import MysqlConfig
from helpers.utils import filter_query_generator, load_json_strings

# colored logging
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


class UserDetailsController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    # for create and update user details
    def create_user(self, user_data):
        try:
            # list of columns in user table in sql
            user_column_list = MysqlConfig.TABLES_MAPPING[MysqlConfig.USER_TABLE_NAME]["columns"]

            # dynamic query for creating & updating user with given details
            final_column_list = []
            final_value_list = []
            update_params_str = ''

            for column in user_data:
                if column in user_column_list:
                    final_column_list.append(column)
                    final_value_list.append(user_data.get(column))
                    if column != "user_id":
                        update_params_str += " {} = '{}',".format(column, user_data.get(column))

            columns = ','.join(final_column_list)
            params = ('%s,' * len(final_column_list)).strip(',')

            query = CREATE_USER_QUERY.format(columns=columns, params=params) + update_params_str.strip(',')

            self.mysql_model_obj.dml_queries(query=query, query_params=tuple(final_value_list))
        except Exception as err:
            logging.error(f'Error coming from create_user due to {err}')
            raise

    # for retrieving user details
    def get_user_details(self, request_data):
        try:
            request_filters = request_data.get('filters', {})
            request_batch_size = request_data.get('batch_size', None)

            user_column_list = MysqlConfig.TABLES_MAPPING[MysqlConfig.USER_TABLE_NAME]["columns"]

            valid_required_props = []

            for prop in request_data.get('properties'):
                if prop in user_column_list:
                    valid_required_props.append(prop)

            if valid_required_props:
                if 'user_id' not in valid_required_props:
                    valid_required_props.append('user_id')

            if valid_required_props:
                columns = ",".join(valid_required_props)

                query = GET_USER_DATA_QUERY.format(columns=columns)

                if request_filters:
                    query = filter_query_generator(request_filters=request_filters, query=query)

                if request_batch_size:
                    query += " LIMIT " + str(request_batch_size)

                users_data = self.mysql_model_obj.dql_queries(query=query)

                return load_json_strings(users_data=users_data)
            else:
                return "give at least one valid property"
        except Exception as err:
            logging.error(f'Error coming from get_user_details due to {err}')
            raise
