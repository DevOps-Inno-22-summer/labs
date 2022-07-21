from datetime import datetime as dt, timezone, timedelta
from django.http import HttpResponse, HttpRequest


def get_moscow_time(request: HttpRequest):
    moscow_tz = timezone(timedelta(hours=3))
    moscow_time = dt.now(moscow_tz)

    with open('/app_volume/visits.txt', 'a') as f:
        f.write(f'Visited at {moscow_time}\n')
    return HttpResponse(moscow_time.strftime("%H:%M"))


def get_visits(request: HttpRequest):
    with open('/app_volume/visits.txt', 'r') as f:
        content = f.read()
    return HttpResponse(content)
