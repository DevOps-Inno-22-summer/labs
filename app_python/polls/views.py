from django.shortcuts import render
from django.http import HttpResponse
import time as t
from datetime import datetime as dt, timezone as tz, timedelta as td


def index(request):
    return HttpResponse(request_time())
    
def request_time():
    return (dt.utcnow() + td(hours=3)).strftime("%H:%M")
