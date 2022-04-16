from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.urls import reverse
from places.models import Place, Image


def index(request):
    features = []
    for place in Place.objects.all():
        feature = {
                      'type': 'Feature',
                      'geometry': {
                          'type': 'Point',
                          'coordinates': [place.lng, place.lat]
                      },
                      'properties': {
                           'title': place.title,
                           'placeId': place.placeId,
                           'detailsUrl': reverse('get-place',
                                                 args=[place.id])
                      }
                  }
        features.append(feature)

    places_data = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'index.html', 
                  context={'places_data': places_data})


def get_place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = []
    for image in place.images.all():
        images.append(image.image.url)
    place_data = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat
        }
    }
    return JsonResponse(place_data, json_dumps_params={
        'ensure_ascii': False, 'indent': 4
    })
