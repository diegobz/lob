
Pet project to work with django-rest-framework

## Dev setup requirements

    python-3.8
    virtualenv
    sqlite


## Instalation

    git clone https://github.com/diegobz/lob.git
    cd lob
    mkvirtualenv lob
    pip install -r requirements.txt
    cd src
    ./manage.py migrate
    ./manage.py loaddata addresses/fixtures/addresses.json


## Running test

    ./manage.py test

## Running the app

    ./manage.py runserver

## Using it

    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/addresses/


    curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/addresses/?search=1600