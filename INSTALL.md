Powershell Windows

Cloning the Repository
======================

(https://stackoverflow.com/questions/11621768/how-can-i-make-git-accept-a-self-signed-certificate/26785963#26785963)

`$Env:GIT_SSL_CAINFO = "C:\path\to\cert.pem"`

`git clone https://github.com/schmid42/edith-stein-schule.net.git`

Python Virtual Environment
=======

`cd .\edith-stein-schule.net\`

`python -m venv venv`

`.\venv\Scripts\activate`

Backend
=======

(https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi)

`cd backend`

`python -m pip install --upgrade pip --cert C:\path\to\cert.pem`

`pip install -r requirements.txt --cert C:\path\to\cert.pem`

`$Env:DJANGO_SETTINGS_MODULE = "main.settings.dev"`

`python manage.py migrate`

`python manage.py createsuperuser`

frontend
========

in root directory

`cd frontend`

`npm init`

RUNNING
=======

Backend
-------

`python manage.py runserver`

Frontend
--------

