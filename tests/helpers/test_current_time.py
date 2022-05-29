"""System module"""
from datetime import datetime, timezone, timedelta
from app_python.helpers.current_time import current_moscow_time

def test_current_moscow_time():
    """test current moscow time"""
    offset = timezone(timedelta(hours=3))
    assert current_moscow_time() == datetime.now(offset)
    