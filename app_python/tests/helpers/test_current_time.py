"""System module"""
from datetime import datetime, timezone, timedelta
from src.helpers.current_time import current_moscow_time

def test_current_moscow_time():
    """test current moscow time"""
    offset = timezone(timedelta(hours=3))
    gotten_response = str(current_moscow_time()).split(" ")
    expected_response = str(datetime.now(offset)).split(" ")
    assert gotten_response[0] == expected_response[0]
    gotten_response = gotten_response[1].split(".")
    expected_response = expected_response[1].split(".")
    assert gotten_response[0] == expected_response[0]
    