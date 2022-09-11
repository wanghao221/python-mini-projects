import requests
import json
from IPython.display import Image, display

# api-key
appId="944**************************"

# place input
query=input("Enter Your Place to Check Weather : ")

# queries
unit="metric"

# API url
url="https://api.openweathermap.org/data/2.5/weather?q="+f"{query}"+"&appid="+f"{appId}"+"&units="+f"{unit}"

# get response from api-hit
response=requests.get(url,stream=True)

# get data (in bytes form)
data=response.content

# get json file from "bytes" type
jsn=json.loads(data.decode("utf-8"))
jsn

# get temperature
temp=jsn["main"]["temp"]

# get weather icon
icon=jsn["weather"][0]["icon"]

# get weather description
weatherDesc=jsn['weather'][0]["description"]

# get request with imageUrl to fetch png image
imageUrl="https://openweathermap.org/img/wn/"+f"{icon}"+"@2x.png"
response2=requests.get(imageUrl,stream=True)

# display png
display(Image(response2.content))

# display temperature
print(f"Temperature : {temp}°C (Degree Celcius)")

# display place name
print(f"Place : {query}")

# display weather description
print(f"Weather Description : {weatherDesc}")
