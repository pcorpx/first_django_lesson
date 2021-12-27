from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from places.models import Place

def index(request):
    features = []

    for place in Place.objects.all():
        feature = {
                      "type": "Feature",
                      "geometry": {
                          "type": "Point",
                          "coordinates": [place.lng, place.lat]
                      },
                      "properties": {
                           "title": place.title,
                           "placeId": place.placeId,
                           "detailsUrl": "/places"
                      }
                  }
        features.append(feature)

    places_data = {
        "type": "FeatureCollection",
        "features": features
    }
    return render(request, 'index.html', context={'places_data': places_data})
