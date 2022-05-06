from django.db import models


class Phone(models.Model):
    id = models.indexes
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    image = models.TextField(max_length=500)
    release_date = models.CharField(max_length=10)
    lte_exists = models.BooleanField(default=0)
    slug = models.CharField(max_length=100)    
