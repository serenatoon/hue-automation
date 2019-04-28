import requests
import sys
import json


def get_light_data(ip, id):
    url = "http://" + ip + "/api/" + id + "/lights/3"
    req = requests.get(url)
    return req.json()


def get_light_state(ip, id):
    data = get_light_data(ip, id)
    return data['state']


def light_is_on(ip, id):
    data = get_light_state(ip, id)
    return data['on']


def toggle_light(ip, id):
    current_state = light_is_on(ip, id)
    url = "http://" + ip + "/api/" + id + "/lights/3/state"  # todo: light number as arg
    body = {
        "on": not current_state
    }
    requests.put(url, json.dumps(body))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: toggle.py IP ID"
    else:
        toggle_light(sys.argv[1], sys.argv[2])
