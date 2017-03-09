from Tkinter import *
import json
import requests
#
# lb_tk_input.py
#
import datetime, time

requests.packages.urllib3.disable_warnings()

# update your auth Token and device ID
authToken = "4f3830b44e1d4b27xxxx"
deviceId = "00e04c0379bb"

littleBitsUrl = "https://api-http.littlebitscloud.cc/devices/" + deviceId + "/input"

headers = {"Authorization": "Bearer " + authToken, "Accept": "application/vnd.littlebits.v2+json"}

def getvalue():
    r = requests.get(littleBitsUrl, headers=headers, stream=True)
    for line in r.iter_lines():
        print line
        # Parse the line, get the results, then break
        result = json.loads(line.split('data:')[1])
        thevalue = result['percent']
        lb_value['text']="Input : " + str(thevalue) 
        thetime = datetime.datetime.fromtimestamp(result['timestamp']/1000)
        lb_time['text'] = "Time : " + str(thetime.date()) + " " + str(thetime.time())
        root.update()
        break

root = Tk()
root.title('littleBits Input')

lb_value = Label(root, text="Input : ", width= 40)
lb_value.pack(side = BOTTOM)
lb_time = Label(root, text= "Time : ")
lb_time.pack(side = BOTTOM)

while True:
	getvalue()
	time.sleep(2)





