$ python -m venv venv
$ source venv/bin/activate
$ cd backend
$ cp .env.example .env
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ cd ../frontend
$ npm install
$ npm run production
