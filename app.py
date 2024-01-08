import requests

api_key = "71849053b6dbf56791f70b5365a0bad9"

user_input = input("Enter a city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("no city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']

print(f"the weather in {user_input} is: {weather}")
print(f"the temperature in {user_input} is: {temp} degrees F")
