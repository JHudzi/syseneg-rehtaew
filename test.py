import pytest
from model.sensor import Sensor
from model.reading import Reading 

@pytest.fixture
def valid_sensor():
    sensor = Sensor("1", "JAV3", "Java", "Jakarta ")
    yield sensor
    sensor.delete()

def test_sensor_save_successful(valid_sensor):
    saved = valid_sensor.save()
    assert saved == True

@pytest.fixture
def valid_reading():
    sensor = Sensor("2", "FRA", "France", "Parid")
    sensor.save()
    reading = Reading("1", "FRA", 1, 1, 1)    
    yield reading
    sensor.delete()

def test_reading_valid(valid_reading):
    saved = valid_reading.save()
    assert saved == True