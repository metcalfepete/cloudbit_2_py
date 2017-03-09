# cloudbit_2_py
Python examples of how to connect to the (littleBits) Cloudbit REST API

The project contains the following examples:

* __lb_input.py__ - basic read Cloudbit input value
* __lb_tk_input.py__ - Tkinter read Cloudbit input value every 2 seconds
* __lb_tk_output.py__ - Tkinter set Cloudbit output value

#lb_input.py__ - basic read Cloudbit input value

The Cloudbit input value REST API is a streaming value, this can be a problem if the application is only expecting a single value. To simply get only a single data value a **break** can be used after reading the first line. A simple example to read only a single value is shown below.

```python
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

##lb_tk_input.py - Tkinter read Cloudbit input value every 2 seconds




```


