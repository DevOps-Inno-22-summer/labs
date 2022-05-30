from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import pytz




def homePageView(request):
    moscow_time = datetime.now(pytz.timezone('Europe/Moscow'))
    return render(request, 'pages/home.html', {'time': moscow_time.strftime("%H:%M:%S") })
