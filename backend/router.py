from fastapi import APIRouter

from bot import delete_queue, get_queue_statistic, add_queue_place

api_router = APIRouter()  # noqa: pylint=invalid-name


@api_router.post('/queue/place')
async def message(chat_id: str = None):
    res = add_queue_place(chat_id)
    return res


@api_router.get('/queue/statistics')
async def message(chat_id: str = None):
    res = get_queue_statistic(chat_id)
    return res


@api_router.delete('/queue/place')
async def message(chat_id: str = None):
    res = delete_queue(chat_id)
    return res
