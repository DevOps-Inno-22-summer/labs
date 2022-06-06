'''Get current time'''

from datetime import datetime, timezone, timedelta

def get_current_time(tzone: int) -> str:
    '''Get current time of timezone'''
    current_timezone = timezone(timedelta(hours=tzone))
    date = datetime.now(current_timezone).strftime("%H:%M:%S")
    return date
