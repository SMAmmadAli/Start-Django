from django.db import models

# Create your models here.


class Product(models.Model):
    category = models.CharField(max_length=100)
    decription = models.CharField(max_length=1000)
    manufacture = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    timeStamp = models.DateTimeField(
        auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return self.name
