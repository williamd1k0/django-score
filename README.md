# Django Score

![python-version](https://img.shields.io/badge/python-v3.5%2B-blue.svg?style=flat-square)
![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)

## Before installation (optional)

Use a *virtualenv* in development to prevent conflicts with the dependencies ([more info about virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).

You can install virtualenv via pip:

```bash
pip install virtualenv
```

Create an env ignoring all site-packages:

```bash
virtualenv env --no-site-packages
```

Activate the env:

* Bash on Linux:
```bash
source env/bin/activate
```

* Bash on Windows:
```bash
source env/Scripts/activate
```

* CMD/PowerShell:
```bash
.\env\Scripts\activate
```

## Installation

Intall server dependencies using pip:

```bash
pip install -r requirements.txt
```

For Python linting and other development tools, install devel requirements (optional):

```bash
pip install -r requirements-devel.txt
```

## Initializing database tables

Change to `django_score` directory and make/apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Starting the server

Execute the runserver Django command:

* Bash on Linux or CMD/PowerShell:
```bash
python manage.py runserver
```

* Bash on Windows (for pty support):
```bash
winpty python manage.py runserver
```

## Testing score system

>TODO