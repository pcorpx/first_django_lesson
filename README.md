# Where to go

This website based on Django and serves as a learning project. It presents information about different places on the map. It has convinient admin panel.

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
