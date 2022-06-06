from datetime import datetime as dt, timezone, timedelta
from django.http import HttpResponse, HttpRequest


def get_moscow_time(request: HttpRequest):
    moscow_tz = timezone(timedelta(hours=3))
    moscow_time = dt.now(moscow_tz)
    return HttpResponse(moscow_time.strftime("%H:%M"))
