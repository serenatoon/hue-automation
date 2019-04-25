import requests
import sys
import json


def turn_on_light(ip, id):
	url = "http://" + ip + "/api/" + id + "/lights/3/state" # todo: light number as arg
	body = {
		"on": True
	}
	req = requests.put(url, json.dumps(body))
	print req.json()



if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "Script usage: on.py IP ID"
    else:
        turn_on_light(sys.argv[1], sys.argv[2])
