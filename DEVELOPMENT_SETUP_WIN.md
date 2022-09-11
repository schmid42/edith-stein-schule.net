# Setup develepment environment under Windows

## required software

## Setup backend

* clone the repository

```shell
git clone https://github.com/schmid42/edith-stein-schule.net.git
cd edith-stein-schule.net
```

* create a new virtual environment and activate it

```powershell
python -m venv venv
.\venv\Scripts\activate
```

* install dependenies

```shell
python -m pip install --upgrade pip
cd backend
pip install -r .\requirements.txt
pip install gunicorn
pip install psycopg2
```

* create a `.env` file for the backend

```powershell
cp .\.env.example .\.env
```

* edit `.env` to set development environment

* setup wagtail

```shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Setup Frontend

```powershell
cd ..\frontend\
npm install
npm run production
npm run development
```

## Documentation

<https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/>
<https://docs.gunicorn.org/en/latest/deploy.html>
