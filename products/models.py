from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    is_live = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
