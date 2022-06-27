"""System module"""
from datetime import datetime, timezone, timedelta

def current_moscow_time()-> datetime:
    """Current Moscow time"""
    offset = timezone(timedelta(hours=3))
    return datetime.now(offset)

def record_access():
    """ record access to root pass by a client"""
    with open('visits.txt', 'a',encoding='UTF-8') as file:
        file.write(f'The root pass is accessed by a client at: {datetime.now()}')

def get_visits_content():
    """ Get content of visits file """
    with open('visits.txt', encoding='UTF-8') as file:
        contents = file.read()
    return contents
