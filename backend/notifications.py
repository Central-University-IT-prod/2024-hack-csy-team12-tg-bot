# скачайте requests из Python Packages
import requests
token = "{{sensitive data}}"
# надо решить проблему - как связать id юзера с этим кодом (пока для user написал None):
def push(chat_id, text):
    url = f"https://api.telegram.org/bot{token}"
    params = {f"chat_id": chat_id, text: "Hello World"}
    r = requests.get(url + "/sendMessage", params=params)
