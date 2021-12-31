from flask import Flask, request
api = Flask("tagup-api")
data = []

@api.route('/healthz')
def get_healthz():
    return "", 204

@api.route('/data', methods=["POST"])
def post_data():
    global data
    data += request.json
    return "", 201

api.run()