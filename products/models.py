from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    kgs= models.FloatField(default=0)
    stock_kgs= models.IntegerField(default=0)
    image_url = models.CharField(max_length=2100)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()
