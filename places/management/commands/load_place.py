from msilib.schema import Error
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from slugify import slugify
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Pull place from a json and fill the database'

    def add_arguments(self, parser):
        parser.add_argument('src_link', nargs='+')

    def attache_image(self, img_link, img_data, place_obj, position):
        img_content = ContentFile(img_data.content)
        img_obj = Image.objects.create(position=position, place=place_obj)
        img_name = img_link.split('/')[-1]
        img_obj.image.save(img_name, img_content)
        img_id = img_obj.save()
        return img_id

    def handle(self, *args, **options):
        for src_link in options['src_link']:
            try:
                place_json = requests.get(src_link).json()
            except requests.exceptions.RequestException as err:
                self.stdout.write(self.style.ERROR(err))
                continue
            place_obj, created = Place.objects.get_or_create(
                slug=slugify(place_json['title']),
                defaults={
                    'title': place_json['title'],
                    'description_short': place_json['description_short'],
                    'description_long': place_json['description_long'],
                    'lat': place_json['coordinates']['lat'],
                    'lng': place_json['coordinates']['lng'],
                }
            )
            if created:
                position = 0
                for img_link in place_json['imgs']:
                    try:
                        img_data = requests.get(img_link)
                    except requests.exceptions.RequestException as err:
                        self.stdout.write(self.style.ERROR(err))
                        continue
                    try:
                        self.attache_image(img_link, img_data,
                                           place_obj, position)
                        position += 1
                    except Exception as err:
                        self.stdout.write(self.style.ERROR(err))
                if len(place_obj.images.all()) == len(place_json['imgs']):
                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully processed data for {place_obj.title}'))
                else:
                    self.stdout.write(self.style.WARNING(
                        f'There were not all images loaded for \
                        {place_obj.title}'))
