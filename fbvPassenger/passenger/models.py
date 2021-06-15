from django.db import models

# Create your models here.
class Passenger(models.Model):
    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    travelPoints = models.CharField(max_length=30)

    def __str__(self):
        return self.firstName + self.lastName