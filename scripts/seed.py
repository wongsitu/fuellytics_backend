from cars.models import Car
import requests
import csv

# https://towardsdatascience.com/use-python-scripts-to-insert-csv-data-into-django-databases-72eee7c6a433
def run():
    Car.objects.all().delete()

    url = "https://fuellytics-media.s3.us-west-2.amazonaws.com/cars.csv"
    response = requests.get(url)
    content = response.content.decode('utf-8')
    csv_reader = csv.reader(content.splitlines(), delimiter=',')

    next(csv_reader)

    for row in csv_reader:
            print(row)

            car = Car(make=row[2],
                        model=row[3],
                        displacement=row[4],
                        year=row[1],
                        is_supercharged=row[6],
                        drag=row[5],
                        )
            car.save()