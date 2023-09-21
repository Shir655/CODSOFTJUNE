import requests

api_key = '77c486d321b4e11a1ef5ce47efd6a062'

user_input = input("ENTER CITY: ")

weather_data =requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather= weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"THE WEATHER IN {user_input} IS: {weather}")
print(f"THE TEMPERATURE IN {user_input} IS: {temp}f")