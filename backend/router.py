from fastapi import APIRouter
from starlette import status
from starlette.responses import Response

from bot import proceed_release, proceed_custom, queue, delete_queue, get_queue_statistic, add_queue_place
from models import Body, Actions, Message

api_router = APIRouter()  # noqa: pylint=invalid-name


@api_router.post('/queue/place/')
async def message(chat_id: str = None):
    res = await add_queue_place(chat_id)
    return Response(status_code=res.status_code)


@api_router.get('/queue/statistics/')
async def message(chat_id: str = None):
    res = await get_queue_statistic(chat_id)
    return Response(status_code=res.status_code)


@api_router.delete('/queue/place/')
async def message(chat_id: str = None):
    res = await delete_queue(chat_id)
    return Response(status_code=res.status_code)
