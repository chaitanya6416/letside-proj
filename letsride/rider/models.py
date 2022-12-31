from django.db import models
from datetime import date

class Rider(models.Model):
    BUS = 'bus'
    CAR = 'car'
    TRAIN = 'train'
    MEDIUM_CHOICES = [
        (BUS, 'Bus'),
        (CAR, 'Car'),
        (TRAIN, 'Train'),
    ]
    name = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date_of_travel = models.DateField(default=date(2022,1,1))
    travel_medium = models.CharField(max_length=5, choices=MEDIUM_CHOICES, default=BUS)
    phone_number = models.CharField(max_length=255, default='0')


# class rider_details(models.Model):
#     name = models.CharField(max_length=255)
#     start_location = models.CharField(max_length=255)
#     end_location = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255)