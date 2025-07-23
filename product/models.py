from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Product(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    area = models.DecimalField(max_digits=6, decimal_places=2)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    geo = models.TextField()
    promo_video = models.FileField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.title
