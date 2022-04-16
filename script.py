import requests
from places.models import Place, Image
from environs import Env


env = Env()
env.read_env()
source_link = env.str('SOURCE_LINK')
response = requests.get(source_link)
place_data = response.json()

created_place = Place.objects.create(
    title = place_data.title,
    placeId = '',
    description_short = place_data.description_short,
    description_long = place_data.description_long,
    lat = place_data.lat,
    lng = place_data.lng
)
