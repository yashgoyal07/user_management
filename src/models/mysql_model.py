import logging, coloredlogs
import mysql.connector
from helpers.utils import get_environment
from configs.mysql_config import MysqlConfig

logger = logging.getLogger(__name__)

coloredlogs.install(level='DEBUG')


class MysqlModel(object):
    def __init__(self):
        self.infra_env = get_environment()
        self.instance_config = MysqlConfig().INSTANCE_CONFIG.get(self.infra_env, {})

    def get_connection(self):
        connection = mysql.connector.connect(host=self.instance_config.get('host'),
                                             port=self.instance_config.get('port'),
                                             username=self.instance_config.get('username'),
                                             password=self.instance_config.get('password'))
        return connection

    # for data-modification language commands
    def dml_queries(self, query, query_params):
        conn = None
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, query_params)
            conn.commit()
            result = cur.rowcount
            return result
        except Exception as err:
            logging.error(f'Error from dml_queries due to {err}')
            raise
        finally:
            if conn:
                conn.close()

    # for data-query language commands
    def dql_queries(self, query, query_params):
        conn = None
        try:
            conn = self.get_connection()
            cur = conn.cursor(dictionary=True)
            cur.execute(query, query_params)
            result = cur.fetchall()
            return result or []
        except Exception as err:
            logging.error(f'Error from dql_queries due to {err}')
            raise
        finally:
            if conn:
                conn.close()
