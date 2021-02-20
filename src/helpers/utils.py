import os


def get_environment():
    return os.environ.get('my_env', 'local')
