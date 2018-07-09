from django.db import models

# Create your models here.

class Member(models.Model):
    Description= models.CharField(max_length=40)
    Lattitude= models.CharField(max_length=40)
    Longitude= models.CharField(max_length=40)
    Elevation= models.CharField(max_length=40)
    CreatedDate= models.CharField(max_length=40)

    def __str__(self):
        return self.Description + " " + self.Lattitude + " " + self.Longitude + " " + self.Elevation + " " + self.CreatedDate
