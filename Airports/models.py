from django.db import models

# Create your models here.


class Airport(models.Model):
    ident = models.CharField(max_length=10)  # max7 pk=True
    type = models.CharField(max_length=20)  # max14
    name = models.CharField(max_length=100)  # max83
    latitude_deg = models.CharField(max_length=25)  # max24
    longitude_deg = models.CharField(max_length=25)  # max21
    elevation_ft = models.IntegerField()  # max5
    continent = models.CharField(max_length=2)  # max2
    iso_country = models.CharField(max_length=2)  # max2
    iso_region = models.CharField(max_length=10)  # max7
    municipality = models.CharField(max_length=100)  # max51
    scheduled_service = models.CharField(max_length=10)  # max3
    gps_code = models.CharField(max_length=10,null=True,blank=True)  # max4
    iata_code = models.CharField(max_length=3,null=True,blank=True)  # max3
    local_code = models.CharField(max_length=10,null=True,blank=True)  # max7
    home_link = models.CharField(max_length=150,null=True,blank=True)  # max128
    wikipedia_link = models.CharField(max_length=150,null=True,blank=True)  # max128
    keywords = models.CharField(max_length=500,null=True,blank=True)  # max300

    def __str__(self):
        return self.ident +'- '+self.type +' ('+self.name+')'
