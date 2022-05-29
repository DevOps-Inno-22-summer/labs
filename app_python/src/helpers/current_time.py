"""System module"""
from datetime import datetime, timezone, timedelta

def current_moscow_time()-> datetime:
    """Current Moscow time"""
    offset = timezone(timedelta(hours=3))
    return datetime.now(offset)
