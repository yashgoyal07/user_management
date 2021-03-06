from configs.mysql_config import MysqlConfig

CREATE_USER_QUERY = f"""INSERT INTO {MysqlConfig.DATABASE_NAME}.{MysqlConfig.USER_TABLE_NAME} """ + """({columns}) VALUES({params}) ON DUPLICATE KEY UPDATE"""

GET_USER_DATA_QUERY = """SELECT {columns}""" + f""" FROM {MysqlConfig.DATABASE_NAME}.{MysqlConfig.USER_TABLE_NAME}"""

CREATE_USER_TABLE = """CREATE TABLE `user` (
  `user_id` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `dob` datetime DEFAULT NULL,
  `country_code` varchar(20) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `tags` json DEFAULT NULL,
  `delivery_address` json DEFAULT NULL,
  `billing_address` json DEFAULT NULL,
  `payment_info` json DEFAULT NULL,
  `latest_order_id` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
