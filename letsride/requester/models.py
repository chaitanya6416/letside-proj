from django.db import models
from datetime import date

class Requester(models.Model):

    LAPTOP = 'laptop'
    TRAVEL_BAG = 'travel_bag'
    PACKAGE = 'package'
    ASSET_CHOICES = [
        (LAPTOP, 'Laptop'),
        (TRAVEL_BAG, 'Travel_Bag'),
        (PACKAGE, 'Package')
    ]

    HIGHLY_SENSITIVE = 'highly_sensitive'
    SENSITIVE = 'sensitive'
    NORMAL ='normal'
    SENSITIVITY_CHOICES = [
        (HIGHLY_SENSITIVE, 'Highly_Sensitive'),
        (SENSITIVE, 'Sensitive'),
        (NORMAL, 'Normal')
    ]
    
    name = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date_of_travel = models.DateField(default=date(2022,1,1))
    asset_type = models.CharField(max_length=20, choices = ASSET_CHOICES, default=PACKAGE)
    sensitivity = models.CharField(max_length=20, choices = SENSITIVITY_CHOICES, default=NORMAL)
