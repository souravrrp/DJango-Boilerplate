
## Project Title
DJango Boilerplate

## Project Overview
DJango Boilerplate

## End User
* Developer Department

## Version No
v1.02

## System Requirements
* Apache 2.4 with mod_wsgi
* Python 3.7
* Django 3.0.3
* MariaDB 10.6

## Installation
Create directory
`
mkdir <dirname>  
`

Go to the directory
`
cd <dirname> 
`

Open/Run Command prompt or type addresbar `cmd` and type 
`
code .
`

Create virtual environment first and active
`
python -m venv venv
`

Start virtual environment
`
.venv\scripts\activate
`

Install required packages
`
pip install -r requirements.txt
`

Create and migrate database
`
python manage.py makemigrations
`
`
python manage.py migrate
`


`
pip install Django==3.2

django-admin startproject config .

django-admin startapp api

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

User: admin

Mail: 
`
sourav.paul@singerbd.com
`

Password: 
`
admin123
`
`
y
`

Run Python Server Default
`
python manage.py runserver
`

Run Python Server Customized
`
python manage.py runserver 127.0.0.2:7000 
`

Run Python Server Customized
`
pip freeze > requirements.txt
`

url: http://127.0.0.1:8000/