from typing import Tuple
from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('E', 'Electronics'),
        ('B', 'Books'),
        ('C', 'Computers'),
        ('GF', 'Girls Fashion'),
        ('PC', 'Personal Care'),
        ('MF', 'Mens Fashion')

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, default="", upload_to="images/")
    brand = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return self.name