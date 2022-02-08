from database import DatabaseManager

class Sensor:
    def __init__(self, id, sen_read_link, country, city):
        self.id = id
        self.sen_read_link = sen_read_link
        self.country = country
        self.city = city

    def save(self):
        db_manager = DatabaseManager()
        query_string = "INSERT INTO Sensor (sen_read_link, country, city) values(?, ?, ?)"
        result = db_manager.run_query(query_string, [self.sen_read_link, self.country, self.city])    
        if result["success"]:
            self.saved = True
            return True
        return False

    def delete(self):
        db_manager = DatabaseManager()
        query_string = "DELETE FROM Sensor WHERE read_sen_link = ?"
        result = db_manager.run_query(query_string, [self.sen_read_link])    
        if result["success"]:
            self.saved == False
            return True
        return False

    ### Static Methods
    @staticmethod
    def get_all_sensors():
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensor"
        result = db_manager.run_query(query)
        
        sensors = list(map(lambda row: Sensor(row[0], row[1], row[2], row[3]), 
            result["data"]
        ))
        return sensors

    @staticmethod
    def get_sensor_by_unique(id):
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensor WHERE id = ?"
        result = db_manager.run_query(query, [id])

        sensor = None
        if result["data"]:
            row = result["data"][0]
            sensor = Sensor(row[0], row[1], row[2], row[3])
        return sensor

    @staticmethod
    def sen_read_link_exists(sen_read_link):
        db_manager = DatabaseManager()
        query = "SELECT * FROM Sensor WHERE sen_read_link = ?"
        result = db_manager.run_query(query, [sen_read_link])
        if result["data"]:
            return True
        return False
