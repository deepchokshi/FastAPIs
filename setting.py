import logging
import os
from dotenv import load_dotenv

log = logging.getLogger()
log.setLevel(logging.DEBUG)
env = load_dotenv()

class PostgresConfiguration:
    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_LOGIN = os.getenv('DB_LOGIN')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_ADDRESS = os.getenv('DB_ADDRESS')

    @property
    def postgres_db_path(self):
        url = f"postgresql://{self.DB_LOGIN}:{self.DB_PASSWORD}@" \
              f"{self.DB_ADDRESS}" \
              f"/{self.DB_NAME}"
        return url
