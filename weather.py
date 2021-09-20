import requests

# API url
url = 'http://api.openweathermap.org/data/2.5/weather?zip=21230,&appid=ca4edf7fd84d13a4f8a978b452bfa425'
# GET request to Open Weather
response = requests.get(url)
# Print content in JSON
print(response.json())