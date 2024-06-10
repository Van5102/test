import os
# from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# DB config
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')

MySQL_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# db_engine = create_engine(MySQL_URL, pool_size=100, pool_recycle=3600, pool_pre_ping=True)
class APP_CONFIG:
    SQLALCHEMY_DATABASE_URI = MySQL_URL
    SQLALCHEMY_ENGINE_OPTIONS = {}