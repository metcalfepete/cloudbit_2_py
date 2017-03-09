#
# lb_input.py - read input from a Cloudbit device
#
import json
import requests


requests.packages.urllib3.disable_warnings()

# Change with your Authorization code and deviceID
authToken = "4f3830b44e1d4b27xxxxxx"
deviceId = "00e04c0379bb"

littleBitsUrl = "https://api-http.littlebitscloud.cc/devices/" + deviceId + "/input"

headers = {"Authorization": "Bearer " + authToken,"Content-type": "application/json"}
r = requests.get(littleBitsUrl, headers=headers, stream=True)

for line in r.iter_lines():
    if "StatusCode" in line:
        # there is an error
        print line
    else:
        # parse the response to get the JSON data
        result = json.loads(line.split('data:')[1])
        print "percent   : ", result['percent']
    break



