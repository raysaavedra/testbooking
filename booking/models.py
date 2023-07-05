from django.db import models

# Create your models here.

class Booking(models.Model):
    customer_first_name = models.CharField(max_length=255)
    customer_last_name = models.CharField(max_length=255)
    customer_address = models.TextField()
    customer_contact_number = models.CharField(max_length=255)
    shop_name = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255)
    schedule = models.DateTimeField() #start
    schedule_end = models.DateTimeField()

