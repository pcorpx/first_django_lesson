from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import requests
from slugify import slugify
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Pull place from a json and fill the database'

    def add_arguments(self, parser):
        parser.add_argument('src_link', nargs='+')

    def attache_image(self, image_link, requested_image,
                      created_place, position):
        image = ContentFile(requested_image.content)
        created_image = Image.objects.create(position=position,
                                             place=created_place)
        image_name = image_link.split('/')[-1]
        created_image.image.save(image_name, image)
        image_id = created_image.save()
        return image_id

    def handle(self, *args, **options):
        for src_link in options['src_link']:
            try:
                requested_place = requests.get(src_link).json()
            except requests.exceptions.RequestException as err:
                self.stdout.write(self.style.ERROR(err))
                continue
            created_place, created = Place.objects.get_or_create(
                slug=slugify(requested_place['title']),
                defaults={
                    'title': requested_place['title'],
                    'description_short': requested_place['description_short'],
                    'description_long': requested_place['description_long'],
                    'lat': requested_place['coordinates']['lat'],
                    'lng': requested_place['coordinates']['lng'],
                }
            )
            if created:
                position = 0
                for image_link in requested_place['imgs']:
                    try:
                        requested_image = requests.get(image_link)
                    except requests.exceptions.RequestException as err:
                        self.stdout.write(self.style.ERROR(err))
                        continue
                    try:
                        self.attache_image(image_link, requested_image,
                                           created_place, position)
                        position += 1
                    except Exception as err:
                        self.stdout.write(self.style.ERROR(err))
                if len(created_place.images.all()) == \
                   len(requested_place['imgs']):
                    self.stdout.write(self.style.SUCCESS(
                        'Successfully processed data for ' +
                        created_place.title
                        )
                    )
                else:
                    self.stdout.write(self.style.WARNING(
                        'There were not all images loaded for ' +
                        created_place.title
                        )
                    )
