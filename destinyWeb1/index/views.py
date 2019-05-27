from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import json

# Create your views here.
def index(request):
    years = range(1920, 2050)
    month = range(1, 19)
    day = range(1,38)
    return render(request, 'index.html', {"year":years, "month":month, "day":day})

def year(request):
    years = range(1920, 2020)
    return render(request, 'index.html', {"data":years})

'''def bazi(request):
    import os
    os.system('python <index\pyFile\bazi.py>')
'''

def login(request):
    if request.method == "GET":
        result = {}
        year = request.GET.get('year')
        month = request.GET.get('month')
        day = request.GET.get('day')
        time = request.GET.get('time')
        result['year'] = year
        result['month'] = month
        result['day'] = day
        result['time'] = time
        result = json.dumps(result)

        return HttpResponse(result, content_type='application/json;charset=utf-8')

    return render(request, 'index.html', {'times': result})
