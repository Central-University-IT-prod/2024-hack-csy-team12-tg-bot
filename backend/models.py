from datetime import datetime
from pydantic import BaseModel

class QueueStatistics(BaseModel):
    chat_id: int
    queue_time: datetime = datetime.now().time()
