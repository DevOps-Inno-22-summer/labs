from pydantic import BaseModel
from datetime import datetime


class CurrentTime(BaseModel):
    time_zone: str
    time: datetime
