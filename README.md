# ENGO-651 final project

## Project setup
Run the following commands in your terminal:

```terminal
  python -m venv .env
```

Activate (.env) environment

```terminal
  source .env/bin/active
```

Install dependencies

```terminal
  pip install -r requirements.txt
```

Then create a postgres database with the name `fuellytics`. The default settings are listed below and you can
in find these in the fuellytics/settings.py file. 

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

Alternatively, you can use other values for `DATABASE_NAME`, `DATABASE_USER` and `DATABASE_PASSWORD` 
by creating a `.env` file inside the fuellytics directory. For example:

```
DATABASE_NAME=mydatabase
ADMIN_USERNAME=myusername
ADMIN_PASSWORD=mypassword
```

Then to start the DB

```
sudo service postgresql start
```

To run migrations:

```
python manage.py migrate
```

Finally, to run the project:

```
python manage.py runserver
```

