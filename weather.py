import requests

# API url
url = 'http://api.openweathermap.org/data/2.5/weather?zip=21230,&appid={API_KEY}'
# GET request to Open Weather
response = requests.get(url)
# Print content in JSON
print(response.json())
