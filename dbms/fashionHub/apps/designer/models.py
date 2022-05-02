from django.db import models
from apps.core.models import User


# Create your models here.

class Designer(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='designer', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']


    def get_balance(self):
        items = self.items.filter(designer_paid = False, order__designers__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)

    def get_paid_amount(self):
        items = self.items.filter(designer_paid = True, order__designers__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)