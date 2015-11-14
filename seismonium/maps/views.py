# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from maps.models import Earthquake, Setting

def index(request):

  settings = Setting.objects.all()  
  # context = {'map': map}
  context = {}
  return render(request, 'maps/index.html', context)


def earthquakes(request):

  count = Earthquake.objects.count()

  if count > 0:
    earthquakes = Earthquake.objects.latest('cached_at')
    cached_at = earthquakes.cached_at

  import datetime, pytz
  utc = pytz.UTC
  cache_interval = Setting.objects.get(name='geojson_cache_interval').value  
  cache_time = utc.localize(datetime.datetime.utcnow() - datetime.timedelta(minutes=int(cache_interval)))

  if ((count == 0) or (cached_at < cache_time)):
    import requests
    url = Setting.objects.get(name='geojson_url').value
    response = requests.get(url)
    earthquakes = Earthquake(geojson=response.content)
    earthquakes.save()

  return HttpResponse(earthquakes.geojson, content_type='application/json')
