# ENGO-651 final project

## How to run the project
First make sure you have a DB setup with ```NAME = fuellytics```, ```USER = postgres``` and ```PASSWORD = postgres``` You can see the db settings in the settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'fuellytics'),
        'USER': os.getenv('DATABASE_USER', 'postgres'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'postgres'),
        'HOST': "127.0.0.1",
        'PORT': "5432",
    }
}
```

Then in your terminal run

```terminal
  python -m venv .env
  source .env/bin/active
  pip install -r requirements.txt
```

To start the DB

```
sudo service postgresql start
```

Then run migrations

```
python manage.py migrate
```

Finally, to run the project:

```
python manage.py runserver
```

