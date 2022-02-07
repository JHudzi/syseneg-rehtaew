from database import DatabaseManager
from model.sensor import Sensor
class Reading:
    def __init__(self, id, read_sen_link, temperature, humidity, windspeed, timestamp=None):
        self.id = id
        self.read_sen_link = read_sen_link
        self.temperature = temperature
        self.humidity = humidity
        self.windspeed = windspeed
        self.timestamp = timestamp

    def save(self):
        db_manager = DatabaseManager()
        query_string = "INSERT INTO Reading (read_sen_link, temperature, humidity, windspeed) values(?, ?, ?, ?)"
        result = db_manager.run_query(query_string, [self.read_sen_link, self.temperature, self.humidity, self.windspeed])
        if result["success"]:
            self.saved = True
            return True
        return False

    ### Static Methods
    @staticmethod
    def get_all_readings():
        db_manager = DatabaseManager()
        query = "SELECT * FROM Reading"
        result = db_manager.run_query(query) 
        reading = list(map(lambda row: Reading(row[0], row[1], row[2], row[3], row[4], row[5]), 
            result["data"]
        ))
        return reading

    @staticmethod
    def get_reading_by_sensor(sen_read_link):
        db_manager = DatabaseManager()
        query = "SELECT * FROM Reading WHERE read_sen_link = ?"
        result = db_manager.run_query(query, [sen_read_link])

        reading = list(map(lambda row: Reading(row[0], row[1], row[2], row[3], row[4], row[5]), 
            result["data"]
        ))
        return reading