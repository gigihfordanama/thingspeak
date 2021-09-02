import httplib2
import urllib
import time
import requests as req
import random
import http.client
from time import localtime, strftime
from urllib.request import urlopen as uReq

key = "4TSSXOMU03H52235"  # Put your API Key here
def sensor_jarak():
    while True:
        print ("KIRIM DATA BERHASIL")
        time.sleep(1)
        data = random.randint(0,250)
    
        #Calculate Distance by Random Number
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        params = urllib.parse.urlencode({'field1': data,'field2': data, 'field3': data, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print (data)
            print (response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print ("connection failed")
        break
if __name__ == "__main__":
        while True:
                sensor_jarak()
