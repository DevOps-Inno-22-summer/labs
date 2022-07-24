from django.http import HttpResponse
from datetime import datetime


def homePageView(request):
    with open('timelogger.txt', 'a') as f:
        print(datetime.now(), file=f)
    return HttpResponse("Hey from home. We have logged your time")


def visitsPageView(request):
    return HttpResponse(datetime.now())