from flask import Flask, request
from collections import defaultdict

api = Flask("tagup-api")
measurements = defaultdict(list)
last_measurement = None
count = 0

@api.route('/healthz')
def get_healthz():
    return "", 204

@api.route('/data', methods=["POST"])
def post_data():
    global measurements, last_measurement, count
    for data in request.json:
        measurements[data["sensor"]].append(data["value"])
        last_measurement = data["timestamp"]
        count += 1

    return "", 201

@api.route('/statistics/<string:id>')
def get_stats(id):
    response = {"last_measurement" : last_measurement, "count" : count}
    response["avg"] = sum(measurements[id])/(len(measurements[id]) or 1)
    return response, 200

api.run()