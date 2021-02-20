from configs.mysql_config import MysqlConfig

INSERT_DATA_QUERY_TEMPLATE = """INSERT INTO {DATABASE_NAME}.{TABLE_NAME} """

CREATE_USER_QUERY_TEMPLATE = INSERT_DATA_QUERY_TEMPLATE \
    .format(DATABASE_NAME=MysqlConfig.DATABASE_NAME,
            TABLE_NAME=MysqlConfig.USER_TABLE_NAME
            )

CREATE_USER_QUERY = CREATE_USER_QUERY_TEMPLATE + """({columns}) VALUES({params})"""

CREATE_USER_TABLE = """CREATE TABLE `user` (
  `user_id` varchar(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `country_code` varchar(20) DEFAULT NULL,
  `mobile` varchar(20) DEFAULT NULL,
  `tags` json DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
