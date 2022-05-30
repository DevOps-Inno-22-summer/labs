from django.http import HttpResponse
from clock.utills import get_current_datetime


def index(request):
    return HttpResponse("Current date time in Moscow is: " + get_current_datetime())