from flask import Flask, jsonify, request
from apis.averageApi import GetSensorData
from model.sensor import Sensor
from model.reading import Reading
#from api.get_metrics_for_sensors import GetMetricsForSensors

app = Flask(__name__)
"""
Route Endpoint
"""
@app.route("/")
def index():
    return jsonify(
        api = "Example use URL endpoints like /reading/all to interact with the API"
    )
"""
Sensor Endpoint: Use /add, /all, and /<sen_read_link> to get the required data

-----------------------TEST-------------------------------
curl --location --request POST 'http://127.0.0.1:5000/sensor/add' \
--header 'Content-Type: application/json' \
--data-raw '
{"id": "id", "sen_read_link": "PLD1", "country": "Poland", "city": "Warsaw"}
----------------------PASS---------------------------------
"""
@app.route("/sensor/add", methods=["POST"])
def add_sensor():
    request_data = request.get_json()
    print(request_data)
    try:
        sensor = Sensor(request_data["id"], request_data["sen_read_link"], request_data["country"], request_data["city"])
        result = sensor.save()
        if result:
            return jsonify(code=201, msg="New Sensor Added")
        else:
            return jsonify(code=500, msg="Object Not Instantiated")
    except KeyError:
        return jsonify(code = 400, msg = "Attribute key missing")
    except ValueError: 
        return jsonify(code = 500, msg = "Server Error")

"""
-----------------------TEST-------------------------------
curl --location --request GET 'http://127.0.0.1:5000/sensor/all'\
--header 'Content-Type: application/json'\
----------------------PASS---------------------------------
"""
@app.route("/sensor/all")
def get_all_sensors():
    sensors = Sensor.get_all_sensors()
    response = {}
    for sensor in sensors:
        response[sensor.sen_read_link] = {
            "id": sensor.id,
            "sen_read_link": sensor.sen_read_link,
            "country": sensor.country,
            "city": sensor.city,
        }
    return jsonify(response)

"""
-----------------------TEST-------------------------------
curl --location --request GET 'http://127.0.0.1:5000/sensor/1' \
--header 'Content-Type: application/json' \
----------------------PASS---------------------------------
"""
@app.route("/sensor/<id>")
def get_sensor_by_unique(id):
    sensor = Sensor.get_sensor_by_unique(id)
    
    if sensor:
        return jsonify({ 
            "id": sensor.id,
            "sen_read_link": sensor.sen_read_link,
            "country": sensor.country,
            "city": sensor.city,
        })
    else:
        return jsonify({})

"""
Reading Endpoint: Use /reading --> /add, /all, and /<read_sen_link> to get the required data

-----------------------TEST-------------------------------
curl --location --request POST 'http://127.0.0.1:5000/reading/add' \
--header 'Content-Type: application/json' \
--data-raw '{"id": "id","read_sen_link": "IRE3", "temperature": "-69", 
"humidity": "69", "windspeed": "69", "timestamp": "timestamp"}'
----------------------PASS---------------------------------
"""
@app.route("/reading/add", methods=["POST"])
def add_reading():
    request_data = request.get_json() 
    print(request_data)  
    try:
        reading = Reading(request_data["id"], request_data["read_sen_link"], request_data["temperature"], request_data["humidity"], request_data["windspeed"])
        result = reading.save()
        
        if result:
            return jsonify(code=201, msg="New Reading Added")
        else:
            return jsonify(code=500, msg="Object Not Instantiated")
    except KeyError:
        return jsonify(code = 400, msg = request_data)
    except ValueError: 
        return jsonify(code = 500, msg = "Server Error")

"""
-----------------------TEST-------------------------------
curl --location --request GET 'http://127.0.0.1:5000/reading/all' \
--header 'Content-Type: application/json' \
----------------------PASS---------------------------------
"""
@app.route("/reading/all")
def get_all_readings():
    reading = Reading.get_all_readings()
    response = {}
    for data in reading:
        if data.read_sen_link not in response.keys():
            response[data.read_sen_link] = []

        response[data.read_sen_link].append({
            "read_sen_link": data.read_sen_link,
            "temperature": data.temperature,
            "humidity": data.humidity,
            "windspeed": data.windspeed,
            "timestamp": data.timestamp
        })
    return jsonify(response)

"""
-----------------------TEST-------------------------------
curl --location --request GET 'http://127.0.0.1:5000/reading/IRE3' \
--data-raw ''
----------------------PASS---------------------------------
"""
@app.route("/reading/<read_sen_link>")
def get_reading_by_sensor(read_sen_link):
    reading = Reading.get_reading_by_sensor(read_sen_link)
    
    response = {}
    for data in reading:
        if data.read_sen_link not in response.keys():
            response[data.read_sen_link] = []

        response[data.read_sen_link].append({
            "read_sen_link": data.read_sen_link,
            "temperature": data.temperature,
            "humidity": data.humidity,
            "windspeed": data.windspeed,
            "timestamp": data.timestamp
        })
    return jsonify(response)


"""
Average Endpoint: Use /get_average to get the average data in any mix over any time

--------------------TEST----------------------
curl --location --request GET 'http://127.0.0.1:5000/get_average' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "read_sen_link": "IRE3",
    "attribute": "humidity",
    "start_day": "2022-02-04",
    "end_day": "2022-02-07",
    "average": ""
}

---------FAIL-----------------

"""
@app.route("/get_average")
def sensor_average():
    try:
        result = GetSensorData(request.args["read_sen_link"], request.args["attribute"], request.args["start_day"], request.args["end_day"])
        return jsonify(result.calculate())
    except KeyError:
        return jsonify(code = 400, msg = "Attribute key missing")




if __name__ == '__main__':
    app.run(debug=True)
