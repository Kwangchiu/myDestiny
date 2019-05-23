from django.shortcuts import render

# Create your views here.
def index(request):
    years = range(1920, 2050)
    month = range(1, 20)
    day = range(1,39)
    return render(request, 'index.html', {"year":years, "month":month, "day":day})

def year(request):
    years = range(1920, 2020)
    return render(request, 'index.html', {"data":years})