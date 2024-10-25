import os
import urllib.parse
from sqlalchemy.exc import OperationalError
from sqlalchemy import create_engine

# Lấy các giá trị từ biến môi trường
db_server = os.getenv('DB_SERVER')
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')
db_driver = os.getenv('DB_DRIVER')

# Config SQL server
params = urllib.parse.quote_plus(f"DRIVER={db_driver};"
                                 f"SERVER={db_server};"
                                 f"DATABASE={db_name};"
                                 f"UID={db_username};"
                                 f"PWD={db_password}")

connection_string = f"mssql+pyodbc:///?odbc_connect={params}"
engine = create_engine(connection_string)

def check_db_connection():
    try:
        # Tạo kết nối đến cơ sở dữ liệu
        connection = engine.connect()
        print("Connect SQL Server successfully!")
        connection.close()
    except OperationalError as e:
        print(f"Connect SQL Server failed: {e}")
