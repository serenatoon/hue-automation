import requests
import sys
import json


def turn_off_light(ip, id):
    url = "http://" + ip + "/api/" + id + "/lights/3/state"  # todo: light number as arg
    body = {
        "on": False
    }
    req = requests.put(url, json.dumps(body))
    print req.json()


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: off.py IP ID"
    else:
        turn_off_light(sys.argv[1], sys.argv[2])
