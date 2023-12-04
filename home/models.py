from django.db import models


# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateField()

    def __str__(self):
        return self.name
    



class ItemInsert(models.Model): 
    item_group = models.CharField(max_length=30)
    item_desc = models.CharField(max_length=30)
    stock_qty = models.IntegerField()
    item_rate = models.IntegerField(default=0)
    item_date = models.DateField()
    image = models.ImageField(upload_to="seller/images", default="")

    def __str__(self):
        return self.item_desc
    



class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    mobile = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name    
      