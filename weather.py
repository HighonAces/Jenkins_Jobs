import requests
import os
from datetime import date

key = os.getenv("RAPID_API_KEY")
discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
url = "https://aerisweather1.p.rapidapi.com/observations/hyderabad,%20india"


def current_weather():
    headers = {
        'x-rapidapi-key': key,
        'x-rapidapi-host': "aerisweather1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    response = response.json()
    Message = {
        "content": "Hyderabad\nWeather: {}\nTemp: {}\nHumidity: {}\nFeels like: {}".format(
            response["response"]["ob"]["weather"], response["response"]["ob"]["tempC"],
            response["response"]["ob"]["humidity"], response["response"]["ob"]["feelslikeC"])
    }
    requests.post(discord_webhook_url, data=Message)


current_weather()
