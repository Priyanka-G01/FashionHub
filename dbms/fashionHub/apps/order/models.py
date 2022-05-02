from django.db import models
from apps.product.models import Product
from apps.designer.models import Designer
from apps.customer.models import Customer

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    place= models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=9,decimal_places=2)
    designers = models.ManyToManyField(Designer, related_name='orders')
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, related_name='order' )

    class Mata:
        ordering = ['-created_at']

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='items',on_delete=models.CASCADE)
    designer = models.ForeignKey(Designer,related_name='items',on_delete=models.CASCADE)
    designer_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

    def get_total_price(self):
        return self.price * self.quantity

