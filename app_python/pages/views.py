from django.http import HttpResponse
from datetime import datetime


def homePageView(request):
    return HttpResponse(datetime.now())