$ python -m venv venv
$ source venv/bin/activate
$ cd backend
$ cp .env.example .env
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ pip install gunicorn
$ pip install psycopg2

$ python manage.py migrate
$ python manage.py createsuperuser
$ cd ../frontend
$ npm install
$ npm run production



# database


https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/gunicorn/
https://docs.gunicorn.org/en/latest/deploy.html

