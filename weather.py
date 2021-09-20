import requests

# Take user input zip-code
zipcode = input("Enter zip-code: ")

# Validate the number of digits is correct
if len(zipcode) != 5:
    print("You must enter a 5 digit zip code")
    quit()

# URL GET request parameters
params = {'zip':zipcode, 'appid':'ca4edf7fd84d13a4f8a978b452bfa425'}

# API url
url = 'http://api.openweathermap.org/data/2.5/weather'

# GET request to Open Weather
response = requests.get(url, params=params)

# Print content in JSON
data = response.json()
 
# Store city as variable
city = (data['name'])

# Store temperature as variable
temperature = (data["main"]["temp"])

# Get weather
for conditions in data["weather"]:
    print("Current weather conditions in",city, zipcode,"are",conditions['main'],"with a temperature of",temperature)

# Handles 404 response code
if response.status_code == 404:
   print("Invalid request, verify that the zip-code and API Key are valid")