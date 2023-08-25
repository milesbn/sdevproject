from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()
    trending = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_curtain = models.BooleanField(default=False)
    is_blind = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)