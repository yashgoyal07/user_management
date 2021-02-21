import coloredlogs
import logging
import json
from models.mysql_model import MysqlModel
from helpers.mysql_queries import *
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
            if not request_data:
                request_data = {}

            request_user_ids = (request_data.get('filters', {})).get('user_ids', [])

            request_dob_start_date = ((request_data.get('filters', {})).get('dob', {})).get('start_date', "")

            request_dob_end_date = ((request_data.get('filters', {})).get('dob', {})).get('end_date', "")

            user_column_list = MysqlConfig.TABLES_MAPPING[MysqlConfig.USER_TABLE_NAME]["columns"]

            valid_required_props = []
            for prop in request_data.get('properties'):
                if prop in user_column_list:
                    valid_required_props.append(prop)

            if 'user_id' not in valid_required_props:
                valid_required_props.append('user_id')

            columns = ",".join(valid_required_props)

            query = GET_USER_DATA_QUERY.format(columns=columns)

            where_clause = []

            if request_user_ids:
                users_params = "'" + "','".join((request_data.get('filters')).get('user_ids')) + "'"
                where_clause.append(" user_id IN ({})".format(users_params))

            if request_dob_start_date and request_dob_end_date:
                where_clause.append("dob BETWEEN '{}' AND '{}'".format(request_dob_start_date, request_dob_end_date))

            if len(where_clause) > 0:
                query += " WHERE "
                query += " AND ".join(where_clause)

            users_data = MysqlModel().dql_queries(query=query)
            print(query)
            for user in users_data:
                for key, value in user.items():
                    try:
                        if isinstance(value, datetime):
                            user[key] = datetime.strftime(value, '%Y-%m-%d')
                        else:
                            user[key] = json.loads(value)
                    except Exception:
                        pass

            return users_data
        except Exception as err:
            logging.error(f'Error coming from get_user_details due to {err}')
            raise
