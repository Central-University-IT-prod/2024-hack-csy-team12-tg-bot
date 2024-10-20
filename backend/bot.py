import os
from datetime import datetime
from urllib.parse import urljoin, quote
import httpx
from httpx import Response


from models import Body, Message
from settings import TG_API_URL
from untils import make_message
get=input # ввод времени на сеанс
queue: [{str: datetime}] = []
quetime = 10 #время для человека, который уже в интеркативе

async def add_queue_place(chat_id):
    queue.append({chat_id: datetime.now()})
    return get_queue_statistic(chat_id)


async def get_queue_statistic(chat_id):
    index = queue.index({chat_id: datetime.now()})
    return f'Ваша позиция в очереди: {index + 1}. \nОсталось ждать: ~{get}.' # d {} gjckt осталось ждать формула расчета времени

async def delete_queue(chat_id):
    queue.remove({chat_id:datetime.now()})
    index = queue.index({chat_id:datetime.now()})
    if index <2 :
        return  send_push(index)

async def send_push(index):
    if index == 0:
        return f'Ваша очередь подошла , пожалуйста, подойдите к стенду '
    elif index == 1:
        return f'Ваша позиция в очереди: {index + 1}. \n пожалуйста,подойдите к стенду.'
















    # Предупредить первого, что его очередь пришла
    # Предупредить вторго, что его очередь скоро придет