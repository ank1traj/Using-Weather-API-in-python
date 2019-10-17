import requests
import urllib


api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = input('City Name :')
url = api_address + city

headers = {}
#Header for websites
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

#Urllib code
req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)

json_data = requests.get(url).json()
format_add = json_data['base']
print(format_add)
