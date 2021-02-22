import os
import json
from datetime import datetime


def get_environment():
    return os.environ.get('my_env', 'local')


def filter_query_generator(request_filters, query):
    request_dob = request_filters.get('dob', {})
    request_user_ids = request_filters.get('user_ids', [])
    request_dob_start_date = request_dob.get('start_date', None)
    request_dob_end_date = request_dob.get('end_date', None)

    where_clause = []

    if request_user_ids:
        users_params = "'" + "','".join(request_user_ids) + "'"
        where_clause.append(" user_id IN ({})".format(users_params))

    if request_dob_start_date and request_dob_end_date:
        where_clause.append("dob BETWEEN '{}' AND '{}'".format(request_dob_start_date, request_dob_end_date))

    if len(where_clause) > 0:
        query += " WHERE "
        query += " AND ".join(where_clause)

    return query


def load_json_strings(users_data):
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
