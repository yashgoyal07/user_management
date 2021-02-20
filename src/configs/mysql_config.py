class MysqlConfig(object):
    INSTANCE_CONFIG = {
        'local': {
            'host': 'localhost',
            'port': 3306,
            'username': 'root',
            'password': 'YasMys@1'
        },
        'qa': {
            'host': '##.##.##.##',
            'port': 0000,
            'username': '####',
            'password': '########'
        },
        'prod': {
            'host': '##.##.##.##',
            'port': 0000,
            'username': '####',
            'password': '########'
        }
    }

    DATABASE_NAME = 'usr_mgmt'
    USER_TABLE_NAME = 'user'
    ORDER_TABLE_NAME = 'order'

    TABLES_MAPPING = {
        USER_TABLE_NAME: {
            'columns': ['user_id', 'name', 'email', 'sex', 'dob', 'country_code', 'mobile',
                        'tags']
        },
        ORDER_TABLE_NAME: {
            'columns': ['order_id', 'user_id', 'payment_info', 'billing_address', 'delivery_address', ]
        }
    }
