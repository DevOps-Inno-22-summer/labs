from django.http import HttpResponse
from clock.utills import get_current_datetime


def index(request):
    return HttpResponse(get_current_datetime())
