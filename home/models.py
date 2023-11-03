from django.db import models
# 4.11.23
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload="categories")


class Product(BaseModel):
    Product_name = models.CharField(max_length=100)
    category = models.IntegerField(Category, on_delete= models.CASCADE, related_name="product")
    price = models.IntegerField()
    product_description = models.TextField()


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name="product_image")
    image = models.ImageField(upload="product")

#4.11.23



# Create your models here.

class Registration(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    date=models.DateField()

    def __str__(self):
        return self.name
    