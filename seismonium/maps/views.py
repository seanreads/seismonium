# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
# from maps.models import Map

def index(request):
  # map = Map.objects.all()  
  # context = {'map': map}
  context = {}
  return render(request, 'maps/index.html', context)

def earthquakes(request):
  url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
  import requests
  data = requests.get(url)
  return HttpResponse(data, mimetype='application/json')
