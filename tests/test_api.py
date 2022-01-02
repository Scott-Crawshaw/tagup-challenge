# Scott Crawshaw
# Tagup backend challenge

from requests import get, post, delete
from json import load

URL = "http://localhost:8080%s"


# Helper Function
# Hits the api and returns reponse.
def get_response(path, method, data=None):
    return method(URL % path, json=data)


# Helper Function
# Pulls json from file, posts each array to endpoint, ensures status code.
def check_data(filename, goal_code):
    data_lst = load(open(filename))
    for data in data_lst:
        r = get_response("/data", post, data=data)
        assert r.status_code == goal_code


# Ensures GET /healthz endpoint returns 204
def test_healthz():
    r = get_response("/healthz", get)
    assert r.status_code == 204
    assert len(r.text) == 0


# Ensures POST /data endpoint works as intended
def test_data():
    # Ensure that good dataset returns 204 status code
    check_data("good_post_data.json", 204)

    # Ensure that bad dataset returns 400 status code
    check_data("bad_post_data.json", 400)


# Ensures GET /statistics endpoint works as intended
def test_get_stats():
    # Post sensor100 data and ensure 204 status code
    check_data("sensor100_data.json", 204)

    # Get sensor100 stats and ensure they match expectations
    data = load(open("sensor100_data.json"))[0]
    r2 = get_response("/statistics/sensor100", get)
    r2_json = r2.json()
    assert r2_json["last_measurement"] == data[-1]["timestamp"]
    assert r2_json["count"] == len(data)
    assert r2_json["avg"] == sum(obj["value"] for obj in data) / len(data)

    # Delete sensor 100 stats to allow for future testing
    get_response("/statistics/sensor100", delete)


# Ensures DELETE /statistics endpoint works as intended
def test_delete_stats():
    # Post sensor200 data and ensure 204 status code
    check_data("sensor200_data.json", 204)

    # Delete sensor200 data
    r3 = get_response("/statistics/sensor200", delete)

    # Ensure sensor200 stats have been deleted
    r4 = get_response("/statistics/sensor200", get)
    assert r4.json()["count"] == 0