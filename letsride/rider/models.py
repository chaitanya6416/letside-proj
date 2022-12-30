from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)


# class rider_details(models.Model):
#     name = models.CharField(max_length=255)
#     start_location = models.CharField(max_length=255)
#     end_location = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=255)