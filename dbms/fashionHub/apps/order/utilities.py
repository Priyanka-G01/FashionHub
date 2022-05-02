from apps.cart.cart import Cart
from .models import Order, OrderItem
from django.core.mail import send_mail

def checkout(request, first_name, last_name, email, address, zipcode, place, phone, amount):
    order = Order.objects.create(first_name=first_name, last_name=last_name, email=email, address=address, zipcode=zipcode, place=place, phone=phone, paid_amount=amount,customer=request.user.customer)
    
    for item in Cart(request):
        OrderItem.objects.create(order=order, product=item['product'], designer=item['product'].designer, price=item['product'].price, quantity=item['quantity'])

        order.designers.add(item['product'].designer)
        
    return order



