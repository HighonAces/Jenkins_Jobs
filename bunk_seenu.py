import requests
from datetime import date
import os

discord_webhook_url = os.getenv(DISCORD_WEBHOOK_URL)
rapid_api_url = "https://daily-fuel-prices-update-india.p.rapidapi.com/car/v2/fuel/prices"


def daily_fuel_prices():
    querystring = {"cityId": "10005"}

    headers = {
        'src': "android-app",
        'appversion': "1.0",
        'deviceid': "abcd",
        'x-rapidapi-key': os.getenv(RAPID_API_KEY),
        'x-rapidapi-host': "daily-fuel-prices-update-india.p.rapidapi.com"
    }

    response = requests.request("GET", rapid_api_url, headers=headers, params=querystring)

    response = response.json()

    Message = {
        "content": "Fuel Prices on {} are:\n"
                   "Petrol:Rs.{}\n"
                   "Diesel:Rs.{}\n".format(date.today(), response['data']['fuelPrice']['petrol'],
                                           response['data']['fuelPrice']['diesel'])
    }
    requests.post(discord_webhook_url, data=Message)


daily_fuel_prices()
