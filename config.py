from dotenv import load_dotenv
import os

load_dotenv()

POSTGRESS_DB_USER = os.environ.get("POSTGRESS_DB_USER")
POSTGRESS_DB_PASSWORD = os.environ.get("POSTGRESS_DB_PASSWORD")
POSTGRESS_DB_PORT = os.environ.get("POSTGRESS_DB_PORT")
POSTGRESS_DB_HOST = os.environ.get("POSTGRESS_DB_HOST")
POSTGRESS_DB_NAME = os.environ.get("POSTGRESS_DB_NAME")

