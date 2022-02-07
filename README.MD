## ---------------------- Requirements ------------------------
pip 
Python 3.10
virtualenv

## ---------------------- Deploying ------------------------
cd ./Working_directory
.\venv\Scripts\activate
pip install -r requirements.txt

## ---------------------- Queries ------------------------
# Get all sensors
curl --location --request GET 'http://127.0.0.1:5000/sensor/all'\
--header 'Content-Type: application/json'\

# Get specific Sensor by id
curl --location --request GET 'http://127.0.0.1:5000/sensor/1' \
--header 'Content-Type: application/json' \

# Get all readings
curl --location --request GET 'http://127.0.0.1:5000/reading/all' \
--header 'Content-Type: application/json' \

# Get specific Reading by unique link
curl --location --request GET 'http://127.0.0.1:5000/reading/IRE3' \
--data-raw ''
 
# Create sensor
curl --location --request POST 'http://127.0.0.1:5000/sensor/add' \--header 'Content-Type: application/json' 
\--data-raw '{"id": "id", "sen_read_link": "PLD1", "country":"Poland", "city": "Warsaw"}

# Create reading
curl --location --request POST 'http://127.0.0.1:5000/reading/add' \--header 'Content-Type: application/json' \
--data-raw '{"id": "id","read_sen_link": "IRE3", "temperature": "-69", "humidity": "69", "windspeed": "69", "timestamp": "timestamp"}'

# Get average attributes
## Failing on response attributes
curl --location --request GET 'http://127.0.0.1:5000/get_average' \--header 'Content-Type: application/json' \
--data-raw '{   "read_sen_link": "IRE3", "attribute": "humidity", "start_day": "2022-02-04", "end_day": "2022-02-07", "average": ""}
