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

api.run()