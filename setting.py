import logging
import os
from dotenv import loa

log = logging.getLogger()
log.setLevel(logging.DEBUG)
env = load_dotenv()

class PostgresConfiguration:
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_LOGIN = os.getenv('DB_LOGIN')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_ADDRESS = os.getenv('DB_ADDRESS')
