from django.db import models
from apps.core.models import User


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['name']

   