# скачайте requests из Python Packages
import requests

from backend.notifications import push

que1 = [1, 2, 3, 4, 5] # очередь
token = "{{sensitive data}}"

# тут должен быть код, который добавляет id юзеров в список que и удаляет их слева-направо,
# при этом обновляя позицию каждого в списке так, что номер юзера в левом конце списка всегда равен [0].


text = "Ваша позиция в очереди - 5! Приготовьтесь!"

if chat_id == str(que1[4]):
    push(chat_id, text) # функция из notifications
