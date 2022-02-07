from model.reading import Reading
from datetime import datetime
from functools import reduce


class GetSensorData:
    def __init__(self, read_sen_link, attribute, start_day, end_day):
        self.read_sen_link = self.__parse_arg(read_sen_link)
        self.attribute = self.__parse_arg(attribute)
        self.start_day = self.__parse_day(start_day)
        self.end_day = self.__parse_day(end_day)
        self.average = {}

    def get_reading(self):
        sensor = list(map(lambda sen_read_link: Reading.get_reading_by_sensor(sen_read_link), self.read_sen_link))
        return [item for reading in sensor for item in reading]
    
    def filter_by_dates(self, reading):
        return [ data for data in reading
            if self.start_day <= self.__parse_datetime(data.timestamp) <= self.end_day]
            
    def get_average(self, attribute, reading):
        return reduce(lambda x,y: x+y, [vars(data)[attribute] for data in reading]) / len(reading)

    def get_return(self):
        return {
            "read_sen_link": self.read_sen_link,
            "attribute": self.attribute,
            "start_day": self.start_day,
            "end_day": self.end_day,
            "average": self.average
        }
    """
    Process data and formated 
    """
    def calculate(self):
        reading = self.get_reading()
        print(reading)
        if not reading:
            return self.get_return()
        
        reading = self.filter_by_dates(reading)
        if not reading:
            return self.get_return()
        
        if not self.attribute:
            return self.get_return()

        for attribute in self.attribute:
            self.average[attribute] = self.get_average(attribute, reading)

        return self.get_return()

    """
    Create a readible syntax and filter specific day
    """
    def __parse_arg(self, arg):
        if "," in arg:
            return arg.split(",")
        return [arg]

    def __parse_day(self, arg):
        return datetime.strptime(arg, "%d-%m-%Y")

    def __parse_datetime(self, arg):
        return datetime.strptime(arg, "%Y-%m-%d %H:%M:%S")