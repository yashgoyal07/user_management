import os

mysql_user = os.environ.get("MYSQL_USER", "")
mysql_password = os.environ.get("MYSQL_PASSWORD", "")


class MysqlConfig(object):
    INSTANCE_CONFIG = {
        'local': {
            'host': 'localhost',
            'port': 3306,
            'username': mysql_user,
            'password': mysql_password
        },
        'qa': {
            'host': '##.##.##.##',
            'port': 0000,
            'username': mysql_user,
            'password': mysql_password
        },
        'prod': {
            'host': '##.##.##.##',
            'port': 0000,
            'username': mysql_user,
            'password': mysql_password
        }
    }

    DATABASE_NAME = 'usr_mgmt'
    USER_TABLE_NAME = 'user'
    ORDER_TABLE_NAME = 'order'

    TABLES_MAPPING = {
        USER_TABLE_NAME: {
            'columns': ['user_id', 'name', 'email', 'sex', 'dob', 'country_code', 'mobile',
                        'tags', 'payment_info', 'delivery_address', 'billing_address', 'latest_order_id']
        },
        ORDER_TABLE_NAME: {
            'columns': ['order_id', 'user_id', 'payment_info', 'billing_address', 'delivery_address', ]
        }
    }
