import coloredlogs
import logging
from models.mysql_model import MysqlModel
from helpers.mysql_queries import CREATE_USER_QUERY
from configs.mysql_config import MysqlConfig

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
                        update_params_str += " {} = '{}',".format(column,user_data.get(column))

            columns = ','.join(final_column_list)
            params = ('%s,' * len(final_column_list)).strip(',')
            query = CREATE_USER_QUERY.format(columns=columns, params=params)
            query += update_params_str.strip(',')
            logging.info(f"query=={query}")
            self.mysql_model_obj.dml_queries(query=query, query_params=tuple(final_value_list))
        except Exception as err:
            logging.error(f'Error coming from set_details due to {err}')
            raise
