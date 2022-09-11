import os
import urllib.request as urllib2
import json

while True:
    ip=input("What is your target IP: ")
    url="http://ip-api.com/json/"
    response=urllib2.urlopen(url+ip)
#     print(response)
    data=response.read()
#     print(data)
    values=json.loads(data)
#     print(values)
    
    print("IP: "+values["query"])
    print("City: "+values["city"])
    print("ISP: "+values["isp"])
    print("Country: "+values["country"])
    print("Region: "+values["region"])
    print("Timezone: "+values["timezone"])
    break
