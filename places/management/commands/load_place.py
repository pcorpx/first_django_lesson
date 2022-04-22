from doctest import Example
import requests
import logging
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from slugify import slugify
from places.models import Place, Image


logging.basicConfig(
    format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s \
             [%(asctime)s] %(message)s',
    handlers=[logging.FileHandler('mylog.log', 'a', 'utf-8')], 
    level = logging.DEBUG
)


class Command(BaseCommand):
    help = 'Pull place from a json and fill the database'

    def add_arguments(self, parser):
        parser.add_argument('src_link', nargs='+')

    def attache_image(self, image_link, requested_image,
                      created_place, position):
        image = ContentFile(requested_image)
        created_image = Image.objects.create(position=position,
                                             place=created_place)
        image_name = image_link.split('/')[-1]
        created_image.image.save(image_name, image)
        image_id = created_image.save()
        return image_id

    def handle(self, *args, **options):
        for src_link in options['src_link']:
            try:
                response = requests.get(src_link)
                response.raise_for_status()
                requested_place = response.json()
                if 'error' in requested_place:
                    raise requests.exceptions.HTTPError(requested_place['error'])
            except requests.exceptions.HTTPError as err:
                self.stdout.write(self.style.ERROR('Http Error ' + str(err)))
                logging.debug(err)
                continue
            except requests.exceptions.ConnectionError as err:
                self.stdout.write(self.style.ERROR('Error Connecting ' + str(err)))
                logging.debug(err)
                continue
            except requests.exceptions.Timeout as err:
                self.stdout.write(self.style.ERROR('Timeot Error ' + str(err)))
                logging.debug(err)
                continue
            except requests.exceptions.JSONDecodeError:
                self.stdout.write(self.style.ERROR('Non valid format of json file'))
                logging.debug('Non valid format of json file')
                continue
            except requests.exceptions.MissingSchema:
                self.stdout.write(self.style.ERROR('Non valid format of url (ex. http://name.ru)'))
                logging.debug('Non valid format of url. (ex. http://name.ru)')
                continue
            except requests.exceptions.RequestException as err:
                self.stdout.write(self.style.ERROR(err))
                logging.debug(err)
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
            if not created:
                continue

            for position, image_link in enumerate(requested_place['imgs']):
                try:
                    response = requests.get(image_link)
                    response.raise_for_status()
                    requested_image = response.content
                except requests.exceptions.HTTPError as err:
                    self.stdout.write(self.style.ERROR('Http Error ' + str(err)))
                    logging.debug(err)
                    continue
                except requests.exceptions.ConnectionError as err:
                    self.stdout.write(self.style.ERROR('Error Connecting ' + str(err)))
                    logging.debug(err)
                    continue
                except requests.exceptions.Timeout as err:
                    self.stdout.write(self.style.ERROR('Timeot Error ' + str(err)))
                    logging.debug(err)
                    continue
                except requests.exceptions.MissingSchema:
                    self.stdout.write(self.style.ERROR('Non valid format of url (ex. http://name.ru)'))
                    logging.debug('Non valid format of url. (ex. http://name.ru)')
                    continue
                except requests.exceptions.RequestException as err:
                    self.stdout.write(self.style.ERROR(err))
                    logging.debug(err)
                    continue
                try:
                    self.attache_image(image_link, requested_image,
                                        created_place, position)
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
