# скачайте requests из Python Packages
import os
import requests

#token = os.getenv('TOKEN')
token = '{{sensitive data}}'
# надо решить проблему - как связать id юзера с этим кодом (пока для user написал None):
def push(chat_id, text):
    url = f"https://api.telegram.org/bot{token}"
    params = {f"chat_id": chat_id, "text": text}
    requests.get(url + "/sendMessage", params=params)
