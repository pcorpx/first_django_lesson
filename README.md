# Where to go

This website based on Django and serves as a learning project. It presents information about different places on the map. It has convinient admin panel. You may follow this link https://pcorp.pythonanywhere.com/ to see live.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use.

### Prerequisites

Clone project to your local machine:

`git clone ...`

It's necessary to have right environment:

* Django==3.2.10
* Pillow==8.4.0
* django-admin-sortable2==1.0.3
* django-tinymce==3.4.0
* environs==9.3.5
* requests==2.27.0
* python-slugify==6.1.1

You may use requirements file to prepare your environment:

`pip install -r requirements.txt`

Also you should provide your environment with the right sef of variables and their values:

* __SECRET_KEY__
  *The value is used for generating cryptographic signature. It is critical data and mustn't be in public*
* __DATABASE_FILEPATH__ 
  *The value defines path to the database for the project*
* __ALLOWED_HOSTS__
  *A list of strings representing the host/domain names that this Django site can serve*
* __DEBUG__
  *A boolean that turns on/off debug mode. Default: False*

Put those variables with values to .env file in the same directory as file manage.py 

Before launching the website you also should create user for authentication to the admin panel:

`python manage.py createsuperuser`
 
### Launch of the website
 
You may use any webserver for serving website. For example, it is possible to start with simple python build-in webserver:
 
`python -m http.server 8000`

### To fill the website with data you may use script as follows

`python manage.py load_place <url_to_the_json_data>`

The <url_to_the_json_data> is the url link to json file with data of place.
The following json is an example of valid data which you may use to make your own file.

```
{
    "title": "Лагерь «Подмосковный»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/d70328bcfd30a5751fc8b833918d1e94.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0976915841002135611c3697a7b4f3f9.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/b3df33667dfd510b2c6baf78f6714190.jpg"
    ],
    "description_short": "«Кто шагает дружно в ряд — это сталкеров отряд», — так сегодня звучит кричалка заброшенного пионерлагеря «Подмосковный». Доехав до ж/д платформы «Кузяево» и пробравшись сквозь лес к месту назначения, можно почувствовать себя не только настоящим сталкером, но и, как говорят, увидеть пионеров-призраков.",
    "description_long": "<p>В своё время лагерь «Подмосковный» считался престижным местом отдыха детей «Мостотреста». Здесь могли разместиться до 2000 человек.</p><p>Из особенностей лагерной жизни тех лет бывалые вспоминают обилие комаров, ящериц и змей в кузяевских лесах, а также кузяевский фарфор, который, как бы сейчас сказали, был спонсором лагеря. Фарфоровые трофеи до сих пор периодически находят на развалинах. В лагере сохранились добротно выстроенные двухэтажные кирпичные корпуса, бассейн, искусственный водоём и традиционный для всех лагерей киноконцертный зал.</p><p>Масштабы и оснащённость лагеря восхищают. Однако сразу после закрытия лагерь, как водится, был «раздет догола» вандалами. На развалинах проводятся квесты, однако нужно быть предельно осторожным, чтобы не свалиться в какой-нибудь подвал или не наткнуться на оголённую арматуру, внутри корпусов находиться небезопасно.</p><p>Сегодня, помимо сталкеров, ищущих романтики на этих руинах, лагерь стал плацдармом для любителей экстремального пейнтбола. Но местные жители до сих пор жалеют о разрушении «Подмосковного» и охотно рассказывают истории о призраках пионеров.</p><p>Лагерь не охраняется, вход свободный.</p>",
    "coordinates": {
        "lng": "38.02520099999999",
        "lat": "55.59279999999996"
    }
}
```