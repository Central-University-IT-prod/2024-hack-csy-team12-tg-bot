from datetime import datetime

from notifications import push

queue: [{str: datetime}] = []
quetime = 10  # время для человека, который уже в интеркативе


def add_queue_place(chat_id):
    queue.append({chat_id: datetime.now()})
    return get_queue_statistic(chat_id)


def get_queue_statistic(chat_id):
    index = queue.index(next((item for item in queue if chat_id in item), None))
    return f'Ваша позиция в очереди: {index + 1}. \nОсталось ждать: ~{index * quetime}. минут'


def delete_queue(chat_id):
    index = queue.index(next((item for item in queue if chat_id in item), None))
    queue.remove(next((item for item in queue if chat_id in item), None))
    if index == 0:
        if len(queue) > 0:
            send_push(list(queue[0].keys())[0], 0)
        if len(queue) > 1:
            send_push(list(queue[1].keys())[0], 1)


def send_push(chat_id, index):
    if index == 0:
        return push(chat_id, f'Ваша очередь подошла , пожалуйста, подойдите к стенду ')
    elif index == 1:
        return push(chat_id, f'Ваша позиция в очереди: {index + 1}. \n пожалуйста,подойдите к стенду.')
