from django.db import models

# Create your models here.
class Country(models.Model):
    countryid = models.IntegerField(primary_key = True)
    countryname = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 100)

class Capital(models.Model):
    capitalid = models.IntegerField(primary_key = True)
    capitalname = models.CharField(max_length = 100)