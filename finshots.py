import requests
from bs4 import BeautifulSoup
import os

discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")


def get_link_of_latest_story():
    response = requests.get("https://finshots.in/archive/")
    soup = BeautifulSoup(response.text, 'html.parser')
    link = soup.find_all("a", {"class": "post-card-image-link"})[0]['href']
    link2 = "https://finshots.in" + link
    Message = {
        "content": link2
    }
    requests.post(discord_webhook_url, data=Message)


get_link_of_latest_story()