#
# lb_tk_output.py
#
from Tkinter import *
import json
import requests

# update your auth Token and device ID
authToken = "4f3830b44e1d4b27xxxx"
deviceId = "00e04c0379bb"

littleBitsUrl = "https://api-http.littlebitscloud.cc/devices/" + deviceId + "/output"

headers = {"Authorization": "Bearer " + authToken, "Content-type": "application/json"}

def setvalue():
	thevalue = lb_value.get()
	thetime = lb_duration.get()
	body = {"percent": thevalue , "duration_ms": thetime}
	thebody = json.dumps(body)
	print body, thebody
	#r = requests.post(littleBitsUrl,  data=body, headers=headers)
	r = requests.post(littleBitsUrl,  data=thebody, headers=headers)
	print r
     

root = Tk()
root.title('littleBits Output')

Label(text = "Value (0-100) :",width=30).grid(row=0,column=0)
lb_value = Entry(root, width= 10)
lb_value.grid(row=0,column=1)
Label(text = "Duration (ms) (constant=-1) :",width=30).grid(row=1,column=0)
lb_duration = Entry(root, width= 10)
lb_duration.grid(row=1,column=1)


Button(root, text=' Set Output ', bg='silver', command=setvalue).grid(row=2,column=1)

root.mainloop()
