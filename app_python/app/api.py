from fastapi.routing import APIRouter
from datetime import datetime
import pytz

from . import schemas

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.get(
    "/current_time",
    response_model=schemas.CurrentTime,
)
def current_time():
    tz = 'Europe/Moscow'
    return schemas.CurrentTime(
        time_zone=tz,
        time=datetime.now(pytz.timezone(tz))
    )
