from flask import Flask
api = Flask("tagup-api")

@api.route('/healthz/')
def get_healthz():
    return ("", 204)

api.run()