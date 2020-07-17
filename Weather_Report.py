import json
import requests
with open('data.json') as f:
    #reads api key from json and display as dictionary
    api = json.load(f)
    country_code=str(input("Enter valid country code to generate weather report:"))
url ="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(country_code,api["apikey"])
#makerequest
response=requests.get(url)
#gets complete JSon response
response_data=json.loads(response.text)
print(response_data)

min = response_data["main"]["temp_min"]
max = response_data["main"]["temp_max"]
print(("Weather Report of {}:\nMinimum Temperature:{} \nMaximum temperature{}".format(country_code,min,max)))

