import sqlite3
from sqlite3 import Error
# import os.path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "8thMay.db")

class DBConnection:
    def sql_connection(self):
        try:
            con = sqlite3.connect('cab')
            return con
        except Error:
            print(Error)
