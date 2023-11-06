from dotenv import load_dotenv
import os
import requests
from pprint import pprint

load_dotenv()

def get_weather(city="Colombo"):

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("API_KEY")}&units=metric'
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    city = input("Enter your city: ")

    # Check for empty string and strip leading and trailing spaces
    if not bool (city.strip()):
        city = "Colombo"
    weather_data = get_weather(city)

    pprint(weather_data)
