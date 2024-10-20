from http.client import responses

import requests

url = "http://localhost:8080"



def add_queue_place(chat_id: str):
    response = requests.post(f"{url}/queue/place?chat_id={chat_id}")
    return response.json()

def get_queue_statistic(chat_id: str):
    response_text = requests.get(f"{url}/queue/statistics/?chat_id={chat_id}")
    return response_text.json()

def delete_queue_place(chat_id: str):
    requests.delete(f"{url}/queue/place?chat_id={chat_id}")
