import requests
from places.models import Place, Image

response = requests.get('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D0%BD%D1%82%D0%B8%D0%BA%D0%B0%D1%84%D0%B5%20Bizone.json')
place_data = response.json()

created_place = Place.objects.create(
    title = place_data.title,
    placeId = '',
    description_short = place_data.description_short,
    description_long = place_data.description_long,
    lat = place_data.lat,
    lng = place_data.lng
)

