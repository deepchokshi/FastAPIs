import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path('.') / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME = "First Project"
    PROJECT_VERSION = "1.0.0"

    DB_PORT = os.getenv('DB_PORT')
    DB_NAME = os.getenv('DB_NAME')
    DB_LOGIN = os.getenv('DB_LOGIN')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_ADDRESS = os.getenv('DB_ADDRESS')
    DB_URL = f"postgresql://{DB_LOGIN}:{DB_PASSWORD}@{DB_ADDRESS}/{DB_NAME}"


settings = Settings()
