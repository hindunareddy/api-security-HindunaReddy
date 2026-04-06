from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 429:
            print("Error: Too many requests. Please try again later.")
            return

        elif response.status_code == 200:
            data = response.json()
            print("Weather fetched successfully!")
            print("Temperature:", data["main"]["temp"])

        else:
            print("Error:", response.status_code)

    except Exception as e:
        print("Exception occurred:", e)

# Do not log user location data to protect privacy (GDPR principle)

get_weather("London")