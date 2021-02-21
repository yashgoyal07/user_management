import coloredlogs
import logging
import json
from models.mysql_model import MysqlModel
from helpers.mysql_queries import CREATE_USER_QUERY, GET_USER_DETAILS
from configs.mysql_config import MysqlConfig
from datetime import datetime

logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


class UserDetailsController(object):
    def __init__(self):
        self.mysql_model_obj = MysqlModel()

    def create_user(self, user_data=None):
        try:
            if not user_data:
                user_data = {}

            user_column_list = MysqlConfig.TABLES_MAPPING[MysqlConfig.USER_TABLE_NAME]["columns"]
            final_column_list = []
            final_value_list = []
            update_params_str = ''
            for column in user_column_list:
                if column in user_data:
                    final_column_list.append(column)
                    final_value_list.append(user_data.get(column))
                    if column != "user_id":
                        update_params_str += " {} = '{}',".format(column, user_data.get(column))

            columns = ','.join(final_column_list)
            params = ('%s,' * len(final_column_list)).strip(',')
            query = CREATE_USER_QUERY.format(columns=columns, params=params)
            query += update_params_str.strip(',')
            logging.info(f"query = {query}")
            self.mysql_model_obj.dml_queries(query=query, query_params=tuple(final_value_list))
        except Exception as err:
            logging.error(f'Error coming from create_user due to {err}')
            raise

    def get_user_details(self, request_data=None):
        try:
            print(request_data)
            if not request_data:
                request_data = {}

            user_column_list = MysqlConfig.TABLES_MAPPING[MysqlConfig.USER_TABLE_NAME]["columns"]

            final_column_list = []
            for column in user_column_list:
                if column in request_data.get('columns'):
                    final_column_list.append(column)

            columns = ','.join(final_column_list)
            query = GET_USER_DETAILS.format(columns=columns)
            logging.info(f"query = {query}")
            result = self.mysql_model_obj.dql_queries(query=query, query_params=(request_data.get('user_id'),))
            print(result)
            if len(result) > 0:
                result = result[0]
                for key, value in result.items():
                    try:
                        if isinstance(value, datetime):
                            result[key] = datetime.strftime(value, '%Y-%m-%d')
                        else:
                            result[key] = json.loads(value)
                    except Exception:
                        pass
            return result
        except Exception as err:
            logging.error(f'Error coming from get_user_details due to {err}')
            raise
