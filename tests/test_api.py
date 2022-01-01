from requests import get, post, delete
from json import load

URL = "http://localhost:8080%s"

def get_response(path, method, data=None):
    return method(URL % path, json=data)

def test_healthz():
    r = get_response("/healthz", get)
    assert r.status_code == 204
    assert len(r.text) == 0

def check_data(filename, goal_code):
    data_lst = load(open(filename))
    for data in data_lst:
        r = get_response("/data", post, data=data)
        assert r.status_code == goal_code

def test_data():
    check_data("good_post_data.json", 204)
    check_data("bad_post_data.json", 400)

def test_get_stats():
    data = load(open("sensor100_data.json"))
    r1 = get_response("/data", post, data=data)
    assert r1.status_code == 204

    r2 = get_response("/statistics/sensor100", get)
    r2_json = r2.json()
    assert r2_json["last_measurement"] == data[-1]["timestamp"]
    assert r2_json["count"] == len(data)
    assert r2_json["avg"] == sum(obj["value"] for obj in data) / len(data)

    get_response("/statistics/sensor100", delete)

def test_delete_stats():
    data = load(open("sensor200_data.json"))
    r1 = get_response("/data", post, data=data)
    assert r1.status_code == 204

    r3 = get_response("/statistics/sensor200", delete)

    r4 = get_response("/statistics/sensor200", get)
    assert r4.json()["count"] == 0