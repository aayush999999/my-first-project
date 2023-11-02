from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
   
    date=models.DateField()

    def __str__(self):
        return self.name
    