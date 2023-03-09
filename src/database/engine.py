import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_ENGINE = os.getenv('DB_ENGINE')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

db_connection_url = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(url=db_connection_url)
