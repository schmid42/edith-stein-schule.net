# edith-stein-schule.net
Ein CMS für die Edith-Stein-Schule Aichach.

## verwendete Technologien

### backend
* Python 3.8
* Wagtail

### frontend

#### client
* Bulma
* glide.js
* Ionicons

#### build
* Webpack
* node-sass

## development workflow

### backend
* virtual environment aktivieren

    ``source venv/bin/activate`` 

* development Server starten

    ``cd backend``

    ``$env:DJANGO_SETTINGS_MODULE = "main.settings.dev"``

    ``python manage.py runserver``

### frontend
* development Server starten

    ``cd frontend``
    
    ``npm run develop``

## production workflow

### backend

### frontend
