import sqlite3

class DatabaseManager:
    DATABASE_NAME = "weather.db"

    def __init__(self):
        pass

    def __get_connection(self):
        return sqlite3.connect(DatabaseManager.DATABASE_NAME)

    def run_query(self, query, params=[]):
        connect = self.__get_connection()
        cursor = connect.cursor()

        response = {"success":None, "msg":None, "data":None}        
        try:
            cursor.execute(query, params)
            connect.commit()
            response["success"] = True
            response["msg"] = "Success"
            response["data"]  = cursor.fetchall()

        except sqlite3.OperationalError as err:
            response["success"] = False
            response["msg"] = str(err)

        finally:
            connect.close()
        
        return response

    ## Initialization data for application
    def create_database(self):
        connect = self.__get_connection()
        cursor = connect.cursor()

        cursor.execute('''PRAGMA foreign_keys = ON''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Sensor(id INTEGER PRIMARY KEY AUTOINCREMENT,
            sen_read_link TEXT NOT NULL UNIQUE,
            country TEXT, 
            city TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Reading(id INTEGER PRIMARY KEY AUTOINCREMENT,
            read_sen_link TEXT NOT NULL, 
            temperature INT, 
            humidity INT,
            windspeed INT, 
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )''')
        
        connect.commit()
        connect.close()