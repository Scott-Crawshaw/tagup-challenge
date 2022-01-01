# Scott Crawshaw
# Tagup backend challenge

from flask import Flask, request
from collections import defaultdict

api = Flask("tagup-api")

measurements = defaultdict(list) # using defaultdict helps eliminate sensor initialization code

# returns 204 if server is running
@api.route('/healthz', methods = ["GET"])
def get_healthz():
    return "", 204

# accepts JSON array of measurements and stores them in measurements dictionary
@api.route('/data', methods = ["POST"])
def post_data():
    global measurements
    try:
        for data in request.json:
            assert "timestamp" in data and "value" in data and "sensor" in data # ensure all keys are present
            assert type(data["value"]) in [int, float] # ensure 'value' is numeric
            sensor_id = data.pop("sensor")
            measurements[sensor_id].append(data)
        return "", 204
    # case where request.json is not a list
    except TypeError:
        return "Body of request must be a JSON array. Please check request and try again.", 400
    # case where 'sensor', 'value', or 'timestamp' keys do not exist, or 'value' is non-numeric
    except AssertionError:
        return "All measurements must contain 'sensor', 'value', and 'timestamp' keys, and 'value' must be numeric. Please check request and try again.", 400

# returns the following as a JSON object:
# timestamp of last measurement for sensor ('null' if no measurements)
# total number of measurements for sensor (0 if no measurements)
# average value of measurements for sensor (0 if no measurements)
@api.route('/statistics/<string:id>', methods = ["GET"])
def get_stats(id):
    response = {}
    response["count"] = len(measurements[id])
    response["avg"] = sum(data["value"] for data in measurements[id])/(len(measurements[id]) or 1)
    if response["count"] > 0:
        response["last_measurement"] = measurements[id][-1]["timestamp"]
    else:
        response["last_measurement"] = None
    return response, 200

# deletes measurements for given sensor id
@api.route('/statistics/<string:id>', methods = ["DELETE"])
def delete_stats(id):
    measurements.pop(id, None)
    return "", 204

api.run()