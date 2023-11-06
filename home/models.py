from django.db import models


# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateField()

    def __str__(self):
        return self.name
    



class ItemInsert(models.Model):
    item_id = models.AutoField
    item_group = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=30)
    stock_qty = models.IntegerField()
    item_rate = models.IntegerField(default=0)
    item_date = models.DateField()
    image = models.ImageField(upload_to="seller/images", default="")

    def __str__(self):
        return self.item_desc
    